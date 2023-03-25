import sys
input = sys.stdin.readline

n = int(input())
data = {}

for i in range(n):
    card = int(input())
    if card in data:
        data[card] += 1
    else:
        data[card] = 1

# sorted를 이용해서 value값을 내림차순으로 정렬해주고, 같으면 key값을 오름차순으로 정렬.
res = sorted(data.items(), key=lambda x: (-x[1], x[0]))
print(res[0][0])
