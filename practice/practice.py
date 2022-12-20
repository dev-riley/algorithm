s = input()

answer = True
check = []
for i in s:
    check.append(i)
    if i == ')' and '(' in check:
        check.pop()
        check.pop('(')

if not check:
    answer = False

print(answer)