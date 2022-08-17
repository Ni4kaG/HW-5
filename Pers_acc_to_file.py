import os
import pickle

def refill(refill_sum):

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


FILE_NAME_PURCH = 'purchase_pickle.data'
FILE_NAME_ACC = 'acc_pickle.data'

orders = []
acc_s = []
if os.path.exists(FILE_NAME_PURCH):
    with open(FILE_NAME_PURCH, 'rb') as f_purch:
        orders = pickle.load(f_purch)
else:
    purchase = list()
if os.path.exists(FILE_NAME_ACC):
    with open(FILE_NAME_ACC, 'rb') as f_acc:
        t_acc,account_sum = pickle.load(f_acc)
        print(t_acc,account_sum)
else:
    account_sum = 0


while True:
    print('1. пополнение счета')
    print('2. покупка')
    print('3. история покупок')
    print('4. выход')

    choice = input('Выберите пункт меню: ')
    if choice == '1':
        account_sum += refill(input('Введите сумму поступления: '))
    elif choice == '2':
        purchase = purchases(account_sum)
        name, summ = purchase
        account_sum -= summ
        if summ != 0:
            orders.append(purchase)
    elif choice == '3':
        for order in orders:
            print(order)
    elif choice == '4':
        with open(FILE_NAME_PURCH, 'wb') as f_purch:
            pickle.dump(orders, f_purch)
        with open(FILE_NAME_ACC, 'wb') as f_acc:
            pickle.dump(('Текцщий баланс счета:', account_sum), f_acc)
        break
    else:
        print('Неверный пункт меню')