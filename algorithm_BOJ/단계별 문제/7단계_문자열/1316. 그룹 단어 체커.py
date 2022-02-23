n = int(input())
count = n
for i in range(n):
    w = input()
    for j in range(len(w) - 1):
        if w[j] == w[j + 1]:
            pass
        elif w[j] in w[j + 1:]:
            count -= 1
            break
print(count)