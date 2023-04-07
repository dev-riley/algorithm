import sys
input = sys.stdin.readline

a = input().strip()
b = input().strip()

while len(a) != len(b):
    if b[-1] == 'A':  # 맨 뒤의 문자가 A이면 문자만 제거하고 뒤집지 않아도 된다.
        b = b[:-1]
    else:  # 맨 뒤의 문자가 B이면 문자 제거 후 문자열을 뒤집는다.
        b = b[:-1]
        b = ''.join(reversed(b))

if a == b:
    print(1)
else:
    print(0)