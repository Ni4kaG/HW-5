# 1. встроенные модули
import random
import os
import sys
import shutil

import pickle


# 2. наши модули
from Lesson5modules.my_function_prev_lessons import *

FILE_NAME = 'listdir.txt'

def save_call_to_file(func):
    def inner(*args, **kwargs):
        # пишем первый (единственный) параметр фукнции в файл
        function_param = args[0]
        with open('log.txt', 'a', encoding='utf-8') as f:
            f.write(f'{function_param}\n')

        result = func(*args, **kwargs)
        return result

    return inner


@save_call_to_file
def cons_file_manager(num_choise):
    result = True
    if num_choise == '1':       # создать папку
       os.mkdir('my_new_dir') if not os.path.exists('my_new_dir') else 1    #  тернарный оператор
    elif num_choise == '2':     # удалить (файл/папку)
        os.rmdir('my_new_dir') if os.path.exists('my_new_dir') else 1       #  тернарный оператор
    elif num_choise == '3':     # копировать (файл/папку)
        shutil.copy('my_function_prev_lessons.py', 'my_function_prev_lessons_copy.py')
    elif num_choise == '4':     # просмотр содержимого рабочей директории
        f = open(FILE_NAME,'w')

        f.write('Files: ')
        content = os.listdir()
        result = [file + ', ' for file in content if os.path.isfile(file)]  # генератор списка
        f.writelines(list(result))

        f.write('\n' + 'Dirs: ')
        content = os.listdir()
        result = [file + ', ' for file in content if not os.path.isfile(file)] # генератор списка
        f.writelines(result)
        f.close()
    elif num_choise == '5':     # ппосмотреть только папки
        print([file for file in os.listdir() if not os.path.isfile(file)])  # генератор списка
    elif num_choise == '6':     # ппосмотреть только файлы
        print([file for file in os.scandir()])                              # генератор списка
    elif num_choise == '7':     # просмотр информации об операционной системе
        print(sys.platform)
    elif num_choise == '8':     #  создатель программы
        print(sys.copyright)
    elif num_choise == '9':     #  играть в викторину
        victory()
    elif num_choise == '10':    # мой банковский счет
        pers_account()
    elif num_choise == '11':    # смена рабочей директории
        path = os.path.join(os.getcwd(), 'Lesson5modules')
        os.chdir(path)
        print(os.getcwd())
    elif num_choise == '12':
        result = False
    else:
        print('Неверный пункт меню')
    return result

to_play = True
while to_play:
    print(' 1. создать папку')
    print(' 2. удалить (файл/папку)')
    print(' 3. копировать (файл/папку)')
    print(' 4. просмотр содержимого рабочей директории')
    print(' 5. посмотреть только папки')
    print(' 6. посмотреть только файлы')
    print(' 7. просмотр информации об операционной системе')
    print(' 8. создатель программы')
    print(' 9. играть в викторину')
    print('10. мой банковский счет')
    print('11. смена рабочей директории')
    print('12. выход')
    to_play = cons_file_manager(input('Выберите пункт меню: '))
