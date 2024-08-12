import time
import math
import random

def print_pause(texts,delay):
    # this prints then pauses
    print(texts)
    time.sleep(delay)

def helpchinp(txt,ans):
    # this checks if the condition is false
    if txt is False:
        time.sleep(0)
    else:
        print_pause(f'enter {txt} for {ans}',1)

def check_input(ch1,ch2,ch3,ch4,ans1,ans2,ans3,ans4):
    # this checks if the input  is in the choices
    # if you want to test then take the example and then you can change
    # inp1 = check_input('1','2',False,'4','hi','hello',False,'welcome')
    # print(inp1)
    helpchinp(ch1,ans1)
    helpchinp(ch2,ans2)
    helpchinp(ch3,ans3)
    helpchinp(ch4,ans4)
    while True:
        time.sleep(1)
        inp =str(input('Please enter your input '))
        if inp == ch1:
            return ans1
        elif inp == ch2:
            return ans2
        elif inp == ch3:
            return ans3
        elif inp == ch4:
            return ans4
        else:
            z = 0
def number_check(txt):
    while True:
        inp = (input(f'Enter your {txt} '))
        if inp.isnumeric() is True:
            inp = int(inp)
            return round(inp)
        else:
            z = 0
def close_app():
    Y =0
    print_pause('If you want to continue enter Yes',2)
    print_pause('If you want to close the app enter no',2)
    ListY = ('yes','ye','y','ys','es')
    ListN = ('no','n')
    while Y == 0 :
        X = str(input('Please write Yes or No '))
        X = X.lower()
        if X in ListY :
            print_pause('restarting',2)
            print('------------------------------')
            Y = 1
        elif X in ListN :
            print_pause('Thanks for using our app',1)
            print_pause('Goodbye',1)
            return True
        elif X == 'how' :
            print_pause('one night',1)
            print_pause('Two days',1)
            return True


