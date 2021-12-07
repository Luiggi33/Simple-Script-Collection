import requests
import time

artist = input("Enter the name of the artist: ")
song = input("Enter the name of the song: ")

artist = artist.replace(" ", "%20")
song = song.replace(" ", "%20")

url = "https://api.lyrics.ovh/v1/" + artist + "/" + song

r = requests.get(url)

lyrics = r.json()["lyrics"].split("\n")

for i in range(0, len(lyrics), 1):
    print(lyrics[i])
    time.sleep(3)