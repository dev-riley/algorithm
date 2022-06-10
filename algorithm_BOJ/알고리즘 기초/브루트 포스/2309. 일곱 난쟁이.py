import sys

data = [int(sys.stdin.readline()) for _ in range(9)]
data.sort()
total = sum(data)

# print(total)
for i in range(9):
    for j in range(i + 1, 9):
        if data[i] + data[j] == total - 100:
            for k in range(9):
                if k != i and k != j:
                    print(data[k])
            exit()
