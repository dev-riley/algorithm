n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

def dfs(x, y):
    # 그래프 영역을 벗어나면 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 0:
        # 해당 노드 방문 처리
        graph[x][y] == 1
        # 상, 하, 좌, 우 재귀적으로 호출, True로 바뀌지 않음, 방문 체크만 됨.
        dfs( x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False

# 모든 노드(위치)에 대하여 음료수 채우기
res = 0
for i in range(n):
    for j in range(m):
        # 현재 위치에서 DFS 수행
        # 처음 체크하는 노드가 True면 res + 1을 하고 연결되어 있는 노드는 그냥 방문 처리만 해주기 때문에 res + 1을 해주지 않음.
        if dfs(i, j) == True:
            res += 1
print(res)
