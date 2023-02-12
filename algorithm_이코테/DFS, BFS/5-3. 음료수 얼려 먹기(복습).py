n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
ans = []
cnt = 0

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def dfs(x, y):
    global cnt
    visited[x][y] = True
    if graph[x][y] == 0:
        cnt += 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if graph[nx][ny] == 0 and visited[nx][ny] == False:
                dfs(nx, ny)

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0 and visited[i][j] == False:
            dfs(i, j)
            ans.append(cnt)
            cnt = 0
print(len(ans))