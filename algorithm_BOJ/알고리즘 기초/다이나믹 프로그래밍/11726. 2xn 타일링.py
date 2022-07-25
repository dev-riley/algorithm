# def tiling(n):
#     num_list = [0 for i in range(n + 1)]
#     num_list[1] = 1
#     num_list[2] = 2
#
#     if n > 2:
#         for i in range(3, n + 1):
#             num_list[i] = num_list[i - 1] + num_list[i - 2]
#     return num_list[n]
#
#
# n = int(input())
# print(tiling(n))

#-------------------------------------------------
n = int(input())
dp = [0] * 1001
dp[1] = 1
dp[2] = 2

for i in range(3, 1001):
    dp[i] = dp[i - 1] + dp[i - 2]

print(dp[n] % 10007)

