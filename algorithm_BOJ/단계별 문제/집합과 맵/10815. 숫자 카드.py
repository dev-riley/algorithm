import sys

n = int(sys.stdin.readline())
arr_n = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
arr_m = list(map(int, sys.stdin.readline().split()))

dict_ = {}
for i in range(n):
    dict_[arr_n[i]] = 0

for j in range(m):
    if arr_m[j] not in dict_:
        print(0, end=' ')
    else:
        print(1, end=' ')
