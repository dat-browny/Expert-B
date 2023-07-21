# Enhancing Natural Language Comprehension through Multilingual Large Language Models and Instruction-Based Techniques

My Thesis provides data, models, and evaluation benchmark for large language models.

## Latest News
- [05/10/2023]: Release dataset and training code. 

## Motivation
- Achieving maximum utilization of ChatGPT requires not only employing straightforward techniques but also minimizing the expenses associated with training and inference.

- Make ChatGPT-like LLM accessible across countries and languages, especially for Vietnamese.

##  Get started
### Install
Run the following command to install the required packages:

```angular2html
pip install -r requirements.txt
```

## Data
### Overview
Used the following two sources of data for training `Bloom`

- [Alpaca](https://github.com/tatsu-lab/stanford_alpaca/blob/main/alpaca_data.json)
- [Dolly](https://huggingface.co/datasets/databricks/databricks-dolly-15k/blob/main/databricks-dolly-15k.jsonl)

Based on my experience, the datasets mentioned above are of the highest quality for training a model according to the given instructions. Certainly, I can look into additional public sources of data such as [Phoenix](https://github.com/FreedomIntelligence/LLMZoo) and [GPT4ALL](https://github.com/nomic-ai/gpt4all) that may be relevant to the task at hand.

In my upcoming plan, I intend to generate Vietnamese instructions utilizing the pipeline outlined below. 
```diff
+ Self-Instructed / Translated (Instruction, Input) in Language A (English)
- ---(Step 1) Translation --->
+ (Instruction, Input) in Language B (Vietnamese) (B is randomly sampled w.r.t. the probability distribution of realistic languages)
- ---(Step 2) Generate--->
+ Output in Language B
```

### Download
- [bloom-v1](https://drive.google.com/drive/folders/1So-QFOMyPe2zQ586-ILs2wG6hMtjf9IC?usp=share_link): The data used for training Bloom.

## Models
Updating...

## Evaluation and Benchmark

updaing...

## Training by yourself
### Prepare the data
You can either download the [bloom-v1](https://drive.google.com/drive/folders/1So-QFOMyPe2zQ586-ILs2wG6hMtjf9IC?usp=share_link) data or prepare your own data. 
Run merge.py to cobine all seperated data into a single file.
```shell
python merge.py --in *.json --out bloom_v1.json
```
### Training
Configuration in `train.sh` file is for a NVIDIA node contain 4xA100 40GB.
```shell
bash train.sh
```

## Acknowledgement

My works are inspired by the following works, including but not limited to

- Bloom: https://huggingface.co/bigscience/bloom
- Self-instruct: https://github.com/yizhongw/self-instruct
- Alpaca: https://github.com/tatsu-lab/stanford_alpaca
- Vicuna: https://github.com/lm-sys/FastChat
