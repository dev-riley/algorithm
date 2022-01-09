####index 이용####
li = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
word = input()
res = 0
for i in range(len(word)):
    for j in li:
        if word[i] in j:
            res += li.index(j) + 3
print(res)