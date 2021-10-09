import sys
sys.stdin = open('2050.txt', 'r')

N = input()
for i in range(len(N)):
    ans = ord(N[i]) - ord('A') + 1
    print(ans, end= " ")