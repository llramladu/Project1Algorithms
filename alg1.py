#!/usr/bin/env python



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

