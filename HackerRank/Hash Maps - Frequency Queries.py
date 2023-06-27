#!/bin/python3

from collections import defaultdict
import math
import os
import random
import re
import sys

# Complete the freqQuery function below.
def freqQuery(queries):
    queryDict = {}
    output = []

    for q, val in queries:
        if q == 1:
            if val in queryDict:
                queryDict[val] += 1
            else:
                queryDict[val] = 1
        elif q == 2:
            if val in queryDict and queryDict[val] > 0:
                queryDict[val] -= 1
        else:
            values = set(queryDict.values())
            output.append(1 if val in values else 0)
    return output


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)

    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()
