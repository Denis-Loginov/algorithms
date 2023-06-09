from typing import List

def get_weather_randomness(temperatures: List[int]) -> int:
    n = len(temperatures)
    k = 0

    if n == 1:
        return 1
    else:
        for i in range(0, n):
            if i == 0:
                if temperatures[i] > temperatures[i+1]:
                    k += 1
            if 0 < i < n-1:
                if temperatures[i] > temperatures[i+1] and temperatures[i] > temperatures[i-1]:
                    k += 1
            if i == n-1:
                if temperatures[i] > temperatures[i-1]:
                    k += 1
        return k

def read_input() -> List[int]:
    n = int(input())
    temperatures = list(map(int, input().strip().split()))
    return temperatures

temperatures = read_input()
print(get_weather_randomness(temperatures))
