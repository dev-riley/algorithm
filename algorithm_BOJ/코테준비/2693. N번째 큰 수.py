for tc in range(int(input())):
    data = list(map(int, input().split()))
    data.sort(reverse=True)
    print(data[2])