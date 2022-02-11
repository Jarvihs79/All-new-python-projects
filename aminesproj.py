import requests
a=requests.get('https://en.wikipedia.org/wiki/Naruto')
b=a.json()
print(b)