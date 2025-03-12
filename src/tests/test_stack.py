import pytest

from datastructures.stack import Stack, StackIsEmpty


@pytest.fixture()
def new_stack():
    a = Stack([1, 5, 8, 3])
    return a


@pytest.fixture()
def new_empty_stack():
    b = Stack()
    return b


def test_create_stack(new_stack):
    assert new_stack.val() == [1, 5, 8, 3]


def test_create_empty_stack(new_empty_stack):
    assert new_empty_stack.val() == []


def test_push_stack(new_stack):
    s = new_stack
    s.push(10)
    assert s.val() == [1, 5, 8, 3, 10]


def test_pop_stack(new_stack):
    s = new_stack
    assert s.pop() == 3
    assert s.val() == [1, 5, 8]


def test_pop_empty_stack(new_empty_stack):
    with pytest.raises(StackIsEmpty):
        new_empty_stack.pop()


def test_peek_stack(new_stack):
    s = new_stack
    assert s.peek() == 3


def test_peek_empty_stack(new_empty_stack):
    with pytest.raises(StackIsEmpty):
        new_empty_stack.peek()
