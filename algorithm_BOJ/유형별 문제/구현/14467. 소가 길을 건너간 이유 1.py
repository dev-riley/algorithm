n = int(input())
cow = [-1] * 11
cnt = 0

for _ in range(n):
    cow_num, cow_move = map(int, input().split())

    if cow[cow_num] == -1:
        cow[cow_num] = cow_move
    else:
        if cow[cow_num] != cow_move:
            cnt += 1
            cow[cow_num] = cow_move

print(cnt)