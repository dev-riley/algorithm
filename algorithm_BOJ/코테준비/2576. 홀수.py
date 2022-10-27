lst = []
for _ in range(7):
    data = int(input())
    if data % 2 != 0:
        lst.append(data)

sum_ = 0
for i in lst:
    if i % 2 != 0:
        sum_ += i

if len(lst) == 0:
    print(-1)
else:
    print(sum_)
    print(min(lst))