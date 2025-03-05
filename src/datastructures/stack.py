from typing import Any


class Stack[T]:
    """
    Class for creating Stack

    ...

    Attributes
    ----------
        st : any type
            element of stack

    Methods
    -------
        push(element: Any):
            adds the element to the stack
        pop():
            removes the last element from the stack
        peek():
            returns the last element from stack
        val():
            returns all the elements of the stack
    """
    def __init__(self, st: list[T] = None):
        self.st = st

    def push(self, element: Any):
        """
        Adds the element to the stack

        :param element: new element for adding to stack
        :type element: Any

        :return: None
        """
        self.st.append(element)

    def pop(self):
        """
        Removes the last element from the stack

        :return: None
        """
        self.st.pop()

    def peek(self) -> T:
        """
        Returns the last element from stack

        :return: the last element
        """
        return self.st[-1]

    def val(self) -> list[T]:
        """
        Returns all the elements of the stack
        :return: the list of stack elements
        """
        return self.st
