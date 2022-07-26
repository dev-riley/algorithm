# -----이미 푼 문제(파이썬 sort함수 사용)-----
# 병합정렬 이용
def merge_sort(array):
    if len(array) <= 1:
        return array
    mid = len(array) // 2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])
    # i는 왼쪽 point, j는 오른쪽 point, k는 array point
    i, j, k = 0, 0, 0
    # case 1. left, right 둘다 남아있을 때
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
            j += 1
        k += 1
    # case 2. 오른쪽만 남아있을 때
    if i == len(left):
        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1
    # case 3. 왼쪽만 남아있을 때
    elif j == len(right):
        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1
    return array

n = int(input())
array = []

for _ in range(n):
    array.append(int(input()))

array = merge_sort(array)

for data in array:
    print(data)
