scores = [(90, 80), (85, 75), (90, 100)]

# for tc in range(1, len(scores) + 1):
sum = avg = tc = 0
for score in scores:
    sum = score[0] + score[1]
    avg = sum / len(score)
    tc += 1
    print('{}번 학생의 총점은 {}점이고, 평균은 {}입니다.'.format(tc, sum, avg))