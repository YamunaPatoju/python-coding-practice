def rotate90(mat):
    n = len(mat)
    res = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            res[j][n - i - 1] = mat[i][j]
    for i in range(n):
        for j in range(n):
            mat[i][j] = res[i][j]
mat = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]
rotate90(mat)
for row in mat:
    print(" ".join(map(str, row)))
