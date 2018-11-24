import requests
import re

r = requests.get("http://lauzhack.sqpub.ch/prices", stream=True)
f = open("Data.txt", "a")
f.write("\n")
f.close()
i = 0
for chunk in r.iter_content(chunk_size=1024):
    chunk = str(chunk)
    i = 0
    z = False
    for x in chunk:
        if z:
            if x == '\\':
                break
            i = i+1
        else:
            if x <= ' ':
                z = True
            i = i+1
    f = open("Data.txt", "a")
    f.write(chunk[0:i])
    f.write("\n")
    f.close()
    i = i+1

f.close()
