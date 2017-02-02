#!/usr/bin/env python

from sys import maxint
from os import path
import numpy as np
import time


def changedp(array, value):
    coinCount = len(array)-1
    coins = [0 for x in range(coinCount+1)]
    coinUsed = [0 for x in range(value+1)]
    minCoin = [0 for x in range(value+1)]
    for x in range(value+1):
        coinCount = x
        newCoin = 1
        for j in [c for c in array if c <= x]:
            if minCoin[x-j] + 1 < coinCount:
                coinCount = minCoin[x-j]+1
                newCoin = j
            minCoin[x] = coinCount
            coinUsed[x] = newCoin
    coinLoc = value
    while coinLoc > 0:
        coinVal = coinUsed[coinLoc]
        for x in range(len(array)):
            if (array[x] == coinVal):
                coins[x]+=1
        coinLoc -= coinVal
    return minCoin[value], coins

def changegreedy(array, value):
    sum = value
    coinCount = len(array)-1
    num_Coins = 0
    coins = [0 for x in range(coinCount+1)]
    while coinCount >= 0:
        while sum >= array[coinCount]:
            sum -= array[coinCount]
            coins[coinCount]+=1
            num_Coins+=1
        coinCount-=1
    return num_Coins, coins


outFile = "Time_Results.txt"


#open output file for writing
NewFile = open(outFile, 'w')

A=[]
A.extend(range(2010,2210,10))


V = [1, 5, 10, 25, 50]

NewFile.write("slowchange:\n")
#for i in range(len(testArray)):


NewFile.write('\n')
NewFile.write("changegreedy:\n")
for i in range(len(A)):
    start = time.time()
    changegreedy(V, A[i])
    tTime = time.time() - start
    NewFile.write("%f\n" % tTime)

NewFile.write('\n')
NewFile.write("changedp:\n")
for i in range(len(A)):
    start = time.time()
    changedp(V, A[i])
    tTime = time.time() - start
    NewFile.write("%f\n" % tTime)


NewFile.close()

