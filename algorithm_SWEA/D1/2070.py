import sys
sys.stdin = open('2070.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N, M = input().split()

    ans = ''
    if N > M:
        ans = '>'
    elif N < M:
        ans = '<'
    else:
        ans = '='

    print('#{} {}'.format(tc, ans))