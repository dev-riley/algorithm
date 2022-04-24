import sys
from collections import Counter
n = int(sys.stdin.readline())

arr = [int(sys.stdin.readline()) for _ in range(n)]

arr.sort()
most_num = Counter(arr).most_common()

print("%.f"%(sum(arr)/n))
print(arr[(n//2)])

if len(arr) > 1:
    if most_num[0][1] == most_num[1][1]:
        print(most_num[1][0])
    else:
        print(most_num[0][0])
else:
    print(arr[0])
print(arr[-1] - arr[0])