#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    count_sam_apple = 0
    for apple in apples :
        pos = a + apple
        if  pos >= s and pos <= t:
            count_sam_apple = count_sam_apple + 1
    count_sam_oranges = 0
    for orange in oranges : 
        pos = b + orange
        if pos >= s and pos <= t:
            count_sam_oranges = count_sam_oranges + 1
    print(count_sam_apple)
    print(count_sam_oranges)

if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
