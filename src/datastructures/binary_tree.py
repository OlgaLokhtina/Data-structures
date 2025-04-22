from typing import Self


class Node[T]:
    """
    Class to creating the Node of the Tree
    ...

    Attributes
    ----------
        val : T
            the value of the node
        right : Node
            right node
        left : Node
            left node

    Methods
    -------
        add_right(val: T):
            adds the right node with a given value
        add_left(val: T):
            adds the left node with a given value
    """
    def __init__(self, val: T):
        self.val = val
        self.right: Self = None
        self.left: Self = None

    def add_right(self, val: T):
        """
        Adds the right node with a given value

        :param val: the value of the right node
        :type  val: T

        :return: None
        """
        self.right = Node(val)

    def add_left(self, val: T):
        """
        Adds the left node with a given value

        :param val: the value of the left node
        :type val: T

        :return: None
        """
        self.left = Node(val)


class Tree[T]:
    """
    Class for creating binary tree

    ...

    Attributes
    ----------
        head : Node | None
            this node is the root of the tree

    Methods
    -------
        my_gener(node: T)
            returns the generator of the object Tree
        present_tree()
            displays all nodes of the tree
        from_list(list_value: list[T])
            returns the object Tree based on values from the list
        to_list()
            returns the list of values of all nodes of the tree

    """
    def __init__(self, head: Node | None = None):
        self.head = head

    def __iter__(self):
        return self.my_gener(self.head)

    def my_gener(self, node):
        """
        Returns the generator of the object Tree

        :param node: some node of a tree
        :type node: Node

        :return: T
        """
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
        """
        Displays all nodes of the tree

        :return: None
        """
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

    @classmethod
    def from_list(cls, list_value: list[T]) -> Self:
        """
        Returns the object Tree based on values from the list

        :param list_value: list[T]
        :return: Tree
        """
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
        """
        Returns the list of values of all nodes of the tree

        :return: list[T]
        """
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

