money = int(input())
data = list(map(int, input().split()))
JH_money, SM_money = money, money
JH, SM = 0, 0

for i in data:
    if i <= money and money != 0:
        JH += JH_money // i
        JH_money %= i

for i in range(len(data) - 3):
    # 3일 연속 하락
    if data[i] > data[i + 1] > data[i + 2]:
        SM += SM_money // data[i + 3]
        SM_money %= data[i + 3]
    # 3일 연속 상승
    elif data[i] < data[i + 1] < data[i + 2]:
        SM_money += SM * data[i + 3]
        SM = 0

JH_asset = [JH_money + (data[-1] * JH)]
SM_asset = [SM_money + (data[-1]) * SM]

if JH_asset > SM_asset:
    print('BNP')
elif JH_asset < SM_asset:
    print('TIMING')
else:
    print('SAMESAME')