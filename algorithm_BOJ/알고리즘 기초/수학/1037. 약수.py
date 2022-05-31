n = int(input())
data = list(map(int, input().split()))

result = min(data) * max(data)
print(result)