import sys
sys.stdin = open('1859.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    data = list(map(int,input().split()))

    ans = 0
    max_cost = data[-1]
    for i in range(N-2, -1, -1):
        if max_cost > data[i]:
            ans += max_cost - data[i]
        else:
            max_cost = data[i]
    print('#{} {}'.format(tc, ans))
