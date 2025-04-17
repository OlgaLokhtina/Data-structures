import pytest

from datastructures.binary_tree import Node, Tree


@pytest.fixture()
def new_binary_tree():
    h = Node(1)
    h.add_right(2)
    h.add_left(3)
    t = Tree(h)
    return t


@pytest.fixture()
def new_list():
    lst = [5, 4, 9, 1, 4, None, 10, 6, 9, 3, None]
    return lst


@pytest.fixture()
def new_single_list():
    lst = [5]
    return lst


@pytest.fixture()
def new_empty_list():
    empty_lst = []
    return empty_lst


def test_from_list_to_list(new_list):
    tree = Tree.from_list(new_list)
    assert tree.to_list() == new_list


def test_from_single_list_to_list(new_single_list):
    tree = Tree.from_list(new_single_list)
    assert tree.to_list() == new_single_list


def test_from_empty_list_to_list(new_empty_list):
    empty_tree = Tree.from_list(new_empty_list)
    assert empty_tree.to_list() == new_empty_list


def test_tree_generator(new_list):
    tree = Tree.from_list(new_list)
    assert set(new_list) == set(tree)


def test_tree_generator_single(new_single_list):
    tree = Tree.from_list(new_single_list)
    assert set(new_single_list) == set(tree)
