import requests

r = requests.get("http://lauzhack.sqpub.ch/prices", stream=True)
f = open("Data.txt", "a")
f.write("\n")
f.close()
i = 0
for chunk in r.iter_content(chunk_size=1024):
    f = open("Data.txt", "a")
    f.write(str(chunk))
    f.write("\n")
    f.close()
    i = i+1

f.close()
