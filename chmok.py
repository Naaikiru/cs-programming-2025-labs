vk = int(input('введите сумму, которую хотите вложить в банк: '))
sr = int(input('введите срок (в годах): '))

def vkl(x, y):
    c = 0.3
    rez = 0
    if x < 30_000:
        return ('вклад должен быть не меньше 30 000 рублей')
    
    elif y == 3:
        for i in range(y):
            c = (c*(x//10_000) + 3)/100
            if c >= 5:
                p = (8)/100
                x = (((x + x*p)*p + (x + x*p))*p +((x + x*p)*p + (x + x*p))) - x
                return (round(x, 2))
            else:
                x = (((x + x*c)*c + (x + x*c))*c +((x + x*c)*c + (x + x*c))) - x
                return (round(x, 2))
            break

    # elif 4 < y < 6:
    #     for i in range(y):
    #         c = (c*(x//10_000) + 5)/100
    #         if c >= 5:
    #             c = 5/100
                            

print(vkl(vk, sr))