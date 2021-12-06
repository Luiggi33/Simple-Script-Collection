import requests

postalCode = input("Postleitzahl: ")
option = input("1 für billigste Tankstelle, 2 für alle Tankstellen: ")
apiKey = "5b9253c7-e25c-8c1d-4af0-5cd954f77ffe"
url = "https://creativecommons.tankerkoenig.de/api/v4/stations/postalcode?apikey=" + apiKey + "&postalcode=" + postalCode

if postalCode == None:
    print("Please enter a postal code.")
    exit()

response = requests.get(url)
data = response.json()

if (len(data["stations"]) == 0):
    print("Error, versuche es erneut!")
    exit()

if (option == "2"):
    city = data["stations"][0]["place"]

    print("\nTankstellen in [" + postalCode + "] " + city + ":")
    for i in range(len(data["stations"])):
        print(str(i + 1) + ": " + data["stations"][i]["name"])

    input = input("\nWähle eine Tankstelle [1-" + str(len(data["stations"])) + "]: ")

    if input == None or input == "" or int(input) > len(data["stations"]):
        print("Please enter a valid number.")
        exit()

    output = data["stations"][int(input) - 1]

    print("\nTankstelle: " + output["name"])
    print("\n" + output["street"] + output["place"])
    if not output["openingTimes"]:
        print("Kann Öffnungszeiten nicht auslesen!")
    else:
        if (output["isOpen"]):
            closesAt = output["closesAt"]
            closesAt = closesAt.split("T")
            closesAt = closesAt[1].split(".")
            closesAt = closesAt[0]
            closesAt = closesAt.split(":")
            closesAt = closesAt[0] + ":" + closesAt[1]
            print("\nTankstelle ist geöffnet, Sie schließt um " + closesAt + " Uhr!")
        else:
            opensAt = output["opensAt"]
            opensAt = opensAt.split("T")
            opensAt = opensAt[1].split(".")
            opensAt = opensAt[0]
            opensAt = opensAt.split(":")
            opensAt = opensAt[0] + ":" + opensAt[1]
            print("\nTankstelle ist geschlossen, Sie öffnet um " + opensAt + " Uhr!")
    print("\n")
    for i in range(len(output["fuels"])):
        print(output["fuels"][i]["name"] + ": " + str(output["fuels"][i]["price"]) + "€")
else:
    print("\nSprit zur Auswahl: ")
    list = []
    for i in range(len(data["stations"][0]["fuels"])):
        print(data["stations"][0]["fuels"][i]["name"])
        list.append(data["stations"][0]["fuels"][i]["name"])

    fuel = input("\nWähle einen Treibstoff: ")

    if (fuel == None or fuel == "" or fuel not in list):
        print("Please enter a valid fuel.")
        exit()

    fuel = list.index(fuel)
    print("\nBilligste Tankstelle in [" + postalCode + "] " + data["stations"][0]["place"] + ":")

    cheapest = data["stations"][0]
    for i in range(len(data["stations"])):
        if data["stations"][i]["fuels"][fuel]["price"] < cheapest["fuels"][fuel]["price"]:
            cheapest = data["stations"][i]

    print("\n" + cheapest["name"] + ": " + str(cheapest["fuels"][fuel]
          ["price"]) + "€ pro Liter für " + cheapest["fuels"][fuel]["name"])
