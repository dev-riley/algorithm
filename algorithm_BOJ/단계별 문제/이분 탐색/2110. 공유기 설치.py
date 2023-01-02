import sys
input = sys.stdin.readline

n, c = map(int, input().split())
arr = [int(input()) for _ in range(n)]
arr.sort()

start, end = 1, arr[-1] - arr[0] # 시작값은 최소 거리, 끝값은 최대 거리
ans = 0

while start <= end:
    mid = (start + end) // 2
    cur = arr[0]
    cnt = 1
    for i in range(1, n):
        if arr[i] - cur >= mid:
            cnt += 1
            cur = arr[i]
    if cnt >= c:
        ans = mid
        start = mid + 1
    else:
        end = mid - 1

print(ans)