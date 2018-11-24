import requests
import re
import json
import urlib.request

L_L = []
L = []
L_P = []
S = []
i = 0
c = 0


#read history
f = open('Data.txt')
# use readline() to read the first line 
line = f.readline()
while line:
    m = re.search('Z (.+?)\n', line)
    i = float(m.group(1))
    L.append(i)
    line = f.readline()
    if L.size == 60:
        L_L.append(L-L[0])
        L_P = choose()
        Buy = findBuy(L_P)
        Sell = findSell(L_P)
        L = []
        i=0
f.close()
print(L_H)



XBT,cash = calculate_Q()
Q = 2
r = requests.get('http://lauzhack.sqpub.ch/prices', stream=True)
for chunk in r.iter_content(chunk_size=1024):
    current = chunk
    #we get the price information:
    text = chunk.decode("utf-8")
    print(text)
    m = re.search('Z (.+?)\n', text)
    val = float(m.group(1))
    print(val)
    L.append(val)
    if i == Buy:
        buyBitcoin(Q)
        XBT,cash = calculate_Q()
        Q = (cash/10)/val
    if i == Sell:
        sellBitcoin(Q)
        XBT,cash = calculate_Q()
        Q = (cash/10)/val
    i = i+1
    if L.size == 60:
        L_L.append(L-L[0])
        L_P = choose()
        Buy = findBuy(L_P)
        Sell = findSell(L_P)
        L = []
        i=0    

        def findBuy(L):
    """this function finds the minumum point, which tells us
    we should buy"""
    #L: list of 60 elements
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
        for x in chunk:
            if x <= ' ':
                break
            t = t + 1
        print(chunk[t, len(chunk) - 1])

def calculate_Q():
    url = urllib.request.urlopen("http://lauzhack.sqpub.ch/teams")
    data = json.loads(url.read().decode())
    return data[4]["XBT"] , data[4]["cash"]

        
    
