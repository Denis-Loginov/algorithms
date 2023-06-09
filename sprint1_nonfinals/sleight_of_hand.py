# 87243213


def sleight_of_hand(k, lst):
    managed = 0
    counter = [0] * 10
    for symbol in lst:
        if symbol != '.':
            counter[int(symbol)] += 1
    for num in counter:
        if 0 < num <= (k*2):
            managed += 1
    return managed


def read_input():
    k = int(input())
    lst = [i for i in range(4) for i in input()]
    return k, lst


if __name__ == '__main__':
    k, lst = read_input()
    print(sleight_of_hand(k, lst))
