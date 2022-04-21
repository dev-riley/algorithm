import sys

# 메모리 초과
# n = int(input())
#
# array = [0] * (n + 1)
# data = []
# for i in range(n):
#     data.append(int(input()))
#     array[data[i]] += 1
#
# for i in range(len(array)):
#     for j in range(array[i]):
#         print(i)

##################################
# 수정 후
n = int(sys.stdin.readline())

array = [0 for _ in range(10001)]
data = []
for i in range(n):
    data = int(sys.stdin.readline())
    array[data] += 1

for i in range(len(array)):
    for j in range(array[i]):
        print(i)