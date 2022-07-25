TC = int(input())

for tc in range(TC):
    n = int(input())
    data = [0] * 101
    data[1] = 1
    data[2] = 1
    data[3] = 1

    for i in range(4, 101):
        data[i] = data[i - 2] + data[i - 3]

    print(data[n])