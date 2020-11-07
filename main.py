class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []

    def peek(self):
        return self.items[-1]

    def show(self):
        return self.items


def is_balanced(text):
    opening_brackets = ['(', '{', '[']
    closing_brackets = [')', '}', ']']
    stack = Stack()

    for char in text:
        if char in opening_brackets:
            stack.push(char)
        elif char in closing_brackets:
            if (not stack.is_empty()) and (opening_brackets.index(stack.peek()) == closing_brackets.index(char)):
                stack.pop()
            else:
                return False
    return stack.is_empty()


print(is_balanced('(((([{}]))))'))
print(is_balanced('[([])((([[[]]])))]{()}'))
print(is_balanced('{{[()]}}'))
print(is_balanced('}{}'))
print(is_balanced('{{[(])]}}'))
print(is_balanced('[[{())}]'))
