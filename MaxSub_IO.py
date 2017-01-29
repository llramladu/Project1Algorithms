#!/usr/bin/env python

from sys import maxint
from os import path
import time
import os


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


def maxSubArraySum(a,size):
    max_subArray = -maxint - 1
        #sets starting max to smallest possible number
    max_suffix = 0 #smallest end is set to 0 so it will be the first element of the array and then the largest subarray
    start = 0
    end = 0
    for i in range(0,size):
        max_suffix = max_suffix + a[i]
        if(max_subArray < max_suffix): #if the suffix is larger then the subarray it becomes the subarray
            max_subArray = max_suffix
            end = i
        
        if (max_suffix < 0): #if the suffix becomes less than 0 it resets to being 0 so when the loop continues we will get the largest subarray
            max_suffix = 0
            start = i+1
    if (start > end):
        start = 0
    return max_subArray, start, end


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

if(path.isfile(outFile)):
    os.remove(outFile)

NewFile = open(outFile, 'w')


#loop through testArray Writing data into output file
for i in range(len(testArray)):
    aCount = i+1
    NewFile.write("Array %d\n" % aCount)
    for x in range(len(testArray[i])):
        NewFile.write("%d " % testArray[i][x])
    NewFile.write('\n')
    NewFile.write('\n')
    NewFile.write("Enumeration\n")
    total, start, end = enum(testArray[i])
    k = start
    while k <= end:
        NewFile.write("%d " % testArray[i][k])
        k+=1
    NewFile.write('\n')
    NewFile.write("Total: %d\n" % total)
    NewFile.write('\n')
    NewFile.write("Better Enumeration\n")
    total, start, end = better_enum(testArray[i])
    k = start
    while k <= end:
        NewFile.write("%d " % testArray[i][k])
        k+=1
    NewFile.write('\n')
    NewFile.write("Total: %d\n" % total)
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
    total, start, end = maxSubArraySum(testArray[i], len(testArray[i]))
    k = start
    while k <= end:
        NewFile.write("%d " % testArray[i][k])
        k+=1
    NewFile.write('\n')
    NewFile.write("Total: %d\n" % total)
    NewFile.write('\n')
    NewFile.write('\n')

NewFile.close()

