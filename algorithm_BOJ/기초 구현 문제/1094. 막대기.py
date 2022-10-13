n = int(input())
data = [64, 32, 16, 8, 4, 2, 1]
ans = 0

for i in data:
    if n in data:
        ans += 1
        break
    elif n > i:
        n -= i
        ans += 1
        if n == 1:
            ans += 1
            break

print(ans)