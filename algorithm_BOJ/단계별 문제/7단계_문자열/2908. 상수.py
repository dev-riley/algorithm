A, B = map(int, input().split())

a = (A % 10) * 100 + ((A // 10) % 10) * 10 + A // 100
b = (B % 10) * 100 + ((B // 10) % 10) * 10 + B // 100

if a > b:
    print(a)
else:
    print(b)


##################################################
# A, B = map(str, input().split())
#
# a = a[::-1] [::-1] => 배열을 역순으로, 그래서 str로 정의
# b = b[::-1]
# print(max(int(a), int(b)))