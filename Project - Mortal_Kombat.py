#Github: pelmenxd
#Classes practice project - game "Mortal Kombat"
import random
import time
print('======================= Welcome to Mortal Kombat =====================')
print('''
                                  ⠀⠀⣠⣤⣤⣤⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⠿⠿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⡷⣶⠗⡹⢻⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠿⡒⣽⣮⣿⣿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠀⠀⠀⢸⣥⣻⣾⣿⣿⣿⠛⠛⠳⢶⣄⣠⠄⣀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⠖⠋⢩⣿⣿⣿⣿⣿⣿⢁⠀⣀⢀⣶⢟⡷⢾⠏⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠠⣿⣤⣮⣾⣿⣿⣿⣿⡟⠙⠛⠷⣶⣿⡵⠋⠙⡆⠆⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⢃⡏⠀⠠⣿⣿⣿⣿⣿⠀⠀⠀⣴⣟⣮⣀⠀⣸⢣⡥⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠈⢷⢀⣰⣿⣿⣿⣿⡷⢧⣶⣨⣯⣾⡇⠋⠙⠳⡟⡇⠆⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⣦⠸⠛⠉⣿⣿⣿⣿⠁⠀⠀⣿⣽⡯⣇⢁⠀⠀⠘⣿⠆⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⢁⠀⡆⠀⣿⣿⣿⣿⠀⠀⠀⢻⡯⣄⠝⢇⠆⡀⠠⣿⣞⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠠⠺⣫⣇⠂⢿⣿⣿⣿⠈⠀⢠⣿⣿⡇⠀⠈⠱⣵⢾⠏⣞⡃⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⢀⣟⣮⣽⣸⡮⠿⠿⠿⠿⠦⠭⠾⢿⠛⡇⠀⠀⢀⣻⢿⡶⠶⢿⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠈⣿⣾⣶⣽⢿⣿⣿⣿⣿⣿⣿⣿⣿⡐⣵⠀⠀⠈⣾⡞⠀⣄⡡⡃⠀⠀
                    ⠀⠀⠀⠀⠀⠀⢼⣿⣿⡿⢫⣮⢻⡝⠉⠉⢹⡏⢩⣵⣾⡣⢆⠀⠀⠸⣿⢄⡟⡗⡇⠀⠀
                    ⠀⠀⠀⠀⠀⠀⢿⣻⣯⠇⢸⣿⣾⡇⠀⠊⢌⣇⣿⣿⣿⣧⢡⢁⠀⠀⣿⢨⡇⣧⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⣿⡉⣹⣆⣿⣿⣿⡇⠀⠀⠠⣿⣿⣿⣿⣿⣆⢻⠀⣠⣿⣿⣷⡛⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠿⣷⡿⣿⣿⣿⣿⡇⠀⠀⠀⣿⣿⣿⣿⣿⣿⡄⡖⣑⢿⠉⣹⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⡇⠀⠀⠈⢹⣿⣿⣿⣿⣿⣷⡘⡡⠿⠖⠋⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⠧⠀⢀⠀⢸⣿⣿⣿⣿⣿⣿⣖⡁⠀⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣠⣄⡂⠐⣺⣿⣿⣿⣿⣿⣿⣷⡆⠀⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⣿⣿⣿⠃⠀⠀⢿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⠃⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠈⣍⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿⢿⣉⣀⠻⣦⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⢸⠁⠘⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⢠⢹⣿⠈⠘⡆⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠃⢀⢈⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣏⡄⠙⣏⠀⡀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠠⣇⢦⣿⣿⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢦⠝⣟⣧⠈⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⣸⢡⣾⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠪⢿⣻⢄⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⠀⠀⠀
                    ⠀⠀⠀⠀⢀⣠⣶⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣇⠀⠀
                    ⢀⣤⣴⣾⣿⣿⣿⣿⣿⣿⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣦⠀
                    ⠈⠉⠉⠉⠉⠉⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⣆
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠿⠋⠛⠋)
''')

class MortalKombat():
    def __init__(self,name,lvl,hp,deffence,atk):
        self.name = name
        self.hp = hp
        self.deffence = deffence
        self.atk = atk
        self.lvl = lvl
    def info(self):
        print(f'\t\t--------------- {self.name} -----------------\n\t\t\t  * Level: {self.lvl}\n\t\t\t  * hp: {self.hp}\n\t\t\t  * deffence: {self.deffence}\n\t\t\t  * atk: {self.atk}\n\t\t------------------------------------------')
        print('\t       ','--------'*5+ '--')
        
    def attack(self,enemy):
        enemy.hp -= self.atk
        print(f'{self.name} is attacking {enemy.name}')
        print(f'Hero hp: {self.hp}; Enemy hp: {enemy.hp}')
        print('--------'*5 + '--')


pl1_life = 1
pl2_life = 1
pl3_life = 1



player_1 = MortalKombat('Scorpion', 199,100,9,6)
player_1.info()
player_2 = MortalKombat('Sub zero', 199,100,12,4)
player_2.info()
player_3 = MortalKombat('Raiden',23,100,6,5)
player_3.info()

print('                                 FIGHTING',end='')
time.sleep(6/10)
print('.',end='')
time.sleep(6/10)
print('.',end='')
time.sleep(6/10)
print('.')
time.sleep(6/10)
#We need to randomly choose who will attack whom
while True:
    r = [player_1,player_2,player_3]
    if player_1.hp > 0 and player_2.hp > 0 and player_3.hp > 0:
        random.choice(r).attack(random.choice(r))
    elif player_1.hp <= 0:
        pl1_life -= 1
        print(f'***********************************************\n{player_1.name} is DEAD. {player_2.name} and {player_3.name} are left\n**********************************************')
        break
    elif player_2.hp <= 0:
        pl2_life -= 1
        print(f'***********************************************\n{player_2.name} is DEAD. {player_1.name} and {player_3.name} are left\n***********************************************')
        break
    elif player_3.hp <= 0:
        pl3_life -= 1
        print(f'***********************************************\n{player_3.name} is DEAD. {player_1.name} and {player_2.name} are left\n***********************************************')
        break
while True:
    if pl1_life == 0:
        while player_2.hp>=0 and player_3.hp>=0:
            if random.randint(0,1) == 0:
                player_2.attack(player_3)
            else:
                player_3.attack(player_2)
    elif pl2_life == 0:
        while player_1.hp>=0 and player_3.hp>=0:
            if random.randint(0,1) == 0:
                player_1.attack(player_3)
            else:
                player_3.attack(player_1)
    elif pl3_life == 0:
        while player_1.hp>=0 and player_2.hp>=0:
            if random.randint(0,1) == 0:
                player_1.attack(player_2)
            else:
                player_2.attack(player_1)

    if player_1.hp <= 0 and player_2.hp <= 0:
        print(f'!!!!!!!!!!!!!!!!!!!   {player_3.name} WON   !!!!!!!!!!!!!!!!!!!')
        break
    elif player_1.hp <= 0 and player_3.hp:
        print(f'!!!!!!!!!!!!!!!!!!!   {player_2.name} WON   !!!!!!!!!!!!!!!!!!!')
        break
    elif player_2.hp <= 0 and player_3.hp <= 0:
        print(f'!!!!!!!!!!!!!!!!!!!   {player_1.name} WON   !!!!!!!!!!!!!!!!!!!')
        break
    print(f'{player_1.name} hp: ', player_1.hp)
    print(f'{player_2.name} hp: ', player_2.hp)
    print(f'{player_3.name} hp: ', player_3.hp)