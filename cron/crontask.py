import requests
import random
import string


def generate_seed(n):
    return ''.join([random.choice(string.digits) + random.choice(string.digits) +
                    random.choice(string.ascii_lowercase) +
                    random.choice(string.digits) + random.choice(string.digits) + '-' for _ in range(n)])[:-1]


data={"seed": generate_seed(4)}
headers={"Content-Type": "application/json"}
request=requests.post('http://127.0.0.1:8000/api/v1/daily/create/',data=data)
print(request)
