d_list = []
for i in range(1, 9):
    data = (input())
    d_list.append(int(data))

print(max(d_list))
print(d_list.index(max(d_list)) + 1)

