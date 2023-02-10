import sys
from collections import deque
input = sys.stdin.readline

n, m, v = map(int, input().split())
graph = [[0] * (n + 1) for _ in range(n + 1)]
visited1 = [False] * (n + 1)
visited2 = [False] * (n + 1)

for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

def dfs(v):
    visited1[v] = True
    print(v, end=' ')
    for g in range(1, n + 1):
        if not visited1[g] and graph[v][g] == 1:
            dfs(g)

def bfs(v):
    q = deque([v])
    visited2[v] = True
    while q:
        v = q.popleft()
        print(v, end=' ')
        for b in range(1, n + 1):
            if not visited2[b] and graph[v][b] == 1:
                q.append(b)
                visited2[b] = True

dfs(v)
print()
bfs(v)