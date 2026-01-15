a = float(input('Вклад в банке в размере: '))
n = float(input('Срок: '))
deprate = 0
deprate3 = 3
deprate46 = 5
deprate6 = 2
profit = 0
every10deprate = 0

if a < 30000: print('Минимальный вклад - 30 000 рублей!')

elif a >= 30000:
    every10deprate += ((a+profit)//10000) * 0.3
    if every10deprate <= 5: deprate += ((a+profit)//10000) * 0.3
    elif every10deprate >= 5: deprate += 5

    if n <= 3:
        for i in range(int(n)):
            anew = a + profit
            profit += anew*(deprate3+deprate)/100

    elif n >= 4 and n <= 6:
        for i in range(3):
            anew = a + profit
            profit += anew*(deprate3+deprate)/100
        for i in range(int(n)-3):
            anew = a + profit
            profit += anew*(deprate46+deprate)/100
    
    elif n > 6:
        for i in range(3):
            anew = a + profit
            profit += anew*(deprate3+deprate)/100
        for i in range(3):
            anew = a + profit
            profit += anew*(deprate46+deprate)/100
        for i in range(int(n)-6):
            anew = a + profit
            profit += anew*(deprate6+deprate)/100

print(round(profit, 2))