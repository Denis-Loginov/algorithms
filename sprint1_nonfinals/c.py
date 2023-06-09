from typing import List, Tuple


def get_neighbours(matrix: List[List[int]], row: int, col: int) -> List[int]:
    neighbors = []

    if row >= 1:
        up_number = matrix[row-1][col]
        neighbors.append(up_number)

    if row <= (n-2):
        down_number = matrix[row+1][col]
        neighbors.append(down_number)
    neighbors.sort()

    if col >= 1:
        left_number = matrix[row][col-1]
        neighbors.append(left_number)

    if col <= (m-2):
        right_number = matrix[row][col+1]
        neighbors.append(right_number)
    neighbors.sort()

    return neighbors


def read_input() -> Tuple[List[List[int]], int, int]:
    n = int(input())
    m = int(input())
    matrix = []
    for i in range(n):
        matrix.append(list(map(int, input().strip().split())))
    row = int(input())
    col = int(input())
    return n, m, matrix, row, col


n, m, matrix, row, col = read_input()
print(" ".join(map(str, get_neighbours(matrix, row, col))))
