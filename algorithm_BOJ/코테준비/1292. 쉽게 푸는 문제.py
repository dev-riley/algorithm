a, b = map(int, input().split())
ans = 0
lst = []
for i in range(1, 50):
    for j in range(1, i + 1):
        lst.append(i)

for j in range(a - 1, b):
    ans += lst[j]
print(ans)