#!/usr/bin/env python

from sys import maxint
import time
maxSubArray = [31, -41, 59, 26, -53, 58, 97, -93, -23, 84]

def maxSubArraySum(a,size):
	max_subArray = -maxint - 1
	#sets starting max to smallest possible number
	max_suffix = 0 #smallest end is set to 0 so it will be the first element of the array and then the largest subarray

	for i in range(0,size):
		max_suffix = max_suffix + a[i]
		if(max_subArray < max_suffix): #if the suffix is larger then the subarray it becomes the subarray
			max_subArray = max_suffix

		if (max_suffix < 0): #if the suffix becomes less than 0 it resets to being 0 so when the loop continues we will get the largest subarray
			max_suffix = 0

	return max_subArray

start = time.time()
maxSum = maxSubArraySum(maxSubArray, 10)
tTime = time.time() - start
print maxSum
print tTime
