# Install dependency
```bash
pip install -r requirements.txt
```

# How to use 

## Ping Tele server first time
```bash
python ping_login.py
```
Contact to `+84 899 254 268` to take the confirm code.

## Using built-in function
After ping, you can use the function `send_and_receive_ans`
```python
from api_func_call import send_and_receive_ans

#Only parameter is the 'message' you want to send, the return object is the reply of model

return_message = send_and_receive_ans('Làm sao để ngụp 10 lần 1 ngày, hãy nêu dẫn chứng từ Bùi Đức đến từ Bùi Xương Trạch.')

print(return_message)

```


## Using API Server
After ping, you can run api server
```bash
python app.py

```

