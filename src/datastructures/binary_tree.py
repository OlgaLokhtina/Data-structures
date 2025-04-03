from typing import Self


class Node[T]:
    def __init__(self, val: T | None = None):
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

    def present_tree(self):
        print(self.head.val)
        aa = self.head

        def pr(a):
            if a.left:
                print(a.left.val)
                pr(a.left)
            if a.right:
                print(a.right.val)
                pr(a.right)
        pr(aa)

    @classmethod
    def from_list(cls, list_value: list[T]) -> Self:
        n = [Node(el) for el in list_value]
        tree = Tree(n[0])
        m = 0
        j = 1
        while j < len(n):
            k = m
            m = j
            for i in range(k, j):
                if n[i].val:
                    print("Node - ", n[i].val)
                    if j < len(n):
                        n[i].left = n[j]
                        print(n[j].val)
                        j += 1
                    if j < len(n):
                        n[i].right = n[j]
                        print(n[j].val)
                        j += 1
        return tree

    def to_list(self) -> list[T]:
        pass


my_list = [5, 3, 7, 3, None, 8, 1, None, None, 4, 2]
t = Tree.from_list(my_list)
print(t.present_tree())




