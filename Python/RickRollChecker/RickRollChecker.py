import requests
import config

url = input("Enter a URL: ")

r = requests.get("http://api.linkpreview.net/?key=" + config.apiKey + "&q=" + url)

if "rick astly" in r.json()["title"].lower() or "never gonna give you up" in r.json()["title"].lower() or "rick roll" in r.json()["title"].lower():
    print("\nThis is a Rick Roll!")
else:
    print("\nThis is not a Rick Roll!")

if "rick astly" in r.json()["description"].lower() or "never gonna give you up" in r.json()["description"].lower() or "rick roll" in r.json()["description"].lower():
    print("\nThis is a Rick Roll!")
else:
    print("\nThis is not a Rick Roll!")
