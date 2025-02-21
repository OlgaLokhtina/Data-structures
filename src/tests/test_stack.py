from datastructures.stack import Stack


def test_stack():
    s = Stack([1, 5, 8, 3])
    s.push(10)
    assert (s.val()) == [1, 5, 8, 3, 10]
    s.pop()
    assert (s.val()) == [1, 5, 8, 3]
