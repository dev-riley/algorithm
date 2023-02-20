# 최단 거리 => BFS
from collections import deque
import sys
input = sys.stdin.readline

def bfs(s_a, s_b, e_a, e_b):
    q = deque()
    q.append([s_a, s_b])
    graph[s_a][s_b] = 1
    while q:
        x, y = q.popleft()
        if x == e_a and y == e_b:
            print(graph[e_a][e_b] - 1)
            return
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 > nx or nx > l or 0 > ny or ny > l:
                continue
            if 0 <= nx < l and 0 <= ny < l and graph[nx][ny] == 0:
                q.append((nx, ny))
                # 한번도 방문하지 않은 곳이라면 이동하기 전 좌표에서 +1 해준다. 이 좌표로 이동했다는 뜻.
                graph[nx][ny] = graph[x][y] + 1
T = int(input())
for tc in range(T):
    l = int(input())
    graph = [[0] * l for _ in range(l)]
    s_a, s_b = map(int, input().split())
    e_a, e_b = map(int, input().split())
    dx = [1, 2, 2, 1, -1, -2, -2, -1]
    dy = [2, 1, -1, -2, -2, -1, 1, 2]
    bfs(s_a, s_b, e_a, e_b)