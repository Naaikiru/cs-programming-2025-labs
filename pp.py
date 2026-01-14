x = int(input('введите сумму, которую хотите вложить в банк: '))
y = int(input('введите срок (в годах): '))
def deposit_profit(a, n):
    # увеличение от суммы (блоки по 10000 от 0)
    blocks = a // 10000
    increase = min(blocks * 0.003, 0.05)
    
    total = a
    for year in range(1, n + 1):
        if year <= 3:
            base = 0.03
        elif year <= 6:
            base = 0.05
        else:
            base = 0.02
        
        rate = base + increase
        total *= (1 + rate)
    
    profit = total - a
    return round(profit, 2)

# Проверка
print(deposit_profit(x, y))  