def refill():
    refill_sum = input('Введите сумму поступления: ')
    if refill_sum.isdigit():
        return (int(refill_sum))
    else:
        print('Некорректная сумма пополнения!')
        return 0


def purchases(acc_sum):
    purch_sum = 0
    purch_purpose = ''
    purch_s = input('Введите сумму покупки: ')
    if purch_s.isdigit():
        purch_sum = int(purch_s)
        if purch_sum <= acc_sum:
            purch_purpose = input('Введите цель покупки: ')
        else:
            purch_sum = 0
            print('Недостаточно средств')
    else:
        print('Некорректная сумма покупки!')
    return (purch_purpose, purch_sum)


def pers_account():
    account_sum = 0
    purchases_history_list = list()
    purchase = list()

    while True:
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')

        choice = input('Выберите пункт меню: ')
        if choice == '1':
            account_sum += refill()
        elif choice == '2':
            purchase = purchases(account_sum)
            account_sum -= purchase[1]
            if purchase != ('',0):
                purchases_history_list.append(purchase)
        elif choice == '3':
            for purch in purchases_history_list:
                print('\t{0} на сумму \t{1} руб.'.format(purch[0], purch[1]))
        elif choice == '4':
            break
        else:
            print('Неверный пункт меню')
def victory():
    import random
    # quests_list: list[int]
    birthdays_dict = {'Уинстона Черчилля': '30.11.1874',
                      'Махатмы Ганди': '02.10.1869',
                      'Микельанджело': '06.03.1475',
                      'Виктора Пелевина': '22.11.1962',
                      'Юрия Дудя': '11.10.1986',
                      'Ивана Грозного': '25.08.1530',
                      'Сергея Рахманинова': '20.03.1873',
                      'Михаила Лермонтова': '15.10.1814',
                      'Михаила Булгакова': '15.05.1891',
                      'Михаила Врубеля': '17.03.1856',
                      'Юрия Гагарина': '09.03.1934',
                      'Софьи Ковалевской': '15.01.1850'
                      }
    month_dict = {'01': 'января',
                  '02': 'февраля',
                  '03': 'марта',
                  '04': 'апреля',
                  '05': 'мая',
                  '06': 'июня',
                  '07': 'июля',
                  '08': 'августа',
                  '09': 'сентября',
                  '10': 'октября',
                  '11': 'ноября',
                  '12': 'декабря'}
    days_dict = {'30': 'тридцатого',
                 '02': 'второго',
                 '06': 'шестого',
                 '22': 'двадцать второго',
                 '11': 'одиннадцатого',
                 '25': 'двадцать пятого',
                 '20': 'двадцатого',
                 '15': 'пятнадцатого',
                 '09': 'девятого',
                 '17': 'семнадцатого'
                 }

    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    quests_list = random.sample(numbers, 5)
    to_repeat = True
    while to_repeat:
        correct_answer_num = 0
        for i in quests_list:
            name, date = random.choice(list(birthdays_dict.items()))
            answer = input("Введите дату рождения " + name + ': ')
            correct_answer = date.split('.')
            if answer == date:
                correct_answer_num += 1
            else:
                print('Неверно. Правильный ответ - {0} {1} {2} года'.format(days_dict.get(correct_answer[0]),
                                                                            month_dict.get(correct_answer[1]),
                                                                            correct_answer[2]))

        correct_answer_proc = correct_answer_num / 5
        print('Ваш результат:')
        print('\tПравильных ответов:\t', correct_answer_num)
        print('\tНеправильных ответов:', 5 - correct_answer_num)
        print('\tПроцент правильных ответов {:5.1%}'.format(correct_answer_proc))
        print('\tПроцент неправильных ответов {:5.1%}'.format(1 - correct_answer_proc))
        answer = input("Хотите начать игру заново (y/n): ")
        if answer != 'y':
            to_repeat = False

