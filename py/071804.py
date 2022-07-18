import sys
n = int(sys.stdin.readline())
lst = []
for i in range(n):
    x, y = map(int, sys.stdin.readline().split())
    lst.append((y, x))
result = sorted(lst)
for y, x in result:
    print(x, y)