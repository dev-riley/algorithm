from collections import deque

n, k = map(int, input().split())
MAX = 100001
array = [0] * MAX
check = [0] * MAX

def move(now):
    data = []
    temp = now
    for _ in range(array[now] + 1):
        data.append(temp)
        temp = check[temp]
    print(' '.join(map(str, data[::-1])))

def bfs():
    q = deque([n])
    while q:
        v = q.popleft()
        if v == k:
            print(array[v])
            move(v)
            return
        for e in (v + 1, v - 1, 2 * v):
            if 0 <= e < MAX and not array[e]:
                array[e] = array[v] + 1
                q.append(e)
                check[e] = v

bfs()

