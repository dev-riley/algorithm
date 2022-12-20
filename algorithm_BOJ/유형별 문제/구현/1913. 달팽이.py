n = int(input())
target = int(input())

i = [0, 1, 0, -1]
j = [1, 0, -1, 0]

# 처음 1의 위치
x, y = 0, -1

arr = [[0] * n for _ in range(n)]
arr[x][y] = 1
cnt = 2
dir = 0
num = 2
while True:
    for _ in range(cnt - 1):
        nx, ny = x + i[dir], y + j[dir]
        arr[nx][ny] = num
        num += 1

        if num == n**2 + 1:
            break
        x, y = nx, ny

    if num == n**2 + 1:
        break
    dir = (dir + 1) % 4
    if dir == 0 or dir == 2:
        cnt += 1

for i in arr:
    print(*i)
for i in range(n):
    for j in range(n):
        if arr[i][j] == target:
            print(i + 1, j + 1)