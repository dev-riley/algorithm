def collatz(num):
    cnt = 0
    while num > 1:
        if num % 2 == 0:
            cnt += 1
            num = num // 2
            
        elif num % 2 == 1:
            cnt += 1
            num = num * 3 + 1
        if cnt > 500:
            return -1
    return cnt        

print(collatz(6))