# key point : 남은 일수가 가장 많은 것부터 차례대로 살펴서 그날 가장 큰 점수를 뽑아서 더한다.
import sys
input = sys.stdin.readline
n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]

data.sort()
hw_lst = []
ans = 0
day = data[n-1][0] # 남은 일수가 가장 큰 값 저장

while True:
    if day == 0:
        break
    while data and data[-1][0] >= day: # 이 날짜에 수행가능한 과제를 hw_lst에 저장
        hw_lst.append(data.pop()[1])
        # hw_lst에 값이 들어있다면
    day -= 1
    if hw_lst:
        hw_lst.sort() # 오름차순 정렬
        ans += hw_lst.pop() # 가장 큰 점수인 가장 마지막 값은 pop연산 후 ans에 더해주기
print(ans)
