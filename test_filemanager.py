# 1. встроенные модули
import random
import numpy as np
import os
import sys
import shutil
# 2. наши модули
from Lesson5modules.my_function_prev_lessons import *

def test_for_refill():
    """
    проверка функции поплнения счета
    :return: результат проверки
    """
    sum_refill = np.random.randint(0,5000,1)[0]
    assert refill('холодильник') == 0
    assert refill(str(sum_refill)) == sum_refill

def test_sys_platform():
    """
    проверка функции test_sys_platform
    :return: результат проверки

    """
    s = sys.platform
    assert s == sys.platform

def test_sys_copyright():
    """
    проверка функции test_sys_copyright
    :return: результат проверки

    """
    s = sys.copyright
    assert s == sys.copyright

def test_mkdir():
    """
    Тест для грязной функции с побочным эффектом
    mkdir - создание директории
    """
    os.mkdir('folder_mk')
    # папка есть на диске
    assert 'folder_mk' in os.listdir()
    os.rmdir('folder_mk')


def test_rmdir():
    """
    Тест для грязной функции с побочным эффектом
    rmdir - удаление директории
    """
    os.mkdir('folder_to_remove')
    assert 'folder_to_remove' in os.listdir()
    # теперь удаляем папку
    os.rmdir('folder_to_remove')
    assert not ('folder_to_remove' in os.listdir())


if __name__ == '__main__':

    print(1)