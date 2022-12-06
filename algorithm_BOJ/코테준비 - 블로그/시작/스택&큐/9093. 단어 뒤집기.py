n = int(input())
for i in range(n):
    sentence = list(map(str, input().split()))
    lst = []
    for j in range(len(sentence)):
        lst.append(sentence[j][::-1])
    print(' '.join(lst))