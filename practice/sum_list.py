def sum_list_while(numbers):
    sum = 0
    i = 0
    while i >= len(numbers):
        a = numbers[i][0] + numbers[i][1]
        sum = sum + a
        i += 1
        
    return sum

print(sum_list_while([[1,4], [10, 5], [20, 30]]))