import pytest
my_set = {2, 4, 6, 8, 10}
my_set_2 = {'ss', 'ff'}
my_tupel = (1, 2, 3, 4, 5)
my_tupel_2 = (1, 'Igor', 24)
(id, Name, age) = my_tupel_2


def test_tupel_1():
    assert type(my_tupel) == tuple


def test_tupel_2():
    try:
        assert my_tupel[10]
    except IndexError:
        pass


@pytest.mark.parametrize(
    'element, expected', [("id", 1), ("Name", "Igor"), ("age", 24)])
def test_tupel_3(element, expected):
    assert eval(element) == expected


def test_set_1():
    assert type(my_set) == set


@pytest.mark.parametrize(
    "test_input, expected",
    [("88/8", 11), ("len((4, 5, 6, 7))", 4), ("len(my_set)", 5)])
def test_set_2(test_input, expected):
    assert eval(test_input) == expected


def test_set_3():
    assert my_set.isdisjoint(my_set_2) == True
