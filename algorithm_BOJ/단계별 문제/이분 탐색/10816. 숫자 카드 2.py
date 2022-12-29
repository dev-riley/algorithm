def binary_search(array, value, start, end):
    if start > end:
        return 0
    mid = (start + end) // 2
    if array[mid] == value:
        # cnt 딕셔너리에서 value라는 키를 가진 값을 가져온다. 예제에서 value가 -10이면 cnt.get(-10)은 2
        return cnt.get(value)
    elif array[mid] > value:
        return binary_search(array, value, start, mid - 1)
    else:
        return binary_search(array, value, mid + 1, end)

n = int(input())
arr_n = list(map(int, input().split()))
m = int(input())
arr_m = list(map(int, input().split()))
arr_n.sort()

# arr_n 각 요소의 개수를 cnt에 저장.
cnt = {}
for i in arr_n:
    if i in cnt:
        cnt[i] += 1
    else:
        cnt[i] = 1
# print(cnt) => {-10: 2, 2: 1, 3: 2, 6: 1, 7: 1, 10: 3}

# 찾고자 하는 값, 즉 j가 arr_n에 있으면 cnt에서 j에 해당하는 키의 값을 출력
for j in arr_m:
    print(binary_search(arr_n, j, 0, len(arr_n) - 1), end=' ')


