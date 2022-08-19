# 1. встроенные модули
import random
import os
import sys
import shutil

import pickle


# 2. наши модули
from Lesson5modules.my_function_prev_lessons import *

FILE_NAME = 'listdir.txt'


while True:
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

    choice = input('Выберите пункт меню: ')
    if choice == '1':
# создать папку
        if not os.path.exists('my_new_dir'):
            os.mkdir('my_new_dir')
    elif choice == '2':
# удалить (файл/папку)
        if os.path.exists('my_new_dir'):
            os.rmdir('my_new_dir')
    elif choice == '3':
# копировать (файл/папку)
        shutil.copy('my_function_prev_lessons.py', 'my_function_prev_lessons_copy.py')
    elif choice == '4':
# просмотр содержимого рабочей директории
        f = open(FILE_NAME,'w')
        f.write('Files: ')
        content = os.listdir()
        for file in content:
            if os.path.isfile(file):
                f.write(file + ', ')
        f.write('\n' + 'Dirs: ')
        content = os.listdir()
        for file in content:
            if not os.path.isfile(file):
                f.write(file + ', ')
        f.close()
    elif choice == '5':
# ппосмотреть только папки
        content = os.listdir()
        for file in content:
            if not os.path.isfile(file):
                print(file)
    elif choice == '6':
# ппосмотреть только файлы
        with os.scandir() as files:
            for file in files:
                print(file)
    elif choice == '7':
# просмотр информации об операционной системе
        print(sys.platform)
    elif choice == '8':
#  создатель программы
        print(sys.copyright)
    elif choice == '9':
#  играть в викторину
        victory()
    elif choice == '10':
# мой банковский счет
        pers_account()
    elif choice == '11':
# смена рабочей директории
        path = os.path.join(os.getcwd(), 'Lesson5modules')
        os.chdir(path)
        print(os.getcwd())
    elif choice == '12':
        break
    else:
        print('Неверный пункт меню')