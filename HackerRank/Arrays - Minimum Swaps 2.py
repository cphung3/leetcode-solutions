#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    visited = [False] * len(arr)
    correct = { i: arr[i-1] for i in range(1, len(arr)+1)}
    swaps = 0

    # [3, 1, 2, 4]

    for i in range(1, len(arr)+1):
        if visited[i-1]:
            continue
        cor = arr[i-1]
        while cor != i:
            cor = correct[cor]
            swaps += 1
            visited[cor-1] = True
    return swaps//2


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
