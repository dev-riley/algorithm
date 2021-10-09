import sys
sys.stdin = open('1926.txt', 'r')

N = int(input())
for i in range(1, N+1):
    cnt = 0
    # 그냥 있으면 cnt를 하나 추가하는 건데 내가 필요한 건 3, 6, 9가 있을 때마다 cnt += 1 해주는 거다. 어떻게 해야할까??
    if (i % 10) == 3 or (i % 10) == 6 or (i % 10) == 9:
        cnt += 1
    if (i // 10) != 0 and (i // 10) % 3 == 0:
        cnt += 1

    if cnt >= 1:
        i = '-' * cnt
    print(i, end=' ')
