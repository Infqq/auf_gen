import requests
import random

data = requests.get('https://raw.githubusercontent.com/Infqq/auf_gen/main/phrases.txt').text.splitlines()

print(random.choice(data))
