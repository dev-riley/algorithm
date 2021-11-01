N = int(input())
cnt = 0
num = N

while True : # 특별한 일이 없는 한 계속해서 반복문을 진행하겠다는 무한반복문의 의미
    # A = (num // 10) + (num % 10)
    # B = (num % 10)*10 + (int(A) % 10)
    # cnt += 1
    # if B == N:
    #     print(cnt)
    #     break

    num_1 = num // 10
    num_2 = num % 10
    num_3 = (num_1 + num_2) % 10
    num = (num_2*10) + num_3
    cnt += 1
    if num == N:
        print(cnt)
        break