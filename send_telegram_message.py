import os  # 添加 os 模块的导入语句
import random
import requests

# 生成随机消息
with open('message.txt', 'r') as f:
    messages = f.read().splitlines()
message = random.choice(messages)

# 将消息发送给你的朋友
url = f'https://api.telegram.org/bot{os.environ["BOT_TOKEN"]}/sendMessage'  # 使用 os.environ 访问环境变量
data = {'chat_id': os.environ["USER_ID"], 'text': message}
response = requests.post(url, data=data)
print(response.json())
