def matrixPrint(matrix, size: int) -> None:
    for i in range(size):
        for j in range(size):
            print("%7.d" % matrix[i][j], end=' ')
        print("\n\n")


n = int(input("Enter a size of the matrix \n"))
arr = [[0] * n for i in range(n)]
elem_cnt = 1
row_cnt = 0
column_cnt = 0
arr[n // 2][n // 2] = n ** 2

for v in range(n // 2):
    for i in range(n - column_cnt * 2):
        arr[column_cnt][i + row_cnt] = elem_cnt
        elem_cnt += 1
    row_cnt += 1

    for i in range(n - row_cnt - column_cnt):
        arr[i + row_cnt][n - 1 - column_cnt] = elem_cnt
        elem_cnt += 1
    column_cnt += 1

    for i in range(column_cnt, n - column_cnt + 1):
        arr[-column_cnt][-i - 1] = elem_cnt
        elem_cnt += 1

    for i in range(row_cnt, n - row_cnt):
        arr[-i - 1][row_cnt - 1] = elem_cnt
        elem_cnt += 1

matrixPrint(arr, n)
