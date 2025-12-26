def sm():
    try:
        n = input()
        n = int(n.strip())
        
        if n < 2:
            print("ERROR: размер матрицы должен быть больше 2")
            return
        
        m1 = []
        print(f"Введите {n} строк по {n} элементов для первой матрицы:")
        for i in range(n):
            r = list(map(int, input().strip().split()))
            if len(r) != n:
                print(f"Ошибка: ожидается {n} элементов в строке")
                return
            m1.append(r)
        
        m2 = []
        print(f"Введите {n} строк по {n} элементов для второй матрицы:")
        for i in range(n):
            r = list(map(int, input().strip().split()))
            if len(r) != n:
                print(f"Ошибка: ожидается {n} элементов в строке")
                return
            m2.append(r)
        
        rm = []
        for i in range(n):
            rr = []
            for j in range(n):
                rr.append(m1[i][j] + m2[i][j])
            rm.append(rr)
        
        print('Сумма двух матриц:')
        for row in rm:
            print(' '.join(map(str, row)))
            
    except ValueError:
        print("Ошибка: некорректный ввод. Ожидается число для размера матрицы и числовые элементы.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

print(sm())