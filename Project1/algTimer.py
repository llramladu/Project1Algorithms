#!/usr/bin/env python

from sys import maxint
from os import path
import numpy as np
import time


#Iterative n^3
def enum( list ):
    max = -1000
    indexI = 0
    indexJ = 0
    sum = 0
    for i in range(len(list)):
        j = i;
        while j < len(list):
            sum = 0
            k = i;
            while k <= j:
                sum += list[k]
                if (sum > max):
                    max = sum
                    indexI = i
                    indexJ = j
                k+=1
            j+=1
    return (max, indexI, indexJ)


#Iterative n^2
def better_enum( list ):
    max = -1000
    indexI = 0
    indexJ = 0
    sum = 0
    for i in range(len(list)):
        j = i;
        sum = 0
        while j < len(list):
            sum += list[j]
            if (sum > max):
                max = sum
                indexI = i
                indexJ = j
            j+=1
    return (max, indexI, indexJ)


# help function for div-con
def maxMid(list, start, mid, end):
    sum = 0
    leftSum = -1000
    rightSum = -1000
    total = 0
    subStart = mid;
    subEnd = mid+1;
    i = mid
    #check left half
    while i >= start:
        sum += list[i]
        if (sum > leftSum):
            leftSum = sum
            subStart = i
        i-=1
    sum=0
    j=mid+1
    #check right half
    while j <= end:
        sum += list[j]
        if (sum > rightSum):
            rightSum = sum
            subEnd = j
        j+=1
    total = rightSum+leftSum
    return total, subStart, subEnd


#Divide and Conquer
def div_con( list, start, end ):
    if start > end:
        return 0, start, end
    if start == end:
        z = list[start]
        return z, start, end
    mid = (end+start)/2
    la, lb, lc = div_con(list, start, mid)
    ra, rb, rc = div_con(list,mid+1, end)
    ma, mb, mc = maxMid(list,start,mid,end)
    if (ma == max(ma, ra, la)):
        return (ma, mb, mc)
    if (ra == max(ma, ra, la)):
        return (ra, rb, rc)
    if (la == max(ma, ra, la)):
        return (la, lb, lc)


outFile = "Time_Results.txt"


#open output file for writing
NewFile = open(outFile, 'w')
#generate 2d random input
testArray = np.random.randint(low=-100, high=100, size=(10,200))

NewFile.write("Enumeration\n")
for i in range(len(testArray)):
    start = time.time()
    enum(testArray[i])
    tTime = time.time() - start
    NewFile.write("%f\n" % tTime)

NewFile.write('\n')
NewFile.write("Better Enumeration\n")
for i in range(len(testArray)):
    start = time.time()
    better_enum(testArray[i])
    tTime = time.time() - start
    NewFile.write("%f\n" % tTime)

NewFile.write('\n')
NewFile.write("Divide and Conquer\n")
for i in range(len(testArray)):
    start = time.time()
    div_con(testArray[i], 0, len(testArray[i])-1)
    tTime = time.time() - start
    NewFile.write("%f\n" % tTime)

NewFile.write('\n')
NewFile.write("Linear-Time\n")


