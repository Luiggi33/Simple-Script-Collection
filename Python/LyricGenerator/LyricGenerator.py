import requests
import time

cooldown = input("How many seconds between Lines? (3) ")
artist = input("Enter the name of the artist: ")
song = input("Enter the name of the song: ")

if artist == "" or song == "":
    print("Error: Artist or Song is empty.")
    exit()

if cooldown == "" or cooldown == "3" or cooldown == " ":
    cooldown = 3
else:
    cooldown = int(cooldown)

artistURL = artist.replace(" ", "%20")
songURL = song.replace(" ", "%20")

url = "https://api.lyrics.ovh/v1/" + artistURL + "/" + songURL

r = requests.get(url)

if r.status_code == 404:
    print("Error: Song not found.")
    exit()

lyrics = r.json()["lyrics"].split("\n")

print("Playing " + song + " by " + artist)
print("\n")

for i in range(3, 0, -1):
    print(i)
    time.sleep(1)

print("Go!\n")
time.sleep(1)

for i in range(0, len(lyrics), 1):
    print(lyrics[i])
    time.sleep(int(cooldown))
