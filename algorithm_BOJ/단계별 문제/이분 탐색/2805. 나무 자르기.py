import sys
input = sys.stdin.readline

n, m = map(int, input().split())
data = list(map(int, input().split()))

start, end = 1, max(data)
res = 0
while start <= end:
    mid = (start + end) // 2
    total = 0
    for i in data:
        # 데이터 내에 모든 숫자들을 돌면서 자르고 남는 나무 길이를 더해줌
        if i >= mid:
            total += i - mid
        # 정해진 길이보다 나무가 더 짧으면 그냥 건너뜀
        else:
            continue
    
    if total >= m:
        res = mid
        start = mid + 1
    else:
        end = mid - 1

print(res)
