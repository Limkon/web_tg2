import random
import requests

# Generate a random message.
with open('message.txt', 'r') as f:
    messages = f.read().splitlines()
message = random.choice(messages)

# Send the message to your friend.
url = f'https://api.telegram.org/bot{os.environ["BOT_TOKEN"]}/sendMessage'
data = {'chat_id': os.environ["USER_ID"], 'text': message}
response = requests.post(url, data=data)
print(response.json())
