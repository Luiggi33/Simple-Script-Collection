import requests
import config

number = input("\nEnter a phonenumber: ")
number = number.replace(" ", "")
number = number.replace("-", "")

country_code = input("\nEnter the Country Code (like DE, IN, etc.): ")

url = "http://apilayer.net/api/validate?access_key=" + config.apiKey + "&number=" + number + "&country_code=" + country_code + "&format=1"

r = requests.get(url)

result = r.json()

if result["valid"] == True:
    print("\nPhonenumber is valid")
    print("\nCarrier: " + result["carrier"])
else:
    print("\nPhonenumber is not valid")