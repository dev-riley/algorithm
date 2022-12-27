n = int(input())
arr = [False, False] + [True] * (n - 1)
prime_num = []
# 에라토스체네스의 체를 이용해 소수 리스트 만들기
for i in range(2, n + 1):
    if arr[i]:
        prime_num.append(i)
        # 소수 i의 배수를 다 False로 바꾸기
        for j in range(2*i, n + 1, i):
            arr[j] = False

# 투 포인터 알고리즘
answer = 0
start, end = 0, 0
while end <= len(prime_num):
    sum_ = sum(prime_num[start:end])
    if sum_ == n:
        answer += 1
        end += 1
    elif sum_ < n:
        end += 1
    else:
        start += 1

print(answer)