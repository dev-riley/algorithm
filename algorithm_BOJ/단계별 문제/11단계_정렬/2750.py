# 너무 느림
n = int(input())

array = []
for i in range(n):
    array.append(int(input()))

array = sorted(array)
for i in range(len(array)):
    print(array[i])

