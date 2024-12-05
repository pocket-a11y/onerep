def mg_kv(matrix):
    summ=sum(matrix[0])
    for i in range(len(matrix)):
        dl=0
        for j in range(len(matrix)):
            dl=dl+matrix[j][i]
        if dl!=summ or sum(matrix[i])!=summ:
            return False
    return True
matr = [[1, 2, 2], [2, 1, 2], [2, 2, 1]]
print(mg_kv(matr))
matr = [[1, 2, 1], [2, 1, 2], [2, 2, 1]]
print(mg_kv(matr))