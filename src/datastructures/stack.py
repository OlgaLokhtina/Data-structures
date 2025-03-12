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
        if st is None:
            self.st = []
        else:
            self.st = st

    def push(self, element: T):
        """
        Adds the element to the stack

        :param element: new element for adding to stack
        :type element: Any

        :return: None
        """
        self.st.append(element)

    def pop(self) -> T:
        """
        Removes the last element from the stack

        :return: T
        """
        if self.st:
            return self.st.pop()
        else:
            raise StackIsEmpty("Oooops!")

    def peek(self) -> T:
        """
        Returns the last element from stack

        :return: T
        """
        if self.st:
            return self.st[-1]
        else:
            raise StackIsEmpty('EMPTY')

    def val(self) -> list[T]:
        """
        Returns all the elements of the stack
        :return: list[T]
        """
        return self.st


class StackIsEmpty(Exception):
    pass



