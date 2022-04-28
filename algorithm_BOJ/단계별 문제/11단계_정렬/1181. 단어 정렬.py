import sys
n = int(input())
arr = []

for i in range(n):
    arr.append(sys.stdin.readline())
a = list(set(arr))
a.sort(key=lambda x: (len(x), x)) # 이름길이 먼저 정렬한 후, 사전 순으로 정렬
print("".join(a))
