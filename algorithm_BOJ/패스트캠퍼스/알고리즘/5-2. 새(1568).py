#N마리의 새가 나무에 앉아있고, 자연수를 배우기 원한다. 새들은 1부터 모든 자연수를 오름차순으로 노래한다.
# 어떤 숫자 K를 노래할 때, K마리의 새가 나무에서 하늘을 향해 날아간다. 만약, 현재 나무에 앉아있는 새의 수가 지금 불러야 하는 수 보다 작을 때는, 1부터 게임을 다시 시작한다.
# 나무에 앉아 있는 새의 수 N이 주어질 때, 하나의 수를 노래하는데 1초가 걸린다고 하면, 모든 새가 날아가기까지 총 몇 초가 걸리는지 출력하는 프로그램을 작성하시오.

#-----소스코드-----
N = int(input())
index = 1
res = 0

while N != 0:
    if index > N:
        index = 1
    N -= index
    res += 1
    index += 1
print(res)

#----내 풀이(시관초과)-----
# N = int(input())
# value = N
# index = 1
# res = 0
#
# for i in range(1, N + 1):
#     if value >= index:
#         value -= index
#         index += 1
#         res += 1
#     else:
#         index = 1
# print(res)
