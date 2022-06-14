n = int(input())
# 가게에 있는 전체 부품 번호를 입력받아서 집합(set) 자료형에 기록
# 집합 자료형은 중복을 없애고 기본적으로 오름차순으로 정렬됨.
array = set(map(int, input().split()))

m = int(input())
data = list(map(int, input().split()))

for i in data:
    if i in array:
        print('yes', end=' ')
    else:
        print('no', end=' ')