n = int(input())
data = list(map(int, input().split()))

# 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [0] * 100

# 다이나믹 프로그래밍 진행(보텀업)
d[0] = data[0]
d[1] = max(data[0], data[1])
for i in range(2, n):
    d[i] = max(d[i - 1], d[i - 2] + data[i])

print(d[n-1])