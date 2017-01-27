#!/usr/bin/env python

from sys import maxint
from os import path;
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


importFile = "MSS_TestProblems.txt"
outFile = "MSS_Results.txt"

#open test problem file and import into testArray
if (path.isfile(importFile)):
    testFile = open(importFile, 'r')
    testArray = []
    for line in testFile:
        newLine = line.rstrip('\n')
        newLine = newLine.rstrip('\r')
        newLine = newLine.split()
        x = len(newLine)
        i = 0
        while i < x:
            newLine[i] = int(newLine[i])
            i+=1
        testArray.append(newLine)
    
    testFile.close()

#open output file for writing
NewFile = open(outFile, 'w')


#loop through testArray Writing data into output file
for i in range(len(testArray)):
    aCount = i+1
    NewFile.write("Array %d\n" % aCount)
    for x in range(len(testArray[i])):
        NewFile.write("%d " % testArray[i][x])
    NewFile.write('\n')
    print "Enumeration"
    NewFile.write('\n')
    NewFile.write("Enumeration\n")
    total, start, end = enum(testArray[i])
    k = start
    while k <= end:
        NewFile.write("%d " % testArray[i][k])
        k+=1
    NewFile.write('\n')
    NewFile.write("Total: %d\n" % total)
    print "Better Enumeration"
    NewFile.write('\n')
    NewFile.write("Better Enumeration\n")
    total, start, end = better_enum(testArray[i])
    k = start
    while k <= end:
        NewFile.write("%d " % testArray[i][k])
        k+=1
    NewFile.write('\n')
    NewFile.write("Total: %d\n" % total)
    print "Divide and Conquer"
    NewFile.write('\n')
    NewFile.write("Divide and Conquer\n")
    total, start, end = div_con(testArray[i], 0, len(testArray[i])-1)
    k = start
    while k <= end:
        NewFile.write("%d " % testArray[i][k])
        k+=1
    NewFile.write('\n')
    NewFile.write("Total: %d\n" % total)
    NewFile.write('\n')
    NewFile.write("Linear-Time\n")
#linear time goes here
    NewFile.write('\n')
    NewFile.write('\n')

NewFile.close()

