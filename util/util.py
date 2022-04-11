import datetime, time
import test_data.coins as coins
import random

def generateNonce(nonceSeed): 
    t = datetime.datetime.now()
    return str(int(time.mktime(t.timetuple())*1000) + nonceSeed)

def pickRandomCoinPair():
    return random.choice(coins.coin_pairs)
