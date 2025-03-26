import pytest

from datastructures.linked_list import DoubleLinkedList


@pytest.fixture()
def new_double_linked_list():
    my_dll = DoubleLinkedList(30)
    my_dll.add_last(40)
    my_dll.add_last(50)
    my_dll.add_first(20)
    my_dll.add_first(10)
    return my_dll


def test_present_dll(new_double_linked_list):
    assert new_double_linked_list.present() == [10, 20, 30, 40, 50]


def test_add_last(new_double_linked_list):
    new_double_linked_list.add_last(60)
    assert new_double_linked_list.present() == [10, 20, 30, 40, 50, 60]


def test_add_first(new_double_linked_list):
    new_double_linked_list.add_first("0")
    assert new_double_linked_list.present() == ["0", 10, 20, 30, 40, 50]


def test_get_first(new_double_linked_list):
    assert new_double_linked_list.get_first() == 10


def test_get_last(new_double_linked_list):
    assert new_double_linked_list.get_last() == 50


def test_pop_first(new_double_linked_list):
    assert new_double_linked_list.pop_first() == 10
    assert new_double_linked_list.present() == [20, 30, 40, 50]


def test_pop_last(new_double_linked_list):
    assert new_double_linked_list.pop_last() == 50
    assert new_double_linked_list.present() == [10, 20, 30, 40]