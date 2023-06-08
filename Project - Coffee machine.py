import time
print('==================== WELCOME TO COFFEE VENDING MACHINE ===================')
fullname = input('Please,enter your fullname: ')
menu = {
    1: 'Cappucinno',
    2: 'Latte',
    3: 'Americano',
    4: 'Mocha',
    5: 'Espresso',
    6: 'Cortado',
    7: 'Caramel Cortado',
    8: 'Flat White',
    9: 'Flat Black',
    10: 'Classic',
    11: 'Dopio',
    12: 'Macchiato',
    13: 'Red eye',
    14: 'Galao',
    15: 'Lungo',
    16: 'Risretto',
    17: 'Affogato',
    18: 'Cafe au laif',
    19: 'Irish',
    20: 'Пополнить баланс'
    }

price = {
    1:'20',
    2:'20',
    3:'15',
    4:'25',
    5:'19',
    6:'17',
    7:'23',
    8:'15',
    9:'15',
    10:'10',
    11:'14',
    12:'18',
    13:'20',
    14:'23',
    15:'19',
    16:'18',
    17:'21',
    18:'20',
    19:'17',
    20:'0'
    }
u = 1
balance = int(input(f'Dear {fullname}, enter the deposit (in TMT): '))
if balance < 10:
    print('Unfortunately you do not have enough money to buy anything from machine :(')
elif balance >= 10:
    print()
    while True:
        print(f'\t\t====== Menu ======')
        for i in menu:
            print(f'\t\t{u}. {menu[i]}')
            u += 1
        break
    while True:
        
        print('=========='*6)
        operation = int(input('Enter the number of operation: '))
        if 0 < operation <= 19:
            print('-------' * 8)
            for i in price:
                if balance >= int(price[i]):
                    if operation == i:
                        hot_cold = input(f'Do you want cold {menu[i]} or hot? (cold/hot): ')
                        print('-------' * 8)
                        if hot_cold == 'cold':
                            print(f'Making your cold {menu[i]}... Please wait...')
                            print('===========' * 3)
                            print()
                            print('\t     )))      )))')
                            time.sleep(4 / 10)
                            print('\t    (((      (((')
                            time.sleep(4 / 10)
                            print('\t____________________')
                            time.sleep(4 / 10)
                            print('\t\ ***************** /==')
                            time.sleep(4 / 10)
                            print('\t \ *************** /   |')
                            time.sleep(4 / 10)
                            print('\t  \ ************* /    |')
                            time.sleep(4 / 10)
                            print('\t   \ *********** /=====')
                            time.sleep(4 / 10)
                            print('\t    \ ********* /')
                            time.sleep(4 / 10)
                            print('\t     -----------')
                            print()
                            time.sleep(4 / 10)
                            print('=========='*5)
                            '''print('[',end = '')
                            time.sleep(1)
                            print(f'========',end='')
                            time.sleep(6/10)
                            print(f'========',end='')
                            time.sleep(6/10)
                            print(f'========',end='')
                            time.sleep(6/10)
                            print(f'========',end='')
                            time.sleep(6/10)
                            print(f'========',end='')
                            time.sleep(6/10)
                            print(']')'''
                            balance -= int(price[i])
                            print(f'Here is nice cold {menu[i]} for {fullname} :) You have spent {price[i]} TMT\n=========== YOUR BALANCE IS {balance} TMT ===========')
                            print('=========='*5)
                        elif hot_cold == 'hot':
                            print(f'Making your hot {menu[i]}... Please wait...')
                            print('===========' * 3)
                            print()
                            print('\t     )))      )))')
                            time.sleep(4 / 10)
                            print('\t    (((      (((')
                            time.sleep(4 / 10)
                            print('\t____________________')
                            time.sleep(4 / 10)
                            print('\t\ ***************** /==')
                            time.sleep(4 / 10)
                            print('\t \ *************** /   |')
                            time.sleep(4 / 10)
                            print('\t  \ ************* /    |')
                            time.sleep(4 / 10)
                            print('\t   \ *********** /=====')
                            time.sleep(4 / 10)
                            print('\t    \ ********* /')
                            time.sleep(4 / 10)
                            print('\t     -----------')
                            print()
                            time.sleep(4 / 10)
                            print('=========='*5)
                            '''print('[',end = '')
                            time.sleep(1)
                            print(f'========',end='')
                            time.sleep(6/10)
                            print(f'========',end='')
                            time.sleep(6/10)
                            print(f'========',end='')
                            time.sleep(6/10)
                            print(f'========',end='')
                            time.sleep(6/10)
                            print(f'========',end='')
                            time.sleep(6/10)
                            print(']')'''
                            balance -= int(price[i])
                            print(f'Here is hot {menu[i]} for {fullname} :) You have spent {price[i]} TMT\n=========== YOUR BALANCE IS {balance} TMT ===========')
                            print('=========='*5)
                        yes_no = input('Do you want to continue? (yes/no/addmoney): ')
                        if yes_no == 'yes':
                            print()
                        elif yes_no == 'no':
                            print('Have a nice day!')
                            break

                         #oshibka logika
                        elif yes_no == 'addmoney':
                            money = int(input('How much money do you want to replenish? '))
                            balance += money
                            print('[', end='')
                            time.sleep(1)
                            print(f'========', end='')
                            time.sleep(6 / 10)
                            print(f'========', end='')
                            time.sleep(6 / 10)
                            print(f'========', end='')
                            time.sleep(6 / 10)
                            print(f'========', end='')
                            time.sleep(6 / 10)
                            print(f'========', end='')
                            time.sleep(6 / 10)
                            print(']')
                            print(f'You have replenished your balance for {money}, now your balance is {balance} TMT')
                else:
                    print('You do not have enough money :(')
                    break
        if yes_no =='no':
            break
        elif operation == 20:
            money = int(input('How much money do you want to replenish? '))
            balance += money
            print('[', end='')
            time.sleep(1)
            print(f'========', end='')
            time.sleep(6 / 10)
            print(f'========', end='')
            time.sleep(6 / 10)
            print(f'========', end='')
            time.sleep(6 / 10)
            print(f'========', end='')
            time.sleep(6 / 10)
            print(f'========', end='')
            time.sleep(6 / 10)
            print(']')
            print(f'You have replenished your balance for {money} TMT, now your balance is {balance} TMT')
        else:
            print('Wrong operation! Try again!')

        
        
            
