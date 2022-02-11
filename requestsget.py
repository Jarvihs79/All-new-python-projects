import requests
from win32com.client import Dispatch
url = ('https://newsapi.org/v2/top-headlines?'
       'country=in&'
       'apiKey=5142eb5b03734fc398390d12f134334b')
response = requests.get(url)
rud= response.json()
crud=rud['articles']

a=crud[0]['description']
print(a)

#speak = Dispatch("SAPI.SpVoice")
#speak.Speak(crud)