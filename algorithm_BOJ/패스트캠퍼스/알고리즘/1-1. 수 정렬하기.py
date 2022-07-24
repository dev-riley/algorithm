# 이미 기본 정렬 라이브러리(sort함수) 써서 푼 문제
# ---------- 선택 정렬 알고리즘 -----------
n = int(input())
array = list()

for _ in range(n):
    array.append(int(input()))

for i in range(n):
    min_index = i
    for j in range(i + 1, n):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]

for i in array:
    print(i)