#!/bin/python3

from collections import defaultdict
import math
import os
import random
import re
import sys

#
# Complete the 'sherlockAndAnagrams' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def sherlockAndAnagrams(s):
    # Write your code here
    
    print(s)
    anagram = defaultdict(list)
    count = 0
    for start in range(len(s)):
        for end in range(start,len(s)):
            subString = s[start:end+1]
            print(subString)
            anagram[tuple(sorted(subString))].append(subString)
            
    print(anagram)        
    for value in anagram.values():
        if len(value) > 1:
            current = (len(value) * (len(value) - 1)) // 2
            count = count + current
            
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
