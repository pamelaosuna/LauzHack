import requests
import re
import json
import Functions
import urlib.request

L_L = []
L = []
L_predicted = []
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
        Functions.buyBitcoin(Q)
    if i == Sell and :
        Functions.sellBitcoin(Q)
        Q = Functions.calculate_Q()
    i = i+1
    if L.size == 60:
        L_L.append(L-L[0])
        L_P = Functions.choose(L, L_L)
        Buy = Functions.findBuy(L_P)
        Sell = Functions.findSell(L_P)
        L = []
        i=0
        
    
    print(L)
    



        
    
