def count_vowels(word):
    cnt = 0
    for i in 'aieou':
        cnt += word.count(i)
    return cnt

    
print(count_vowels('apple'))

a = [1, 2, 3, 4, 5]
b = a

a[2] = 5

print(a)
print(b)
