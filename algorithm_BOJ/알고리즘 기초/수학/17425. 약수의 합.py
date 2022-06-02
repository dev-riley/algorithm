# import sys
# n = int(sys.stdin.readline())

# 시간초과...
# for i in range(1, n + 1):
#     num = int(sys.stdin.readline())
#     sum = 0
#     for j in range(1, num + 1):
#        sum += (num // j) * j
#     print(sum)

#---------------------------------------
# 어떻게 이렇게 생각할 수 가 있지..?
import sys
ans = [0] * 1000001
tc = int(sys.stdin.readline())
for i in range(1, 1000001):
    for j in range(i, 1000001, i): #i값을 약수로 가진 인덱스들에 다 더해주기
        ans[j] += i
    ans[i] += ans[i-1] # 약수의 합이라서 앞의 값을 더해주기
for _ in range(tc):
    sys.stdout.write("{}\n".format(ans[int(sys.stdin.readline())]))
