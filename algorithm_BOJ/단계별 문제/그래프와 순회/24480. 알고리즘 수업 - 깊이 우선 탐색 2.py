import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 5) # 재귀 허용 깊이를 수동으로 늘려주는 코드

n, m , r = map(int, input().split())
# 간선 정보를 담아줄 2차원 배열 생성
graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
order = 1

def dfs(v):
    global order
    visited[v] = order
    graph[v].sort(reverse=True)
    # graph [[], [4, 2], [4, 3, 1], [4, 2], [3, 2, 1], []]
    for i in graph[v]:
        if visited[i] == 0:
            order += 1
            dfs(i)

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
# graph [[], [4, 2], [1, 3, 4], [2, 4], [1, 2, 3], []]

dfs(r)
# visited [0, 1, 4, 3, 2, 0]
for i in range(1, n + 1):
    print(visited[i])