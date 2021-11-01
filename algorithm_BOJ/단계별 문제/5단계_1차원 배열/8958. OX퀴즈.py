T = int(input())
for tc in range(1, T + 1):
    data = input()

    cnt = 0
    cnt_lst = []
    for i in range(len(data)):
        if data[i] == 'O':
            cnt += 1
        else:
            cnt = 0
        cnt_lst.append(cnt)

    print(sum(cnt_lst))