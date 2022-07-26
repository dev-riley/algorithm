# 수 N개 A1, A2, ..., AN이 주어진다. A를 오름차순 정렬했을 때, 앞에서부터 K번째 있는 수를 구하는 프로그램을 작성하시오.

# 출력
# 5 2
# 4 1 2 3 5

# 파이썬 sorted 함수 이용 => 성공
# n, k = map(int, input().split())
# array = list(map(int, input().split()))
#
# array = sorted(array)
# print(array[k - 1])

# 병합정렬 이용 => 시간초과
# def merge_sort(left, right):
#     merged = list()
#     left_point, right_point = 0, 0
#
#     while len(left) > left_point and len(right) > right_point:
#         if left[left_point] > right[right_point]:
#             merged.append(right[right_point])
#             right_point += 1
#         else:
#             merged.append(left[left_point])
#             left_point += 1
#
#     while len(left) > left_point:
#         merged.append(left[left_point])
#         left_point += 1
#
#     while len(right) > right_point:
#         merged.append(right[right_point])
#         right_point += 1
#     return merged
#
# def merge_split(array):
#     if len(array) <= 1:
#         return array
#
#     mid = len(array) // 2
#     left = merge_split(array[:mid])
#     right = merge_split(array[mid:])
#     return merge_sort(left, right)
#
# n, k = map(int, input().split())
# data = list(map(int, input().split()))
#
# result = merge_split(data)
# print(result[k - 1])

# 병합정렬 2번째 방식
def merge_sort(array):
    if len(array) <= 1:
        return array
    mid = len(array) // 2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])
    i, j, k = 0, 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
            j += 1
        k += 1
    if i == len(left):
        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1
    elif j == len(right):
        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1
    return array

n, k = map(int, input().split())
array = list(map(int, input().split()))
array = merge_sort(array)

print(array[k - 1])

