import requests
a=requests.get('https://www.geeksforgeeks.org/python-requests-tutorial/')
#print(a.content)
print(a.status_code)
print(a.url)
#print(a.text)
print(a.headers)
print(a.c)