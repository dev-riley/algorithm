import sys
n = int(input())

data = []
for i in range(n):
    data.append(sys.stdin.readline())

data.sort(key=lambda x: (int(x.split()[0])))
print(data) # ['20 Sunyoung\n', '21 Junkyu\n', '21 Dohyun\n']
print(''.join(data))
# for i in data:
#     print(i)