# 횟수 셀 때는 딕셔너리 사용하면 좋음
n = int(input())
books = {}

for _ in range(n):
    book = input()
    if book not in books:
        books[book] = 1
    else:
        books[book] += 1

target = max(books.values())
array = []

for book, number in books.items():
    if number == target:
        array.append(book)

# 가장 많은 숫자를 가진게 여러개라면 사전순으로 정렬해서 가장 앞에 것을 출력
print(sorted(array)[0])


