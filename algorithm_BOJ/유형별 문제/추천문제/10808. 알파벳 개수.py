n = input()
lst = [0] * 26

for i in range(len(n)):
    lst[ord(n[i]) - 97] += 1

print(*lst)