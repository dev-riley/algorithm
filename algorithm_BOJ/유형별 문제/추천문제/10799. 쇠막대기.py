n = input()
stack = []
ans = 0

for i in range(len(n)):
    # 열린 괄호는 추가
    if n[i] == '(':
        stack.append('(')
    else: # 닫힌 괄호의 경우
        stack.pop()
        if n[i-1] == '(': # 레이저인 경우
            ans += len(stack)
        else: # 막대의 끝인 경우
            ans += 1

print(ans)