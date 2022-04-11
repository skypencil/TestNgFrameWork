import datetime, time
import test_data.coins as coins
import random

def generateNonce(): 
    t = datetime.datetime.now() 
    return str(int(time.mktime(t.timetuple())*1000))

def pickRandomCoinPair():
    return random.choice(coins.coin_pairs)
