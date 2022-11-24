n = input()
lst = []
for i in n:
    lst.append(int(i))
ans = lst[0]
for i in range(1, len(lst)):
    if ans <= 1 or lst[i] <= 1:
        ans += lst[i]
    else:
        ans *= lst[i]

print(ans)