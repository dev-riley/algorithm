k = int(input())
data = list(map(int, input().split()))
tree = [[] for _ in range(k)]

def search(data, n):
    mid = (len(data) // 2)
    tree[n].append(data[mid])
    if len(data) == 1:
        return
    search(data[:mid], n + 1)
    search(data[mid + 1:], n + 1)

search(data, 0)
for i in range(k):
    print(*tree[i])