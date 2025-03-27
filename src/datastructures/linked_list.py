from typing import Self


class Node[T]:
    """
    Class for creating Node

    ...

    Attributes
    ----------
        val : T
            the value of the node
        prev : Node
            previous node
        next : Node
            next node

    Methods
    -------
        add_prev(val: T):
            adds the previous node with a given value
        add_next(val: T):
            adds the next node with a given value
    """
    def __init__(self, val: T | None = None):
        self.val = val
        self.prev: Self = None
        self.next: Self = None

    def add_prev(self, val: T):
        """
        Adds the previous node with a given value

        :param val: the value of the previous node
        :type val: T

        :return: None
        """
        self.prev = Node(val)

    def add_next(self, val: T):
        """
        Adds the next node with a given value

        :param val: the value of the next node
        :type val: T

        :return: None
        """
        self.next = Node(val)


class DoubleLinkedList[T]:
    """
    Class for creating double linked list

    ...

    Attributes
    ----------
        head : Node | None
            the first node of the linked list with the value value or None
        len : int
            the length of the list - the number of list nodes

    Methods
    -------
        get_first()
            returns the first node of the list
        get_last()
            returns the last node of the list
        add_first(val: T)
            adds the node to the beginning of the list
        add_last(val: T)
            adds the node to the end of the list
        pop_first()
            removes and returns the first node of the list
        pop_last()
            removes and returns the last node of the list
        present()
            returns the list of all nodes

    """
    def __init__(self, value: T | None = None):
        if value is None:
            self.head = None
            self.len = 0
        else:
            self.head = Node(value)
            self.len = 1

    def get_first(self) -> T | None:
        """
        Returns the first node of the list

        :return: T | None
        """
        if self.head:
            return self.head.val
        else:
            return None

    def get_last(self) -> T | None:
        """
        Returns the last node of the list

        :return: T | None
        """
        if self.head:
            a = self.head
            while a.next:
                a = a.next
            return a.val
        else:
            return None

    def add_first(self, val: T):
        """
        Adds the node to the beginning of the list

        :param val: the value of the added node
        :type val: T

        :return: None
        """
        if self.head is None:
            self.head = Node(val)
        else:
            b = Node(val)
            a = self.head
            self.head = b
            b.next = a
            a.prev = b
        self.len += 1

    def add_last(self, val: T):
        """
        Adds the node to the end of the list

        :param val: the value of the added node
        :type val: T

        :return: None
        """
        if self.head is None:
            self.head = Node(val)
        else:
            a = self.head
            while a.next:
                a = a.next
            a.next = Node(val)
            a.next.prev = a
        self.len += 1

    def pop_first(self) -> T:
        """
        Removes and returns the first node of the list

        :return: T
        """
        if self.head:
            r = self.head.val
            self.head = self.head.next
            self.len -= 1
            return r
        else:
            return None

    def pop_last(self) -> T:
        """
        Removes and returns the last node of the list

        :return: T
        """
        if self.head:
            a = self.head
            while a.next:
                a = a.next
            r = a.val
            if a.prev:
                a.prev.next = None
            else:
                self.head = None
            self.len -= 1
            return r
        else:
            return None

    def present(self) -> list | None:
        """
        Returns the list of all nodes

        :return: list | None
        """
        if self.head:
            s = [self.head.val]
            a = self.head
            while a.next:
                s.append(a.next.val)
                a = a.next
            return s
        else:
            return None
