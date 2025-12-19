def add_matrices():
    try:
        n = int(input().strip())
        
        if n < 2:
            print("Ошибка: размер матрицы должен быть больше 2")
            return
        
        matrix1 = []
        print(f"Введите {n} строк по {n} элементов для первой матрицы:")
        for _ in range(n):
            row = list(map(int, input().strip().split()))
            if len(row) != n:
                print(f"Ошибка: ожидается {n} элементов в строке")
                return
            matrix1.append(row)
        
        matrix2 = []
        print(f"Введите {n} строк по {n} элементов для второй матрицы:")
        for _ in range(n):
            row = list(map(int, input().strip().split()))
            if len(row) != n:
                print(f"Ошибка: ожидается {n} элементов в строке")
                return
            matrix2.append(row)
        
        result_matrix = []
        for i in range(n):
            result_row = []
            for j in range(n):
                result_row.append(matrix1[i][j] + matrix2[i][j])
            result_matrix.append(result_row)
        
        print('Сумма двух матриц:')
        for row in result_matrix:
            print(' '.join(map(str, row)))
            
    except ValueError:
        print("Ошибка: некорректный ввод. Ожидается число для размера матрицы и числовые элементы.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

print(add_matrices())