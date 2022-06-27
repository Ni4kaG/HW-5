def test_func_filter():
    """
    функция тестирования встроенной функции filter
    :return: статус прохождения теста
    """
    import numpy as np
    list_to_filter = np.random.randint(1,1000,11)
    filtered_obj = filter(lambda odd: odd%2, list_to_filter)
    list_filtered_obj = list(filtered_obj)
    assert str(type(filtered_obj))=="<class 'filter'>"
    assert list(filtered_obj)[int(len(list_filtered_obj)/2)]%2
#    return filtered_obj

# if __name__ == "__main__":
#     print(list(test_func_filter()))
#     print(type(test_func_filter()))
#     print(str(type(test_func_filter()))=="<class 'filter'>")