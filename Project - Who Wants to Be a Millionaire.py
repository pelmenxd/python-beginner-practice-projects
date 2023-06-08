import time
import random
def p():
    print('=================='*4)
points = 0
balance = ['1000','3000', '5000', '10000', '20000',
           '35000', '50000', '70000', '100000', '150000',
           '250000','400000','600000','1000000','2000000']
qst = ['What software company is headquartered in Redmond, Washington?\na) Apple\nb) Microsoft\nc) Samsung\nd) Mi',
       'Who founded Elon Mask?\na) His mom\nb) His dad\nc) Apple\nd) Tesla',
       'What is \'programer\'?\na)monster\nb)sleeper\nc)specialist\nd) dumb',
       'Which of Odin\'s children is adopted?\na) Loki\nb) Thor\nc)Spider-man\nd) Iron Man',
       'What is the capital city of Australia?\na)Bern\nb) Budapesht\nc) Canberra\nd) England',
       'How many days are there in July?\na) 28\nb) 29\nc) 30\nd) 31',
       'Who killed Tony Stark’s parents?\na) Thor\nb) The Winter Soldier\nc) Natasha Rostova\nd) Aman Yagsyyew',
       'Who founded Tesla?\na) Nazar Annayew\nb) Elon Mask\nc) Ivan Durachok\nd) Chehov',
       'Who founded Amazon?\na) Fungi\nb) Jeff Bezos\nc) Kronos\nd) Alfa Romeo',
       'Arachnophobia is the fear of what?\na) little spaces\nb) flying\nc) Spiders\nd) Books']

answer = ['b','b','c','a','c','d','b','b','b','c']
a = [['b','c'],['b','d'],['c','d'],['a','b'],['c','d'],['c','d'],['a','b'],['a','b'],['a','b'],['c','d']]
fifty = ['What software company is headquartered in Redmond, Washington?\nb) Microsoft\nc) Samsung',
       'Who founded Elon Mask?\nb) His dad\nd) Tesla',
       'What is \'programer\'?\nc)specialist\nd) dumb',
       'Which of Odin\'s children is adopted?\na) Loki\nb) Thor',
       'What is the capital city of Australia?\nc) Canberra\nd) England',
       'How many days are there in July?\nc) 30\nd) 31',
       'Who killed Tony Stark’s parents?\na) Thor\nb) The Winter Soldier',
       'Who founded Tesla?\na) Nazar Annayew\nb) Elon Mask',
       'Who founded Amazon?\na) Fungi\nb) Jeff Bezos',
       'Arachnophobia is the fear of what?\nc) Spiders\nd) Books']

names = ['Aman', 'Nazar', 'Mered', 'Timur', 'Ibragim', 'Allan','Daniil', 'Nagym', 'Dmitriy', 'Nikolay']
surnames = ['Yagsyyew', 'Annayew', 'Atayew', 'Bashimow', 'Meredow', 'Trashkun', 'Belyayew']
fiftyfifty = 1
call = 1
crowd = 1


p()
print('---------------------- Who Wants to Be a Millionaire -------------------')
p()
#from tkinter import *
#pip install pillow
#from PIL import ImageTk, Image

#root = Tk()
#root.title("Image Viewer")
#root.geometry("1920x1080")
#image_no_1 = ImageTk.PhotoImage(Image.open("mil.jpg"))
#List_images = [image_no_1]
#label = Label(image=image_no_1)
#label.grid(row=1, column=0, columnspan=3)
#root.mainloop()
name = input('Enter your name: ')
ready = input(f'Dear {name} are you ready? (y/n):')
if ready == 'y':
    #root = Tk()
    #root.title("Image Viewer")
    #root.geometry("631x1131")
    #image_no_1 = ImageTk.PhotoImage(Image.open("list.png"))
    #List_images = [image_no_1]
    #label = Label(image=image_no_1)
    #label.grid(row=1, column=0, columnspan=3)
    #root.mainloop()
    p()
    print('You will have:')
    print('\t50:50 (Answer \'e\')\n\tCalling to friend (Answer \'f\')\n\tHelp from crowd (Answer \'g\')')
    p()
    for i in range(0,10):
        babki = balance[i]
        print(f'Question #{i+1}\n{qst[i]}')
        user = input('Answer: ')
        p()
        if user == answer[i]:
            print('Your answer is',end='')
            time.sleep(1)
            print('.',end='')
            time.sleep(1)
            print('.',end='')
            time.sleep(1)
            print('.',end='')
            print('TRUE')
            print(f'Your balance is {balance[i]}$ USD')
            p()
            points += 1
            yes_no = input('Do you want to continue(y/n): ')
            if yes_no == 'y':
                print('Okay...')
                p()
            if yes_no == 'n':
                break
        elif user == 'e':
            if fiftyfifty == 1:
                print('\t50/50')
                print(f'Question #{i+1}\n{fifty[i]}')
                user = input('Answer: ')
                p()
                fiftyfifty -= 1
                if user == answer[i]:
                    print('Your answer is',end='')
                    time.sleep(1)
                    print('.',end='')
                    time.sleep(1)
                    print('.',end='')
                    time.sleep(1)
                    print('.',end='')
                    print('TRUE')
                    print(f'Your balance is {balance[i]}$ USD')
                    p()
                    points += 1
                    yes_no = input('Do you want to continue(y/n): ')
                    if yes_no == 'y':
                        print('Okay...')
                        p()
                    if yes_no == 'n':
                        break
                else:
                    print('Your answer is',end='')
                    time.sleep(1)
                    print('.',end='')
                    time.sleep(1)
                    print('.',end='')
                    time.sleep(1)
                    print('.',end='')
                    print('FALSE')
                    print(f'Dear {name}, YOU LOST :(')
                    print(f'Your balance is {balance[i-1]}$ USD')
                    break
            else:
                print('Invalid! You have already used it')
                p()
                print(f'Question #{i+1}\n{qst[i]}')
                user = input('Answer: ')
                p()
                if user == answer[i]:
                    print('Your answer is',end='')
                    time.sleep(1)
                    print('.',end='')
                    time.sleep(1)
                    print('.',end='')
                    time.sleep(1)
                    print('.',end='')
                    print('TRUE')
                    print(f'Your balance is {balance[i]}$ USD')
                    p()
                    points += 1
                    yes_no = input('Do you want to continue(y/n): ')
                    if yes_no == 'y':
                        print('Okay...')
                        p()
                    if yes_no == 'n':
                        break
                else:
                    print('Your answer is',end='')
                    time.sleep(1)
                    print('.',end='')
                    time.sleep(1)
                    print('.',end='')
                    time.sleep(1)
                    print('.',end='')
                    print('FALSE')
                    print(f'Dear {name}, YOU LOST :(')
                    print(f'Your balance is {balance[i-1]}$ USD')
                    break

        elif user == 'f':
            if call == 1:
                n = random.choice(names)
                s = random.choice(surnames)
                m = random.choice(a[i])
                print(f'Calling to {n} {s}',end='')
                time.sleep(1)
                print('.',end='')
                time.sleep(1)
                print('.',end='')
                time.sleep(1)
                print('.')
                p()
                print(f'Friend {n} {s} thinks that answer is {m}')
                p()
                print(f'Question #{i+1}\n{fifty[i]}')
                user = input('Answer: ')
                p()
                call -= 1
                if user == answer[i]:
                    print('Your answer is',end='')
                    time.sleep(1)
                    print('.',end='')
                    time.sleep(1)
                    print('.',end='')
                    time.sleep(1)
                    print('.',end='')
                    print('TRUE')
                    print(f'Your balance is {balance[i]}$ USD')
                    p()
                    points += 1
                else:
                    print('Your answer is',end='')
                    time.sleep(1)
                    print('.',end='')
                    time.sleep(1)
                    print('.',end='')
                    time.sleep(1)
                    print('.',end='')
                    print('FALSE')
                    print(f'Dear {name}, YOU LOST :(')
                    print(f'Your balance is {balance[i-1]}$ USD')
                    break
            else:
                print('Invalid! You have already used it')
                p()
                print(f'Question #{i+1}\n{qst[i]}')
                user = input('Answer: ')
                p()
                if user == answer[i]:
                    print('Your answer is',end='')
                    time.sleep(1)
                    print('.',end='')
                    time.sleep(1)
                    print('.',end='')
                    time.sleep(1)
                    print('.',end='')
                    print('TRUE')
                    print(f'Your balance is {balance[i]}$ USD')
                    p()
                    points += 1
                    yes_no = input('Do you want to continue(y/n): ')
                    if yes_no == 'y':
                        print('Okay...')
                        p()
                    if yes_no == 'n':
                        break
                else:
                    print('Your answer is',end='')
                    time.sleep(1)
                    print('.',end='')
                    time.sleep(1)
                    print('.',end='')
                    time.sleep(1)
                    print('.',end='')
                    print('FALSE')
                    print(f'Dear {name}, YOU LOST :(')
                    print(f'Your balance is {balance[i-1]}$ USD')
                    break
        elif user == 'g':
            if crowd == 1:
                m = random.choice(a[i])
                print(f'Crowd thinks that answer is {m}')
                p()
                print(f'Question #{i+1}\n{fifty[i]}')
                user = input('Answer: ')
                p()
                crowd -= 1
                if user == answer[i]:
                    print('Your answer is',end='')
                    time.sleep(1)
                    print('.',end='')
                    time.sleep(1)
                    print('.',end='')
                    time.sleep(1)
                    print('.',end='')
                    print('TRUE')
                    print(f'Your balance is {balance[i]}$ USD')
                    p()
                    points += 1
                else:
                    print('Your answer is',end='')
                    time.sleep(1)
                    print('.',end='')
                    time.sleep(1)
                    print('.',end='')
                    time.sleep(1)
                    print('.',end='')
                    print('FALSE')
                    print(f'Dear {name}, YOU LOST :(')
                    print(f'Your balance is {balance[i-1]}$ USD')
                    break
            else:
                print('Invalid! You have already used it')
                p()
                print(f'Question #{i+1}\n{qst[i]}')
                user = input('Answer: ')
                p()
                if user == answer[i]:
                    print('Your answer is',end='')
                    time.sleep(1)
                    print('.',end='')
                    time.sleep(1)
                    print('.',end='')
                    time.sleep(1)
                    print('.',end='')
                    print('TRUE')
                    print(f'Your balance is {balance[i]}$ USD')
                    p()
                    points += 1
                    yes_no = input('Do you want to continue(y/n): ')
                    if yes_no == 'y':
                        print('Okay...')
                        p()
                    if yes_no == 'n':
                        break
                else:
                    print('Your answer is',end='')
                    time.sleep(1)
                    print('.',end='')
                    time.sleep(1)
                    print('.',end='')
                    time.sleep(1)
                    print('.',end='')
                    print('FALSE')
                    print(f'Dear {name}, YOU LOST :(')
                    print(f'Your balance is {balance[i-1]}$ USD')
                    break
        else:
            print('Your answer is',end='')
            time.sleep(1)
            print('.',end='')
            time.sleep(1)
            print('.',end='')
            time.sleep(1)
            print('.',end='')
            print('FALSE')
            print(f'Dear {name}, YOU LOST :(')
            print(f'Your balance is {balance[i-1]}$ USD')
            break
    print(f'Dear {name}, you have answered {points}/10 correctly. You got {balance[points-1]}$ USD')
else:
    print('Bye...')
