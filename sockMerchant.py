#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    ar.sort()
    temp = ar[0]
    output_dict = {}
    output_dict[ar[0]] = 1
    for x in range(1,n):
        if temp == ar[x]:
            output_dict[ar[x]] = output_dict[ar[x]] + 1
        else:
            output_dict[ar[x]]=1
        temp = ar[x]
    total_pair = 0
    for item in output_dict:
        total_pair = total_pair + output_dict[item]//2
    return total_pair



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
