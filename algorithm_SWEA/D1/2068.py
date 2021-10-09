import sys
sys.stdin = open('2068.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    data = list(map(int, input().split()))

    d_max = data[0]
    for i in range(len(data)):
        if d_max < data[i]:
            d_max = data[i]

    print('#{} {}'.format(tc, d_max))