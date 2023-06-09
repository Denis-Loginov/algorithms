# 87460056

OPERATIONS = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: y - x,
    '*': lambda x, y: x * y,
    '/': lambda x, y: y // x
}


class Stack:

    def __init__(self):
        self.operands = []
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def push(self, item):
        self.size += 1
        self.operands.append(item)

    def pop(self):
        if self.is_empty():
            return 'error'
        self.size -= 1
        return self.operands.pop()


def main():
    stack = Stack()

    for item in input().split():
        if item.lstrip('-').isdigit():
            stack.push(int(item))
        else:
            stack.push(OPERATIONS[item](stack.pop(), stack.pop()))

    print(stack.pop())


if __name__ == '__main__':
    main()
