m = int(input())
n = int(input())
ans = 0
lst = []
for i in range(m, n + 1):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        if i == 1:
            continue
        lst.append(i)
        ans += i
if ans == 0:
    print(-1)
else:
    print(ans)
    print(min(lst))
