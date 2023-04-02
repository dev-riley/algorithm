n = input()
lst = [-1] * 26

for i in range(len(n)):
    if lst[ord(n[i]) - 97] == -1:
        lst[ord(n[i]) - 97] = i
    else:
        continue
print(*lst)