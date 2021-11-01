N = int(input())
data = list(map(int, input().split()))

#<556ms>
# max_d = min_d = data[0]
# for i in range(1, N):
#     if data[i] > max_d:
#         max_d = data[i]
#     elif data[i] < min_d:
#         min_d = data[i]
#
# print(min_d, max_d, end=' ')

# <400ms>
print(min(data), max(data), end=' ')

# <704ms> 별로군...10
# data.sort()
# print(data[0], data[-1], end=' ')