from itertools import combinations
import sys

a, b = map(int, sys.stdin.readline().split())
c = list(combinations(range(a), b))
print(len(c))