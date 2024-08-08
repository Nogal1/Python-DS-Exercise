def sum_up_diagonals(matrix):
    """Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

        >>> m1 = [
        ...     [1,   2],
        ...     [30, 40],
        ... ]
        >>> sum_up_diagonals(m1)
        73

        >>> m2 = [
        ...    [1, 2, 3],
        ...    [4, 5, 6],
        ...    [7, 8, 9],
        ... ]
        >>> sum_up_diagonals(m2)
        30
    """

    n = len(matrix)
    tl_br_sum = 0  # Top-left to bottom-right diagonal sum
    bl_tr_sum = 0  # Bottom-left to top-right diagonal sum
    
    for i in range(n):
        tl_br_sum += matrix[i][i]
        bl_tr_sum += matrix[i][n - i - 1]
    
    return tl_br_sum + bl_tr_sum