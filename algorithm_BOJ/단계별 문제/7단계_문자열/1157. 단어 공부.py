word = input().upper()
word_num=list(set(word))
cnt = []
for i in word_num:
     count = word.count(i)
     cnt.append(count)
if cnt.count(max(cnt)) >= 2:
     print('?')
else:
     print(word_num[(cnt.index(max(cnt)))])
