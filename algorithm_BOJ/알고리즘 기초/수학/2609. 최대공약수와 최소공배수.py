# -------시간 초과------------------
# a, b = map(int, input().split())
#
# for i in range(min(a, b), 0, -1):
#     if a % i == 0 and b % i == 0:
#         print(i)
#         break
#
# for j in range(max(a, b), (a * b) + 1):
#     if j % a == 0 and j % b == 0:
#         print(j)
#         break

# ----------------------------------
# import math
# a, b = map(int, input().split())
# print(math.gcd(a, b))
# print(math.lcm(a, b))

# ---------유클리드 호제법--------------
def GCD(a, b): # 최대공약수
    if b == 0:
        return a
    return GCD(b,a%b)
a, b = map(int, input().split())
print(GCD(a, b))
#최소공배수
print(int(a*b/GCD(a,b)))