import math

def fee(minute, distance):
    rental = math.ceil(minute / 10) * 1200
    insurance = math.ceil(minute / 30) * 525

    if distance <= 100:
        distance_fee = distance * 170
    elif distance > 100:
        distance_fee = 100 * 170 + (distance - 100) * 85

    sum = rental + insurance + distance_fee
    return sum

print(fee(600, 50))
print(fee(600, 110))