import sys
sys.stdin = open('sum_input.txt', 'r')

T = int(input())
for tc in range(T):
    N,M = map(int,input().split())
    numbers = list(map(int, input().split()))

    number_list = []
    for i in range(N-1):
        num = sum(numbers[i:i+M])
        number_list.append(num)
    print(number_list)   
    max = min = number_list[0]
    for j in range(N-2):
        if max < number_list[j]:
            max = number_list[j]
        if min > number_list[j]:
            min = number_list[j]

    print('#{} {}'.format(tc+1, max-min))