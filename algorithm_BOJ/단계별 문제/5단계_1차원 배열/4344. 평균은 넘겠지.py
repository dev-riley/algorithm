import sys; sys.stdin = open('4344.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    data = list(map(int,input().split()))
    N = data[0]

    sumV = 0
    for i in range(1, N+1):
        sumV += data[i]

    avgV = sumV / N
    cnt = 0
    for j in range(1, N + 1):
        if data[j] > avgV:
            cnt += 1
    res = (cnt / N)*100
    print("{0:0.3f}%".format(res))