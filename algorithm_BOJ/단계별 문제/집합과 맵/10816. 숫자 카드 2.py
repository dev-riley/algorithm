import sys

n = int(sys.stdin.readline())
arr_n = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
arr_m = list(map(int, sys.stdin.readline().split()))

d = dict()
for i in arr_n:
    if i in d.keys():
        d[i] += 1
    else:
        d[i] = 1
for i in arr_m:
    if i in d.keys():
        print(d[i], end=' ')
    else:
        print(0, end=' ')