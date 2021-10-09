def tax(won):
    if won <= 1200:
        return won * 0.06
    elif 1200 < won <= 4600:
        return 1200 * 0.06 + (won - 1200) * 0.15
    elif 4600< won <= 8800:
        return 1200 * 0.06 + 3400 * 0.15 + (won - 4600) * 0.24

