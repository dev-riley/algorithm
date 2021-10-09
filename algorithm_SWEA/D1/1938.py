import sys
sys.stdin = open('1938.txt', 'r')

a, b = map(int,input().split())
# P = a + b
# M = a - b
# T = a * b
# D = a // b
# print(P, M, T, D, sep='\n')

for e in [a+b, a-b, a*b, a//b]:
    print(e)