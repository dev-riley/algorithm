for t in range(int(input())):
    n = int(input())
    rev_n = (bin(n)[2:])[::-1]

    for i in range(len(rev_n)):
        if rev_n[i] == '1':
            print(i, end=' ')
