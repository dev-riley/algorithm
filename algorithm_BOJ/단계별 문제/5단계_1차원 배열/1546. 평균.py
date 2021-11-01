N = int(input())
data = list(map(int, input().split()))

res = 0
d_max = max(data)
for i in data:
    res += i / d_max * 100

print(res/N)