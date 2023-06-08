print('========= Welcome to Drink Vending Machine =========')
print('''
                     _____________
                    |  _______    |
                    | |_______|   |
             \\\     | |_______|-- |    //
                    | |_______|== |
               \\\   | |_______|   |   //
                    | |_______|   |
                    | |_______| __|
                    | |_______||__|
                    | |_______|   |
                    |             |
                    |_____________|
    ''')
drinks = ['Coca Cola', 'White Claw Vodka', 'High Noon Tequila',
          'Pepsi','Diet Coke', 'Doctor Pepper',
          'Mountain Dew', 'Sprite',
          'Diet Pepsi', 'Sprite',
          'Bold', 'Fanta', 'Archalyk',
          'Powrize', '7 Up']
price = ['20','25','35','23','10','10',
         '50','5','20','8','5',
         '10','2','3','17']
i = 1
select = int(input('''
 ----------------------- Menu: ----------------------
1. Coca Cola         =============>  Price: 20 manats
2. White Claw Vodka  =============>  Price: 25 manats
3. High Noon Tequila =============>  Price: 35 manats
4. Pepsi             =============>  Price: 23 manats
5. Diet Coke         =============>  Price: 10 manats
6. Doctor Pepper     =============>  Price: 10 manats
7. Mountain Dew      =============>  Price: 50 manats
8. Lipton            =============>  Price: 5 manats
9. Diet Pepsi        =============>  Price: 20 manats
10. Sprite           =============>  Price: 8  manats
11. Bold             =============>  Price: 5  manats
12. Fanta            =============>  Price: 10 manats
13. Archalyk         =============>  Price: 2  manats
14. Powrize          =============>  Price: 3  manats
15. 7 Up             =============>  Price: 17 manats
-----------------------------------------------------
Enter the number of operation:   '''))
a = drinks[select - 1]
print(f'You have selected {a}')
cans = int(input('How many cans do you want? '))
price = int(price[select - 1]) * cans
print('------------------------------------------------------')
print(f'To buy {cans} cans of {a}, you need to pay {price} manats...')
paying = input('\n---- Do you want to pay by card or by card?\n1. Card\n2. Cash\nAnswer: ')
if paying == '1':
    card = input('Enter your card No.: ')
    import datetime
    import time
    import random
    print('------------------ Checking your card... ---------------------')
    print('', end='')
    time.sleep(1)
    print(f'                     _____________')
    time.sleep(6 / 10)
    print(f'                    |  _______    |')
    time.sleep(6 / 10)
    print(f'             \\\     | |_______|-- |    //')
    time.sleep(6 / 10)
    print(f'                    | |_______|== |')
    time.sleep(6 / 10)
    print(f'               \\\   | |_______|   |   //')
    time.sleep(6 / 10)
    print(f'                    | |_______|   |')
    time.sleep(6 / 10)
    print(f'                    | |_______| __|')
    time.sleep(6 / 10)
    print(f'                    | |_______||__|')
    time.sleep(6 / 10)
    print(f'                    | |_______|   |')
    time.sleep(6 / 10)
    print(f'                    |             |')
    time.sleep(6 / 10)
    print('                    |_____________|')
    print()
    print(f'You have successfully transfered {price} manats from your card No. {card} to Vending Machine IBAN')
    print(f'---------------- Check #{random.randint(100, 999)} ----------------')
    print(f'• Date of the contract: {datetime.datetime.now()}\n• Drink name: {drinks[int(select)-1]}\n• Price: {price} manats\n• Vending Machine ID: If23123ias23ikfs2')
    print('--------------------------------------------')
elif paying == '2':
    import datetime
    import time
    import random
    money = int(input('How much money do you have?  '))
    print('------------------- Counting money... ------------------------')
    print('', end='')
    time.sleep(1)
    print(f'                     _____________')
    time.sleep(6 / 10)
    print(f'                    |  _______    |')
    time.sleep(6 / 10)
    print(f'             \\\     | |_______|-- |    //')
    time.sleep(6 / 10)
    print(f'                    | |_______|== |')
    time.sleep(6 / 10)
    print(f'               \\\   | |_______|   |   //')
    time.sleep(6 / 10)
    print(f'                    | |_______|   |')
    time.sleep(6 / 10)
    print(f'                    | |_______| __|')
    time.sleep(6 / 10)
    print(f'                    | |_______||__|')
    time.sleep(6 / 10)
    print(f'                    | |_______|   |')
    time.sleep(6 / 10)
    print(f'                    |             |')
    time.sleep(6 / 10)
    print('                    |_____________|')
    if money >= price:
        print(f'You have successfully payed {price} manats to Ticket Machine')
        print(f'---------------- Check #{random.randint(100, 999)} ----------------')
        print(f'• Date of the contract: {datetime.datetime.now()}\n• Drink name: {drinks[int(select)-1]}\n• Price: {price} manats\n• Change: {money - price} manats\n• Vending Machine ID: If23123ias23ikfs2')
        print('----------------------------------------------------')
    else:
        print('--------- You do not have enough money :( ---------')
