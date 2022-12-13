from collections import deque
q = deque()
answer = []
n, k = map(int, input().split())
# 1 ~ n번까지 숫자 q에 넣기
for i in range(1, n + 1):
    q.append(i)
# q가 비워질 때까지
while q:
    # 1, 2번째 숫자들은 q의 맨 뒤로 보내기
    for i in range(k - 1):
        q.append(q.popleft())
    # 3번재 숫자는 answer에 추가
    answer.append(q.popleft())

print('<', end='')
for i in range(len(answer) - 1):
    print('%d, '%answer[i], end='')
print(answer[-1], end='')
print('>')
