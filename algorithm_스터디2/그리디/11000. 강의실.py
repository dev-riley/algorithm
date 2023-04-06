import heapq
n = int(input())
lst = []

for i in range(n):
    s, t = map(int, input().split())
    lst.append((s, t))
# 시작 시간을 기준으로 정렬
lst.sort(key=lambda x:x[0])

room = []
heapq.heappush(room, lst[0][1])
# 끝나는 시간보다 작으면 새로 방 하나 만들고
# 끝나는 시간보다 크면 먼저 빼내고, 끝나는 시간 변경후 다시 입력
for i in range(1, n):
    if lst[i][0] < room[0]:
        heapq.heappush(room, lst[i][1])
    else:
        heapq.heappop(room)
        heapq.heappush(room, lst[i][1])
    # print(room) [3, 4] => [4, 5]
print(len(room))

## 실패 코드 어떤 강의실을 계속 이어나가야할지 알 수없다.##
# ans = 1
# e = lst[0][1]
# for i in range(1, n):
#     if lst[i][0] < e:
#         ans += 1
#     else:
#         e = lst[i][1]
#     print(e)
# print(ans)

