import sys
sys.stdin = open('2846.txt', 'r')

for tc in range(1, 4):
    N = int(input())
    data = list(map(int, input().split()))
    result = [0] * N

    for i in range(N):
        cnt = 0
        for j in range(i+1, N):
            if data[j] > data[j-1]:
                cnt += (data[j] - data[j-1])
            else:
                break
            result[i] = cnt
    print(max(result))