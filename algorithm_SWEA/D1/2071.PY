T = int(input())

for tc in range(T):
    num = list(map(int, input().split()))
    sum = 0
    for n in range(len(num)):
        sum = sum + num[n]
        
    avg = round(sum / len(num))
    print('#{0} {1}'.format(tc+1, avg ))