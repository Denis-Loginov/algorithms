class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]


def main():
    bracket = list(input())
    bracket_seq = {
        '(': ')',
        '{': '}',
        '[': ']'
    }
    stack = Stack()
    for i in bracket:
        if i in bracket_seq.keys():
            stack.push(i)
        elif not stack.is_empty() and bracket_seq[stack.peek()] == i:
            stack.pop()
        else:
            stack.push(i)
            break
    if stack.is_empty():
        print('True')
    else:
        print('False')


if __name__ == '__main__':
    main()