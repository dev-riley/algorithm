croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
c = input()
for i in croatia:
    c = c.replace(i, 'a')
print(len(c))