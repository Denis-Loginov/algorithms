# 87667845

"""
Сложность рекурсивного алгоритма имеет кубическую сложность О(n3)
На каждой итерации рекурсии совершаентся 3+n*(2n+4) операций
Сама рекурсия усложняет алгоритм в n раз.
Таким образом сложность алгоритма = n*(3+n*(2n+4))
"""

from typing import List


def quicksort(interns: list, lf: int, rg: int) -> int:
    if lf >= rg:
        return -1

    left, right = lf, rg
    pivot = interns[lf]

    while left <= right:
        while interns[left] < pivot:
            left += 1
        while interns[right] > pivot:
            right -= 1
        if left <= right:
            interns[left], interns[right] = interns[right], interns[left]
            left += 1
            right -= 1

    quicksort(interns, lf, right)
    quicksort(interns, left, rg)


def datasort(interns: list) -> List:
    interns[1] = -int(interns[1])
    interns[2] = int(interns[2])
    return [interns[1], interns[2], interns[0]]


def read_input() -> List:
    n = int(input())
    interns = [datasort(input().split()) for _ in range(n)]
    return interns


def main():
    interns = read_input()
    quicksort(interns, lf=0, rg=len(interns) - 1)
    for data in interns:
        print(data[2])


if __name__ == '__main__':
    main()
