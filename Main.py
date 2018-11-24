import requests
import re
import json

L_L = []
L = []
L_predicted = []
S = []
i = 0
c = 0


#read history
f = open('histo_prices.txt')
# use readline() to read the first line 
line = f.readline()
while line:
    m = re.search('Z (.+?)\n', line)
    i = float(m.group(1))
    L_H.append(i)
    line = f.readline()
f.close()
print(L_H)

TAKE_GAIN = max(L_H)
STOP_LOSS = min(L_H)


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
        buyBitcoin()
    if i == Sell and :
        sellBitcoin()
    i = i+1
    if L.size == 60:
        L_L.append(L-L[0])
        L_P = choose()
        Buy = findBuy(L_P)
        Sell = findSell(L_P)
        L = []
        i=0
        
    
    print(L)
    
import requests

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


        
    
