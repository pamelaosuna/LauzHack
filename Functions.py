import json
import requests
import urllib


def findBuy(L):
    """this function finds the minumum point, which tells us
    we should buy"""
    # L: list of 60 elements
    return L.index(min(L))


def findSell(L):
    """ finds the maximum point, where we should sell"""
    return L.index(max(L))


def buyBitcoin(x):
    x = str(x)
    data = 'BUY' + x + 'BTC jmf784hkuhkufsd'
    info = requests.post('http://lauzhack.sqpub.ch', data=data)
    print(info)


def sellBitcoin(x):
    x = str(x)
    data = 'SELL' + x + 'BTC jmf784hkuhkufsd'
    info = requests.post('http://lauzhack.sqpub.ch', data=data)


def streamData():
    r = requests.get("http://lauzhack.sqpub.ch/prices", stream=True)

    for chunk in r.iter_content(chunk_size=1024):
        t = 0
        chunk = str(chunk)
        for x in chunk:
            if x <= ' ':
                break
            t = t + 1
        print(chunk[t, len(chunk) - 1])


def choose(L, L_L):
    var = float("inf")
    closest = 0
    for i in range(len(L_L)):
        s = 0
        for k in range(60):
            s += abs(L[k] - L_L[i][k])
        if (s < var):
            closest = i
    return i + 1

def calculate_Q():
    url = urllib.request.urlopen("http://lauzhack.sqpub.ch/teams")
    data = json.loads(url.read().decode())
    print(data)
