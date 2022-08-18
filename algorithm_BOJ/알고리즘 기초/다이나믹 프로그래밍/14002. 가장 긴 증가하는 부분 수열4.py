n = int(input())
array = list(map(int, input().split()))
dp = [1] * n

for i in range(1, n):
    for j in range(0, i):
        if array[j] < array[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp), dp)
data = []
order = max(dp)
for i in range(n - 1, -1, -1):
    if dp[i] == order:
        data.append(array[i])
        order -= 1

data.reverse()
print(*data)
