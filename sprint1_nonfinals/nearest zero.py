# 86918300

def nearest_zero(address):
    step = 0
    n = len(address)
    array_distance = [0] * len(address)

    for first_zero in range(0, n):
        if int(address[first_zero]) == 0:
            k = first_zero
            array_distance[first_zero] = 0
            step_back = 0
            for j in range(first_zero, 0, -1):
                step_back += 1
                array_distance[j-1] = step_back
            break
    for next_zero in range(k, n):
        if int(address[next_zero]) == 0:
            array_distance[next_zero] = 0
            step = 0
            step_back = 0
            for j in range(next_zero, k, -1):
                step_back += 1
                if array_distance[j-1] > step_back:
                    array_distance[j-1] = step_back
                else:
                    break
        else:
            step += 1
            array_distance[next_zero] = step

    list_distance = ' '.join(map(str, array_distance))
    return list_distance


def read_input():
    n = int(input())
    address = list(map(int, input().strip().split()))
    return n, address


if __name__ == '__main__':
    n, address = read_input()
    print(nearest_zero(address))
