import sys
sys.stdin = open('2029.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    a, b = map(int,input().split())
    print('#{} {} {}'.format(tc, a//b, a%b))