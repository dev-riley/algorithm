# 최단 경로는 bfs -> bfs는 queue를 이용
from collections import deque
n, m = map(int, input().split())
data = [list(map(int, input())) for _ in range(n)]

visited = [[0] * m for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    q = deque()
    q.append((0, 0))
    while q:
        x, y = q.popleft()
        # 탐색노드의 4가지 인접 노드 모두 탐색
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            else:
                if data[nx][ny] == 1:
                    data[nx][ny] = data[x][y] + 1
                    q.append((nx, ny))
    return data[n-1][m-1]
print(bfs())