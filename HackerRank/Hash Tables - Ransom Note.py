#!/bin/python3

from collections import defaultdict
import math
import os
import random
import re
import sys

#
# Complete the 'checkMagazine' function below.
#
# The function accepts following parameters:
#  1. STRING_ARRAY magazine
#  2. STRING_ARRAY note
#

def checkMagazine(magazine, note):
    # Write your code here
    magWords = defaultdict(int)
    for w in magazine:
        magWords[w] += 1
    
    for n in note:
        if n not in magWords:
            print('No')
            return
        if magWords[n] <= 0:
            print('No')
            return
        magWords[n] -= 1
    print('Yes')
            

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    m = int(first_multiple_input[0])

    n = int(first_multiple_input[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
