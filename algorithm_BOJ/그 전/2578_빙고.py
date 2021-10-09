import sys
sys.stdin = open('2578.txt', 'r')

bingo = [list(map(int, input().split())) for _ in range(5)]
n_order = [list(map(int, input().split())) for _ in range(5)]

cnt = 0
