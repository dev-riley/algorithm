# 처음에 작성했던 코드는 메모리 초과가 나왔다.
# 찾아보니 for문 속에서 append를 사용하는 것은 메모리 재할당이 이루어져 메모리를 효율적으로 사욯하지 못한다고 한다.
# 일반적으로 입력값이 크지않은 경우에는 상관없지만 이 문제처럼 극한으로 큰 경우에는 메모리 관리가 필요하다.

# n = int(input())
# lst = []
# for i in range(n):
#     w = int(input())
#     lst.append(w)
#
# lst.sort()
# for j in lst:
#     print(j)

############################################################
# 다음과 같이 맨 처음에 값이 0인 10001개의 리스트를 만들어주고, 입력받는 수와 동일한 인덱스에 1을 더해준다.
# 그리고 0이 아닌 리스트를 찾아 해당 인덱스를 갯수만큼 출력해주는 방식으로 푸는 문제이다.
import sys
n = int(sys.stdin.readline())

array = [0 for _ in range(10001)]
data = []
for i in range(n):
    data = int(sys.stdin.readline())
    array[data] += 1

for i in range(len(array)):
    for j in range(array[i]):
        print(i)
