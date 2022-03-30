# N이 100억 이상의 큰 수가 되는 경우, 빠르게 동작하려면 N이 K의 배수가 되도록 효율적으로 한번에 빼는 방식으로 소스코드를 작성할 수 있다.
N, K = map(int, input().split())
res = 0

while True:
    target = (N // K) * K
    res += (N - target)
    N = target
    if N < K:
        break
    res += 1
    N //= K

res += (N - 1)
print(res)