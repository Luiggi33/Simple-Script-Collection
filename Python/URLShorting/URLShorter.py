import config
import urllib
import requests

key = config.apiKey
apiURL = urllib.parse.quote(input("Paste URL to shorten: "))
name = input("Enter a name for the shortened URL: ")

r = requests.get(
    "https://cutt.ly/api/api.php?key={}&short={}&name={}".format(key, apiURL, name))

result = r.json()
url = result['url']

if url["status"] != 7:
    print("Error: {}".format(url["status"]))
    exit()

print("\nTitle: {}".format(url["title"]))
print("Shortened URL: {}".format(url["shortLink"]))
print("\n")
