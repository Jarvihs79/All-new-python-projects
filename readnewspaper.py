from win32com.client import Dispatch
speak = Dispatch("SAPI.SpVoice")
speak.Speak("hii hello this is me")


