def lonely(num_list):

    num = []
    num.append(num_list[0])
    for i in range(1, len(num_list)-1):
        if num_list[i] != num_list[i - 1]:
            num.append(num_list[i])
            i += 1

    return num


print(lonely([1, 2, 3, 3, 0, 1, 1]))
print(lonely([4, 4, 4, 3, 3]))