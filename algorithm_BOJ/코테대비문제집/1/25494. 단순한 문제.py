for t in range(int(input())):
    ans = 0
    x, y, z = map(int, input().split())
    for i in range(1, x + 1):
        for j in range(1, y + 1):
            for k in range(1, z + 1):
                if i % j == j % k == k % i:
                    ans += 1
    print(ans)