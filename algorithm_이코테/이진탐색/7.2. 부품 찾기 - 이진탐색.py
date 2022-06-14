# 이진탐색 코드 함수
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return None

n = int(input())
array = list(map(int, input().split()))
array.sort()

m = int(input())
data = list(map(int, input().split()))

for i in data:
    result = binary_search(array, i , 0, n - 1)
    if result != None:
        print('yes', end=' ')
    else:
        print('no', end=' ')
