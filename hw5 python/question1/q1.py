
def matrixtranspose(X):
    rows = len(X)
    columns = len(X[0])

    result_matrix = []
    for j in range(columns):
        row = []
        for i in range(rows):
           row.append(X[i][j])
        result_matrix.append(row)

    return result_matrix

#Check the function:
matrixtranspose([[10,8],[2,4],[1,7]])
