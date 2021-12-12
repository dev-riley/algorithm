p = input().strip()
num = 0
if len(p) == 0:
    print(0)
# else:
#     print(p.count(' ')+1)
else:
    for i in p:
        if i == ' ':
            num += 1
    print(num + 1)