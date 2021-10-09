import sys
sys.stdin = open('2058.txt', 'r')

N = list(map(int,input()))
sum = 0
for i in range(len(N)):
    sum += N[i]
print(sum)