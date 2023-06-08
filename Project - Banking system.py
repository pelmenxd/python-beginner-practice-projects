import random
import time
print('----------------WELCOME TO THE "U.S. Bancorp" BANKING SYSTEM!!!----------------')
print()
choice = input('Do you want to sign in or create a new banking account? (sign/create) ')
print('---------'*8)
tmt = 0
euro = 0
rubl = 0
yuan = 0

if choice == 'sign':
    login = 'pelmen'
    password = '12345'
    balance = 10000
    while True:
        user_l = input('Please, enter your login: ')
        if user_l == login:
            user_p= input('Please, enter your password: ')
            print('---------' *4)
            print('Processing...')
            time.sleep(3)
            print()
            if user_p == password:
                print('---------' * 4)
                print(f'Dear {login}, you successfully signed up to the "U.S. Bancorp" banking system!')
                print()
                break
            else:
                print('Invalid password :(   Try again')
        else:
            print('Invalid login :(   Try again')
    while True:
        print('\t\t------------CHOICE OPERATION-------------')
        print("Menu: \n 1. Replenish your account\n 2. Withdraw money \n 3. Transit the money \n 4. Exchange money\n 5. About the banking account\n 6. Close")
        print()
        number = int(input('Enter the number of operation: '))
        print('-------' * 8)
        if number == 1:
            money = int(input('How much money you want to add? (in USD) '))
            balance += money
            print('---------' *4)
            print('Processing...')
            time.sleep(3)
            print()
            print(f'Dear {login}, you topped up {money}$ to your balance! Your balance now is {balance}$')
            print('-------'*8)
        elif number == 2:
            reduce = int(input('Enter the amount of money you want to withdraw (in USD): '))
            print('---------' *4)
            print('Processing...')
            time.sleep(3)
            print()
            if balance > reduce and reduce > 0:
                balance -= reduce
                print(f'You got {reduce}$ withdraw. Your balance now is {balance}$')
                print('=========' * 4)
            else:
                print("Unfortunately, you don't have enough money!")
        elif number == 3:
            telephone = int(input('Enter the telephone number you want transit money to: '))
            amount = int(input(f'Enter the amount of money you want to transit to "{telephone}" (in USD): '))
            print('---------' *4)
            print('Processing...')
            print('---------' * 4)
            time.sleep(3)
            if balance > amount and amount > 0:
                balance -= amount
                print(f'{amount}$ are successfully transited to the {telephone}. Your balance now is {balance}$! ')
            else:
                print(f"Unfortunately, you don't have enough money ({amount}$ USD) to transit them to {telephone}!")
        elif number == 4:
            value = int(input(' How much money do you want to exchange? '))
            print('========================================')
            print('\tSelect exchange valute:')
            print('1.TMT---------------------------> dollar exchange rate: 19,3\n2.euro---------------------------> dollar exchange rate: 0,9\n3.ruble---------------------------> dollar exchange rate: 69\n4.yuan---------------------------> dollar exchange rate: 6,74')
            valute = int(input('Enter the number of exchange valute: '))
            balance -= value
            
            print('========================================')
            if valute == 1:
                tmt2 = value * 19.3
                tmt += value * 19.3
                print(f'You exchanged {value}$ USD to {tmt2} TMT')
                print(f'Your balance now is {balance}$ USD and {tmt} TMT')
                print('===============================')
            elif valute == 2:
                euro2 = value * 0.9
                euro += value * 0.9
                print(f'You exchanged {value}$ USD to {euro2} euro')
                print(f'Your balance now is {balance}$ USD and {euro} euro')
                print('===============================')

            elif valute == 3:
                rubl2 = value *  69
                rubl += value *  69
                print(f'You exchanged {value}$ USD to {rubl2} ruble')
                print(f'Your balance now is {balance}$ USD and {rubl} ruble')
                print('===============================')

            elif valute == 4:
                yuan2 = value * 6.74
                yuan += value * 6.74
                print(f'You exchanged {value}$ USD to {yuan2} yuan')
                print(f'Your balance now is {balance}$ USD and {yuan} yuan')
                print('===============================')
            else:
                print('Wrong operation')
        elif number == 5:
            print(f'Your banking account:\n**********************************\nThe name of the card owner: {login}\nYour IBAN: TMABB XXXX XXXX\n--------------Balance-------------:\n---{balance}$ USD\n---{tmt} TMT\n---{euro} euro\n---{rubl} rubles\n---{yuan} yuan')
        elif number == 6:
            print('Thank you for using "U.S. Bancorp" banking system!!!')
            print('---------' * 6)
            break
        else:
            print('Wrong operation :(    Try again!')
elif choice == 'create':
    numbers = ['1','2','3','4','5','6','7','8','9']
    letters = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','c','v','b','n','m']
    symbols = ['!','@','#','$','%','&','*','-','_','?']
    
    fullname = input('Enter your fullname: ')
    passport_no = input(f'Dear client {fullname}, write your passport No:')
    balance_1 = int(input(f'Dear client {fullname}, enter your deposit: '))
    print('---------' * 4)
    print('Wait please... We are creating your account in our system...')
    time.sleep(3)
    print('---------' * 4)
    letters_num = 12
    numbers_num = 8
    symbols_num = 7

    IBAN = []
    iban = ''
    for _ in range(1,letters_num + 1):
        IBAN.append(random.choice(letters))
    for i in range(1,numbers_num + 1):
        IBAN.append(random.choice(numbers))
    for y in range(1,symbols_num + 1):
        IBAN.append(random.choice(symbols))
    random.shuffle(IBAN)
    for i in IBAN:
        iban += i
    print(f'Dear client {fullname}! We created your account!')
    print()
    print(f'Account information: \n**************************\nIBAN No: {iban}\nBalance: {balance_1}$ USD')
    print('\t\t------------CHOISE OPERATION-------------\n')
    while True:
        print("Menu: \n 1. Replenish your account\n 2. Withdraw money \n 3. Transit the money \n 4. Exchange money\n 5. About the banking account\n 6. Close")
        print()
        number = int(input('Enter the number of operation: '))
        print('-------' * 8)
        if number == 1:
            money = int(input('How much money you want to add? (in USD) '))
            balance_1 += money
            print('---------' *4)
            print('Processing...')
            time.sleep(3)
            print()
            print(f'Dear {fullname}, you topped up {money}$ to your balance! Your balance now is {balance_1}$')
            print('-------'*8)
        elif number == 2:
            reduce = int(input('Enter the amount of money you want to withdraw (in USD): '))
            print('---------' *4)
            print('Processing...')
            time.sleep(3)
            if balance_1 > reduce and reduce > 0:
                balance_1 -= reduce
                print(f'You got {reduce}$ withdraw. Your balance now is {balance_1}$')
                print('=========' * 4)
            else:
                print("Unfortunately, you don't have enough money!")
        elif number == 3:
            telephone = input('Enter the telephone you want to transit the money to: ')
            amount = int(input(f'Enter the amount of money you want to transit to "{telephone}" (in USD): '))
            print('---------' *4)
            print('Processing...')
            print('---------' * 4)
            time.sleep(3)
            if balance_1 > amount and amount > 0:
                balance_1 -= amount
                print(f'{amount}$ are successfully transited to the {telephone}. Your balance now is {balance_1}$! ')
                print('-------' * 8)
            else:
                print(f"Unfortunately, you don't have enough money to transit them to {telephone}!")
        elif number == 4:
            value = int(input(' How much money do you want to exchange? '))
            print('========================================')
            print('\tSelect exchange valute:')
            print('1.TMT---------------------------> dollar exchange rate: 19,3\n2.euro---------------------------> dollar exchange rate: 0,9\n3.ruble---------------------------> dollar exchange rate: 69\n4.yuan---------------------------> dollar exchange rate: 6,74')
            valute = int(input('Enter the number of exchange valute: '))
            balance_1 -= value
            print('========================================')
            if valute == 1:
                tmt1 = value * 19.3
                tmt += value * 19.3
                print(f'You exchanged {value}$ USD to {tmt} TMT')
                print(f'Your balance now is {balance_1}$ USD and {tmt} in TMT')
                print('===============================')
                
            elif valute == 2:
                euro1 = value *  0.9
                euro += value * 0.9
                print(f'You exchanged {value}$ USD to {euro} euro')
                print(f'Your balance now is {balance_1}$ USD and {euro} in euro')
                print('===============================')
                
            elif valute == 3:
                rubl1 = value * 69
                rubl += value * 69
                print(f'You exchanged {value}$ USD to {rubl} ruble')
                print(f'Your balance now is {balance_1}$ USD and {rubl} in ruble')
                print('===============================')
                
            elif valute == 4:
                yuan1 = value * 6.74
                yuan += value * 6.74
                print(f'You exchanged {value}$ USD to {yuan} yuan')
                print(f'Your balance now is {balance_1}$ USD and {yuan} in yuan')
                print('===============================')
                
            else:
                print('Wrong operation... Try again')
        elif number == 5:
            print('Processing...')
            print('---------' * 4)
            time.sleep(3)
            print()
            print(f'Account information: \n**************************\nYour passport No: {passport_no}\nIBAN No: {iban}\n--------------Balance-------------:\n---{balance_1}$ USD\n---{tmt} TMT\n---{euro} euro\n---{rubl} rubles\n---{yuan} yuan')
            print()
            print('---------' * 4)
        elif number == 6:
            print('Thank you for using "U.S. Bancorp" banking system!!!')
            print('---------' * 6)
            break
        else:
            print('Wrong operation :(    Try again!')
else:
    print('Wrong operation!')

        
    

