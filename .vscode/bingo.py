#bingo

for numer in range(1, 31):
    if numer%5 == 0 and numer%3 ==0:
        print("BINGO")
    elif numer%3 == 0:
        print("THREE")
    elif numer%5 == 0:
        print("FIVE")
    else: print(numer)
