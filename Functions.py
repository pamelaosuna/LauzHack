import requests


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
            #chunk = float(chunk[t+1:(chunk.__len__() - 3)])
        print(chunk[t+1:(chunk.__len__() - 5)])

