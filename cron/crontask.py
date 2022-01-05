import requests
import random
import string


def generate_seed(n):
    return ''.join([random.choice(string.digits) + random.choice(string.digits) +
                    random.choice('abcde'.upper()) +
                    random.choice(string.digits) + random.choice(string.digits) + '-' for _ in range(n)])[:-1]


data={"seed": generate_seed(4)}
headers={"Content-Type": "application/json"}
print(data)
request=requests.post('http://web:8000/api/v1/daily/create/',data=data)
print(request)
