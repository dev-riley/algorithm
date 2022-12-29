import sys
input = sys.stdin.readline

n = int(input())
arr_n = list(map(int, input().split()))
m = int(input())
arr_m = list(map(int, input().split()))
arr_n.sort()

def binary_search(value, start, end):
    if start > end:
        return False
    mid = (start + end) // 2
    if arr_n[mid] > value:
        return binary_search(value, start, mid - 1)
    elif arr_n[mid] < value:
        return binary_search(value, mid + 1, end)
    else:
        return True

for i in arr_m:
    if binary_search(i, 0, n - 1):
        print(1)
    else:
        print(0)