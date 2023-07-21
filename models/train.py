from dataclasses import dataclass, field
from typing import Optional
import logging

import transformers
from peft import get_peft_model, LoraConfig, TaskType, PeftModel

from src.datasets.datasets import make_supervised_data_module
from src.utils import safe_save_model_for_hf_trainer, CustomTrainer


@dataclass
class ModelArguments:
    model_name_or_path: Optional[str] = field(default="facebook/opt-125m")
    load_from_peft: Optional[str] = field(default=None)
    use_peft: Optional[bool] = field(default=False)


@dataclass
class DataArguments:
    data_path: str = field(default=None, metadata={"help": "Path to the training data."})


@dataclass
class TrainingArguments(transformers.TrainingArguments):
    cache_dir: Optional[str] = field(default=None)
    optim: str = field(default="adamw_torch")
    model_max_length: int = field(
        default=512,
        metadata={"help": "Maximum sequence length. Sequences will be right padded (and possibly truncated)."},
    )


def train():
    parser = transformers.HfArgumentParser((ModelArguments, DataArguments, TrainingArguments))
    model_args, data_args, training_args = parser.parse_args_into_dataclasses()

    model = transformers.AutoModelForCausalLM.from_pretrained(
        model_args.model_name_or_path,
        cache_dir=training_args.cache_dir,
    )
    if model_args.use_peft:
        if model_args.load_from_peft:
            logging.warning(f"Wrapping model with PEFT model at {model_args.load_from_peft}")
            model = PeftModel.from_pretrained(model, model_args.load_from_peft)
        else:
            logging.warning("If you want wrapping model with available PEFT, please use --load_from_peft with PEFT path")
            peft_config = LoraConfig(
            task_type=TaskType.CAUSAL_LM, inference_mode=False, r=8, lora_alpha=16, lora_dropout=0.05, target_modules=["query_key_value"]
            )
            logging.warning(f"Use PEFT to training with config {peft_config}")
            model = get_peft_model(model, peft_config)
        model.print_trainable_parameters()

    tokenizer = transformers.AutoTokenizer.from_pretrained(
        model_args.model_name_or_path,
        cache_dir=training_args.cache_dir,
        model_max_length=training_args.model_max_length,
        padding_side="right"
    )

    data_module = make_supervised_data_module(tokenizer=tokenizer, data_args=data_args)

    trainer = CustomTrainer(model=model, tokenizer=tokenizer, args=training_args, **data_module)

    trainer.train()
    trainer.save_state()
    safe_save_model_for_hf_trainer(trainer=trainer, output_dir=training_args.output_dir)

if __name__ == "__main__":
    train()
