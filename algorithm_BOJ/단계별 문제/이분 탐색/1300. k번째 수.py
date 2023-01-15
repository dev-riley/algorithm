n = int(input())
k = int(input())
arr = []

for i in range(1, n + 1):
    arr.append(i)
arr.sort()

def binarySearch(arr, target, start, end):
    if start > end:
        return False
    mid = (start + end) // 2
    if mid > target:
        return binarySearch(arr, target, start, mid - 1)
    elif mid < target:
        return binarySearch(arr, target, mid + 1, end)
    else:
        return arr[mid]

print(binarySearch(arr, k, 0, n * n))