class MyQueueSized:
    def __init__(self, n):
        self.queue = [None] * n
        self.max_n = n
        self.head = 0
        self.tail = 0
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def push(self, x):
        if self.size != self.max_n:
            self.queue[self.tail] = x
            self.tail = (self.tail + 1) % self.max_n
            self.size += 1
        else:
            return 'error'

    def pop(self):
        if self.is_empty():
            return None
        x = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max_n
        self.size -= 1
        return x

    def peek(self):
        if self.is_empty():
            return None
        x = self.queue[self.head]
        return x

    # def size(self):
    #     return self.size


def main():
    c = int(input())
    n = int(input())

    queue = MyQueueSized(n)
    result = []

    for i in range(c):
        item = input().split()
        if item[0] == 'push':
            if queue.push(int(item[1])) == 'error':
                result.append('error')
        elif item[0] == 'pop':
            result.append(queue.pop())
        elif item[0] == 'peek':
            result.append(queue.peek())
        elif item[0] == 'size':
            result.append(queue.size())
    for i in result:
        print(i)


if __name__ == '__main__':
    main()
