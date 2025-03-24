def print_matrix(n, width=1):
    matrix = [[1] * n for _ in range(n)]
    for r in range(n):
        for c in range(n):
            print(str(matrix[r][c]).ljust(width), end=' ')
        print()


print_matrix(6)
