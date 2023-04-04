import sys
while True:
    # rstript('\n')으로 엔터친 부분만 지워주기
    line = sys.stdin.readline().rstrip('\n')
    if not line:
        break
    l, u, n, s = 0, 0, 0, 0
    for i in line:
        if i.islower():
            l += 1
        elif i.isupper():
            u += 1
        elif i.isdigit():
            n += 1
        elif i.isspace():
            s += 1

    print(l, u, n, s)