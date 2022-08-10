import heapq

n, m = map(int, input().split())
# 각 노드에 연결되 간선 정보를 담기 위한 연결 리스트 초기화
array = [[] for i in range(n + 1)]
# 모든 노드에 대한 진입차수는 0으로 초기화
indegree = [0] * (n + 1)

heap = []
result = []

# 방향 그래프의 모든 간선 정보를 입력받기
for _ in range(m):
    x, y = map(int, input().split())
    # 정점 A에서 B로 이동 가능
    array[x].append(y)
    # 진입 차수를 1 증가
    indegree[y] += 1

for i in range(1, n + 1):
    if indegree[i] == 0:
        heapq.heappush(heap, i)

while heap:
    data = heapq.heappop(heap)
    result.append(data)
    for y in array[data]:
        indegree[y] -= 1
        if indegree[y] == 0:
            heapq.heappush(heap, y)

for i in result:
    print(i, end=' ')