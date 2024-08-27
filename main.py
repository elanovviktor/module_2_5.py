def get_matrix (n, m, value):#cоздали функцию
    matrix = []# добавили пустой список
    for i in range (n):# цикл for интерация(перебор) элементов списка n
        matrix . append([])# добавляем пустой список
        for j in range (m):#цикл уже с элементами списка m
            matrix[i].append(value)# и список value
    print(matrix)
get_matrix(2, 2,10)
get_matrix(3, 5, 42)
get_matrix(4, 2, 13)# вывод в консоль последовательно n, m, value










