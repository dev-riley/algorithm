n = int(input())  #컴퓨터 수
m = int(input()) # 연결되어 있는 컴퓨터 쌍의 수
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
cnt = 0

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(v):
    global cnt
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            cnt += 1
            dfs(i)
dfs(1)
print(cnt)