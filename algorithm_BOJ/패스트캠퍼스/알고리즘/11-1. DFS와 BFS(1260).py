from collections import deque

# 깊이 우선 탐색
def dfs(v):
    print(v, end=' ')
    visited[v] = True
    for e in adj[v]:
        if not(visited[e]):
            dfs(e)

# 너비 우선 탐색 : 한 정점의 인접한 정점들을 다 순서대로 돌아야 하기 때문에 스택으로 구현 어려움. 큐를 사용!!
def bfs(v):
    q = deque([v])
    while q:
        v = q.popleft()
        if not(visited[v]):
            visited[v] = True
            print(v, end=' ')
            for e in adj[v]:
                if not visited[e]:
                    q.append(e)

n, m, v = map(int, input().split())
adj = [[] for _ in range(n + 1)]

for _ in range(m):
    x, y = map(int, input().split())
    adj[x].append(y)
    adj[y].append(x)

# 가장 낮은 순서부터 처리하게 만들기위해 정렬
for e in adj:
    e.sort()

visited = [False] * (n + 1)
dfs(v)
print()
visited = [False] * (n + 1)
bfs(v)
