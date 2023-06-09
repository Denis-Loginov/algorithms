# 87548046

from typing import Tuple


class StackNoItemsError(Exception):
    def __init__(self):
        pass


class StackOverflowError(Exception):
    def __init__(self):
        pass


class Deck:

    def __init__(self, max_size):
        self.__queue = [None] * max_size
        self.__max_size = max_size
        self.__head = 0
        self.__tail = -1
        self.__size = 0

    def index(self, index: int, action: bool) -> int:
        if action:
            return (index + 1) % self.__max_size
        else:
            return (index - 1) % self.__max_size

    def push_front(self, item):
        if self.is_full():
            raise StackOverflowError
        self.__head = self.index(self.__head, False)
        self.__queue[self.__head] = item
        self.__size += 1

    def push_back(self, item):
        if self.is_full():
            raise StackOverflowError
        self.__tail = self.index(self.__tail, True)
        self.__queue[self.__tail] = item
        self.__size += 1

    def pop_front(self):
        if self.is_empty():
            raise StackNoItemsError
        item = self.__queue[self.__head]
        self.__head = self.index(self.__head, True)
        self.__size -= 1
        return item

    def pop_back(self):
        if self.is_empty():
            raise StackNoItemsError
        item = self.__queue[self.__tail]
        self.__tail = self.index(self.__tail, False)
        self.__size -= 1
        return item

    def is_empty(self):
        return self.__size == 0

    def is_full(self):
        return self.__size == self.__max_size


def read_inputs() -> Tuple[int, int]:
    n = int(input())
    max_size = int(input())
    return n, max_size


def main():
    n, max_size = read_inputs()
    deck = Deck(max_size)
    for i in range(n):
        try:
            item = input().split()
            print(getattr(deck, item[0])()) if len(item) == 1 else getattr(
                deck, item[0])(item[1])
        except (StackNoItemsError, StackOverflowError):
            print('error')


if __name__ == '__main__':
    main()
