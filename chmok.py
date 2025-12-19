def poli():
    p = input('введите строку на проверку "является ли она полидромом": ').lower()
    p = p.replace(' ', '')

    if p == p[::-1]: return 'Да' 
    else: return 'Нет' 

print(poli())