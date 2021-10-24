import sys # 특정값을 입력해서 종료한다는 문구가 없으니 에외처리로 무한반복문을 종료하는 코드를 만들면 됨

while True:
    try:
        A, B = map(int, sys.stdin.readline().split())
        print(A+B)
    except:
        break

