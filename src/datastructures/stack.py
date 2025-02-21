class Stack:
    def __init__(self, st: list):
        self.st = st

    def push(self, element):
        self.st.append(element)

    def pop(self):
        self.st.pop()

    def peek(self):
        return self.st[-1]

    def val(self):
        return self.st


a = Stack([1, 7, 4, 9])
print(a.val())
a.push("o")
print(a.val())
print(a.peek())
a.pop()
print(a.val())
a.pop()
print(a.val())
