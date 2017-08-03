#This is a process using moving average and standard deviation to test trading result along Bollinger Band

import numpy as np
import pandas as pd
import numpy.linalg as la
import datetime as dt
import pandas.io.data as web

def bbands(price, length=10, numsd=0.25):
    """ returns average, upper band, and lower band"""
    ave = pd.stats.moments.rolling_mean(price,length)
    sd = pd.stats.moments.rolling_std(price,length)
    upband = ave + (sd*numsd)
    dnband = ave - (sd*numsd)
    return np.round(ave,4), np.round(upband,4), np.round(dnband,4)
def main():
    principle = 1000000
    start, end = dt.datetime(2010, 1, 1), dt.datetime(2015, 12, 31)
    sp = web.DataReader('HP','yahoo', start, end)
    sp['ave'], sp['upper'], sp['lower'] = bbands(sp.Close, length=30, numsd=1)
    sp= sp[-1000:]
    n = 0
    for i in range(899,997):
        if sp.Close[i]<sp['lower'][i-1]:
            shares = principle/sp.Close[i+1]
            principle = shares*sp.Close[i+2]
            n=n+1
            print np.round(principle,4),n

