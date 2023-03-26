n = int(input())
for i in range(n):
    stack = []
    data = input()
    for j in data:
        if j == '(':
            stack.append(j)
        if j == ')':
            if stack:
                stack.pop()
            else:
                print('NO')
                break
    else:
        if not stack:
            print('YES')
        else:
            print('NO')

# print(stack)