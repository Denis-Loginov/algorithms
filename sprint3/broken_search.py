# 87590210

"""
Сложность представленного алгоритма имеет логарифмическую сложность О(log)
В лучшем случае элемент, делящий массив на 2 части равен искомому. O(1)
В ином - запускается бинарный поиск со сложностью log(n), n - размер массива
В бинарном поиске на каждой итерации не более 5 операций (<= = ==)
Также есть две операции присвоения в начале.
Таким образом сложность алгоритма равна log(5n)+2
"""

from typing import Tuple, List


def broken_search(nums: list, target: int) -> int:
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1


def read_input() -> Tuple[int, List[int]]:
    _ = int(input())
    k = int(input())
    nums = list(map(int, input().split()))
    return k, nums


def main():
    k, nums = read_input()
    print(broken_search(nums, k))


if __name__ == '__main__':
    main()
