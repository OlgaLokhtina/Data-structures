from typing import Self


class Node[T]:
    def __init__(self, val: T | None = None):
        self.val = val
        self.prev: Self = None
        self.next: Self = None

    def add_prev(self, val: T):
        self.prev = Node(val)

    def add_next(self, val: T):
        self.next = Node(val)


class DoubleLinkedList[T]:
    def __init__(self, value: T | None = None):
        if value is None:
            self.head = None
            self.len = 0
        else:
            self.head = Node(value)
            self.len = 1

    def get_first(self) -> T | None:
        if self.head:
            return self.head.val
        else:
            return None

    def get_last(self) -> T | None:
        if self.head:
            a = self.head
            while a.next:
                a = a.next
            return a.val
        else:
            return None

    def add_first(self, val: T):
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
        if self.head:
            r = self.head.val
            self.head = self.head.next
            self.len -= 1
            return r
        else:
            return None

    def pop_last(self) -> T:
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

    def present(self):
        if self.head:
            s = [self.head.val]
            a = self.head
            while a.next:
                s.append(a.next.val)
                a = a.next
            return s
        else:
            return None
