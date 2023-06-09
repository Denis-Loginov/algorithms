from typing import List, Tuple


def moving_average(q: List[int], k: int) -> List[float]:
    result = []  # Пустой массив.
    # Первый раз вычисляем значение честно и сохраняем результат.
    current_q = sum(q[0:k])
    result.append(current_q / k)
    for i in range(0, len(q) - k):
        current_q -= q[i]
        current_q += q[i+k]
        current_avg = current_q / k
        result.append(current_avg)
    return result


def read_input() -> Tuple[List[int], int]:
    n = int(input())
    q = list(map(int, input().strip().split()))
    k = int(input())
    return n, q, k


n, q, k = read_input()
print(" ".join(map(str, moving_average(q, k))))
