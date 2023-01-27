import sys
input = sys.stdin.readline

n = int(input())
datas = list(map(int, input().split()))
lis = [0]

for data in datas:
    # data 값이 먼저 lis에 들어가있는 값보다 크면 append
    if lis[-1] < data:
        lis.append(data)
    # data 값이 먼저 lis에 들어가있는 값보다 작으면 data 값이 들어가기 알맞는 위치를 탐색하기 위해 이분탐색을 써준다.
    else:
        left = 0
        right = len(lis)
        while left < right:
            mid = (left + right) // 2
            if lis[mid] < data:
                left = mid + 1
            else:
                right = mid
        lis[right] = data
print(len(lis) - 1)