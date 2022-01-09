####리스트 이용####
str_list = list(input())
a = [2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,7,8,8,8,9,9,9,9]
total = 0
for ch in str_list:
    idx = ord(ch) - ord('A')
    total += a[idx] + 1
print(total)