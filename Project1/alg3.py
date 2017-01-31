#!/usr/bin/env python


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

