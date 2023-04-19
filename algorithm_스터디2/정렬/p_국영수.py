import sys
input = sys.stdin.readline
n = int(input())
data = []

for i in range(n):
    name, k, e, m = input().split()
    data.append((name, k, e, m))

data.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))
for j in data:
    print(j[0])