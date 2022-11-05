#Liczby_doskonale

num = int(input("Podaj liczbę n: "))
d = 0
flag = False
while d < num:

    if num > 1:
    # check for factors
        for i in range(2, num):
            if (num % i) == 0:
            # if factor is found, set flag to True
                flag = True
            # break out of loop
                

# check if flag is True
    if flag == False:
        print(num)
    d+=1

