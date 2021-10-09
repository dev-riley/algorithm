T = int(input())


for tc in range(T):
    numbers = list(map(int, input().split()))
    sum = 0
    for number in numbers:
        if number % 2 == 1:
            sum = sum + number
            
    
    print('#{0} {1}'.format(tc + 1, sum)) 