N, M, K = map(int, input().split())

data = list(map(int, input().split()))

data.sort()
first = data[N-1]
second = data[N-2]

ans = first * K * (M // K) + second * (M % K)

print(ans)