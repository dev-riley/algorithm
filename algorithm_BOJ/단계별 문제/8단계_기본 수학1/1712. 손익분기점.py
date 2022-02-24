A, B, C = list(map(int, input().split()))

def ceil(n):
    if n == int(n):
        return n
    else:
        return int(n) + 1

if A / (C - B) >= 0:
    print(round(ceil(A / (C - B)) + 1))
else:
    print(-1)