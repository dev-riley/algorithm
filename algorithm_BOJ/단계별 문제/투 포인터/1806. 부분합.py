import sys
input = sys.stdin.readline

n, s = map(int, input().split())
arr = list(map(int, input().split())) # 5 1 3 5 10 7 4 9 2 8

end = 0
i_sum = 0
lst = []

for start in range(n):
    while i_sum < s and end < n:
        i_sum += arr[end]
        end += 1

    # 부분 합이 s 이상인 연속된 수의 길이를 lst에 저장.
    if i_sum >= s:
        lst.append(len(arr[start:end]))

    i_sum -= arr[start]

if lst:
    print(min(lst))
else:
    print(0)