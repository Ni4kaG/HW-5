import numpy as np
import math
#import pytest
def func_for_filter(iterable_elem):
    """
    функция - первый параметр для filter
    будем фильтровать только нечетные числа
    :param iterable_elem: проверяемый элемент
    :return: нечетный - True, четный - False
    """
    return int(iterable_elem)%2 == 1

def test_func_for_filter():
    """
    тест для функции func_for_filter
    :return: должна веринуть истину для нечетного числа
    """

    assert func_for_filter(2*np.random.randint(2,777) + 1)

def func_for_map(iterable_elem):
    """
    функция - первый параметр для map
    будем фильтровать только нечетные числа
    :param iterable_elem: проверяемый элемент
    :return: удвоение func_for_map
    """
    return iterable_elem * 2

def test_func_for_map():
    """
    тест для функции func_for_map
    :return: должна веринуть истину для удвоенного числа, или дважды повторенной строки
    """

    a = np.random.randint(2,777)
    assert func_for_map(a) == 2*a
    assert func_for_map('a') == 'aa'

def test_func_filter():
    """
    функция тестирования встроенной функции filter
    :return: статус прохождения теста
    """

    list_to_filter = []
    list_to_filter = np.random.randint(1,777,11)
    filtered_obj = filter(func_for_filter, list_to_filter)
    filtered_list = list(filtered_obj)
    a = np.random.randint(0, len(filtered_list))

    assert str(type(filtered_obj))=="<class 'filter'>"
    assert filtered_list[a]%2
    assert len(filtered_list) <= len(list_to_filter)
    assert func_for_filter(sum(filtered_list)) == func_for_filter(len(filtered_list))


def test_func_map():
    """
    функция тестирования встроенной функции map
    :return: статус прохождения теста
    """

    list_to_map = []
    list_to_map = [*np.random.randint(1,1000,8),*['Ni4ka', "Leo", 'Max'], *np.random.randint(1,1000,3)]
    mapped_obj = map(func_for_map, list_to_map)
    mapped_list = list(mapped_obj)
    a = np.random.randint(0, len(mapped_list))

    assert str(type(mapped_obj))=="<class 'map'>"
    assert mapped_list[a] == func_for_map(list_to_map[a])
    assert len(mapped_list) == len(list_to_map)

def test_func_sort():
    """
    функция тестирования встроенной функции sort
    :return: статус прохождения теста
    """

    dict_to_sort = {2: 'red', 1: 'green', 3: 'blue'}
 #   rev_param = np.random.choice([False, True])
    rev_param = (np.random.randint(0, 10) < np.random.randint(0, 10))
    sorted_obj_key = sorted(dict_to_sort, reverse = rev_param)
    sorted_obj_vol = sorted(dict_to_sort.values(), reverse = rev_param)
    a = len(sorted_obj_key) - 1
    b = len(sorted_obj_vol) - 1
    assert isinstance(sorted_obj_key, list)
    assert (sorted_obj_key[a-1] > sorted_obj_key[a]) == rev_param
    assert a == b
    alphabet = ['a', 'b', 'c', 'g', 'p', 'q', 'r']
    assert (alphabet.index(sorted_obj_vol[a-1][0]) > alphabet.index(sorted_obj_vol[a][0])) == rev_param


def test_pi():
    """
    функция тестирования встроенной функции pi
    :return: статус прохождения теста
    """
    p = math.pi
    assert p == 3.141592653589793

def test_sqrt():
    """
    функция тестирования встроенной функции sqrt
    :return: статус прохождения теста
    """
    a = np.random.randint(0,100)
    assert a - math.sqrt(a)**2 < 1.0e-14

def test_pow():
    """
    функция тестирования встроенной функции pow
    :return: статус прохождения теста
    """
    base = np.random.random(1)*10000
    exp = -1
    a = math.pow(base, exp)
    assert abs(a - 1/base)< 1.0e-14

def test_hypot():
    """
    функция тестирования встроенной функции hypot
    :return: статус прохождения теста
    """
    x = np.random.random(1) * 10000 * np.random.choice([-1, 1])
    y = np.random.random(1) * 10000 * np.random.choice([-1, 1])
    z = math.hypot(x,y)
    assert abs(math.sqrt(x**2 + y**2) - z) <  1.0e-14


if __name__ == "__main__":

    print(str(type(filter(func_for_filter, [])))=="<class 'filter'>")
    rev_p = np.random.choice([False, True])
    print(rev_p, type(rev_p))
    p = math.pi
    print(p)
    print(math.sqrt(48))
    print(48 - math.sqrt(48)**2 < 1.0e-14)
    print(np.random.random(1))

    base = np.random.random(1)*10000
    exp = -1
    a = math.pow(base, exp)
    print(abs(a - 1/base)< 1.0e-14)

    x = np.random.random(1) * 10000 * np.random.choice([-1, 1])
    y = np.random.random(1) * 10000 * np.random.choice([-1, 1])
    z = math.hypot(x,y)
    print(abs(math.sqrt(x**2 + y**2) - z))
