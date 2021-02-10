mmm = [[1, 2, 3], [2, 3, 4], [3, 4, 5]]
nnn = [[10, 20, 30], [20, 30, 40], [30, 40, 50]]

def sum_matrix(selfmatrix, other):
    k = 0
    result = []
    for i in selfmatrix:
        res = []
        for j in range(len(i)):
            res.append((selfmatrix[k][j] + other[k][j]))
        k += 1
        result.append(res)
    return result


print(sum_matrix(mmm, nnn))