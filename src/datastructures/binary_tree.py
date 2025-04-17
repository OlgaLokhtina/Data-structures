from typing import Self


class Node[T]:
    def __init__(self, val: T):
        self.val = val
        self.right = None
        self.left = None

    def add_right(self, val: T):
        self.right = Node(val)

    def add_left(self, val: T):
        self.left = Node(val)


class Tree[T]:
    def __init__(self, head: Node | None = None):
        self.head = head

    def __iter__(self):
        return self.my_gener(self.head)

    def my_gener(self, node):
        if node is self.head:
            yield node.val
        if node.left:
            yield node.left.val
            for p in self.my_gener(node.left):
                yield p
        if node.right:
            yield node.right.val
            for p in self.my_gener(node.right):
                yield p

    def present_tree(self):
        if self.head:
            print("Head -", self.head.val)
            aa = self.head

            def pr(a):
                if a.left:
                    print("Left -", a.left.val)
                    pr(a.left)
                if a.right:
                    print("Right -", a.right.val)
                    pr(a.right)
            pr(aa)
        print("Head -", self.head)

    @classmethod
    def from_list(cls, list_value: list[T]) -> Self:
        if list_value:
            n = [Node(el) for el in list_value]
            tree = Tree(n[0])
            m = 0
            j = 1
            while j < len(n):
                k = m
                m = j
                for i in range(k, j):
                    if n[i].val:
                        if j < len(n):
                            n[i].left = n[j]
                            j += 1
                        if j < len(n):
                            n[i].right = n[j]
                            j += 1

        else:
            tree = Tree()
        return tree

    def to_list(self) -> list[T]:
        b = [self.head]
        result = b
        while b:
            c = []
            for el in b:
                if el:
                    c.append(el.left)
                if el:
                    c.append(el.right)
            result.extend(c)
            b = c
        lst = [r.val for r in result if r]
        return lst
