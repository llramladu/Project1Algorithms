#!/usr/bin/env python


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

