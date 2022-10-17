# import string
# tmp = string.digits + string.ascii_lowercase
tmp = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# def convert(num, base):
#     q, r = divmod(num, base)
#     if q == 0:
#         return tmp[r]
#     else:
#         return convert(q, base) + tmp[r]
#
# q, r = map(int, input().split())
# print(convert(q, r))

#---------------------------------------------
n, b = map(int, input().split())
answer = ''
while n:
    answer += tmp[n % b]
    n = n // b

print(answer[::-1])