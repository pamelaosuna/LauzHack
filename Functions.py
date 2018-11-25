import requests
import re
import json
import urllib

T = 30

def findBuy(L):
        """this function finds the minumum point, which tells us
        we should buy"""
        # L: list of 30 elements
        return L.index(min(L))


def findSell(L):
    """ finds the maximum point, where we should sell"""
    return L.index(max(L))


def buyBitcoin(x):
    x = str(x)
    data = 'BUY ' + x + ' BTC jmf784hkuhkufsd'
    info = requests.post('http://lauzhack.sqpub.ch', data=data)
    print("BUYYY")


def sellBitcoin(x):
    x = str(x)
    data = 'SELL ' + x + ' BTC jmf784hkuhkufsd'
    info = requests.post('http://lauzhack.sqpub.ch', data=data)
    print("SELLL")


def streamData():
    r = requests.get("http://lauzhack.sqpub.ch/prices", stream=True)

    for chunk in r.iter_content(chunk_size=1024):
        t = 0
        for x in chunk:
            if x <= ' ':
                break
            t = t + 1
        print(chunk[t, len(chunk) - 1])


def calculate_Q():
    url = urllib.request.urlopen("http://lauzhack.sqpub.ch/teams")
    data = json.loads(url.read().decode())
    return data[4]["XBT"], data[4]["cash"]

        
def popLowest(L_L,A):
    i = A.index(min(A))
    print(i)
    L_L.pop(2*i)
    L_L.pop(2*i)
    A.pop(i)
    A.append(0)

def choose(L, L_L):
    var = float("inf")
    closest = 0
    i=0
    for i in range(int(len(L_L)/2)):
        s = 0
        for k in range(T):
            s += abs(L[k] - L_L[2*i][k])
        if (s < var):
            closest = i
            var = s
    return 2*i + 1
    
    
