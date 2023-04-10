n, m = map(int, input().split())
data = [list(map(int, input())) for _ in range(n)]

cnt = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    data[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        else:
            if data[nx][ny] == 0:
                dfs(nx, ny)

for i in range(n):
    for j in range(m):
        if data[i][j] == 0:
            dfs(i, j)
            cnt += 1
print(cnt)