import sys
sys.stdin = open('2063.txt', 'r')

N = int(input())
data = list(map(int, input().split()))
data.sort()

mid = N // 2
ans = data[mid]
print(ans)