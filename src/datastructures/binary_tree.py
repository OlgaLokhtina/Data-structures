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
        def create_tree(i):
            if i < len(list_value):
                h = Node(list_value[i])
                if i*2+1 < len(list_value):
                    h.left = create_tree(i*2+1)
                if i*2+2 < len(list_value):
                    h.right = create_tree(i*2+2)
                return h
        head = create_tree(0)
        a = Tree(head)
        return a

    def to_list(self) -> list[T]:
        l[0] = self.head.val

        def tran(i=0, d=self.head):
            l[i*2+1] = d.left.val
            l[i*2+2] = d.right.val
            tran(i*2+1, d.left)
            tran(i*2+2, d.right)
        return l


l = [1, 2, 3, 4, None, 5, 6, None, 7]
t = Tree.from_list(l)
p = t.to_list()
print(p)
