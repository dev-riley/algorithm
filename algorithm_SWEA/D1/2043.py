import sys
sys.stdin = open('2043.txt', 'r')

P, K = map(int, input().split())
cnt = 0
while K <= P:
    cnt += 1
    K += 1
print(cnt)