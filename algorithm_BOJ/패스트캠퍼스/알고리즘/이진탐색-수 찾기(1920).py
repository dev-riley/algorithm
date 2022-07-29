N = int(input())
N_list = list(map(int, input().split()))
M = int(input())
M_list = list(map(int, input().split()))
N_list.sort()

def binary_search(value, start, end):
    if start > end:
        return False
    median = (start + end) // 2
    if N_list[median] > value:
        return binary_search(value, start, median - 1)
    elif N_list[median] < value:
        return binary_search(value, median + 1, end)
    else:
        return True

for item in M_list:
    if binary_search(item, 0, N - 1):
        print(1)
    else:
        print(0)

#------set자료형으로 풀어보기(더 간단)------
n = int(input())
array = set(map(int, input().split()))
m = int(input())
x = list(map(int, input().split()))

for i in x:
    if i not in array:
        print('0')
    else:
        print('1')