import requests
import json
import win32com.client as wincom
if __name__ == '__main__':
    city =input("Enter your city name..\n")
    speak = wincom.Dispatch("SAPI.SpVoice")
    url =f"https://api.weatherapi.com/v1/current.json?key=a936889769ca4aa3a63185305231310&q={city}"
    r = requests.get(url)
    print(r.text)
    wdic = json.loads(r.text)
    print(wdic)
    w = wdic["current"]["temp_c"]
    speak.speak(f"The current weather in {city} is {w} degrees")

