import sys
n, m = map(int, sys.stdin.readline().split())
# 딕셔너리가 리스트보다 메모리는 크지만 속도는 훨씬 빠르다.
s = {sys.stdin.readline().rstrip() for _ in range(n)}
ans = 0
print(s)

for j in range(m):
    word = sys.stdin.readline().strip()
    if word in s:
        ans += 1
print(ans)