import sys
n, m = map(int,sys.stdin.readline().split())

# ----------시간 초과----------
# for num in range(m, n + 1):
#     for i in range(2, num + 1):
#         if num % i == 0:
#             if i != num:
#                 break
#             else:
#                 print(num)

# ------에라토스테네스의 체(메모리 초과)--------

# check = [0] * (m + 1)
# res = []
# for i in range(n, m + 1):
#     for j in range(2, n + 1):
#         if check[j] == 0:
#             if j >= m:
#                 print(j)
#             for k in range(i*2, n + 1, i):
#                 if check[k] == 0:
#                     check[k] = 1
#     for j in range(2, n + 1):
#         if check[j] == 0:
#             res.append(j)

# ------에라토스테네스의 체--------
def isPrime(x):
    if x == 1:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

# for i in range(n, m + 1):
#     if i == 1:
#         break
#     for j in range(2, int(i ** 0.5) + 1):
#         if i % j == 0:
#             break
#     else:
#         print(i)
for i in range(n, m + 1):
    if isPrime(i):
        print(i)