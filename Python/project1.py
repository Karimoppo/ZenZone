import time
import math
import random
Hlthyrcp ='Healthy recipes'
MlRem ='Meal reminders'
MlPrp ='meal preparation'
T = True
F = False
QBBS ='Quinoa and Black Bean Salad'
BSLD = 'Baked salmon with Lemon and Dill'
CSC = 'Chickpea and Spinach Curry'
GYCS = 'Greek Yougurt Chiken Salad'
AEBB = 'Avocado and Egg Breakfast Bowl'
ZNP = 'Zucchini Noodles with Pesto'
QBBSDES1 = 'Cook quinoa according to package instructions. '
QBBSDES2 = 'Mix with black beans, corn, chopped tomatoes,'
QBBSDES3 = ' diced avocado, lime juice, and chopped cilantro.'
QBBSDES =f'{QBBSDES1}{QBBSDES2}{QBBSDES3}'
BSLDDES1 = ' Season salmon with olive oil, lemon juice, minced garlic,'
BSLDDES2 = ' and dill. Bake at 375°F (190°C) for 15-20 minutes.'
BSLDDES = f'{BSLDDES1}{BSLDDES2}'
CSCDES1 = 'Sauté onion, garlic, and ginger. Add curry powder, coconut '
CSCDES2 = 'milk, and chickpeas. Simmer for 20 minutes, then stir in spinach until wilted.'
CSCDES = f'{CSCDES1}{CSCDES2}'
GYCSDES1 = 'Cook and shred chicken. Mix with Greek yogurt, '
GYCSDES2 = 'chopped celery, halved grapes, and almonds. Chill before serving'
GYCSDES = f'{GYCSDES1}{GYCSDES2}'
AEBBDES1 =  'Sauté spinach and cherry tomatoes. Cook eggs to your preference '
AEBBDES2 = '(poached or scrambled). Serve over spinach with sliced avocado.'
AEBBDES = f'{AEBBDES1}{AEBBDES2}'
ZNPDES1 = 'Spiralize zucchini into noodles and sauté for 3-5 minutes. '
ZNPDES2 = 'Toss with pesto sauce, cherry tomatoes, and a sprinkle of Parmesan cheese.'
ZNPDES = f'{ZNPDES1}{ZNPDES2}'
QBBSI1 = '1 cup quinoa (uncooked)'
QBBSI2 = '1 can black beans (15 oz), drained and rinsed'
QBBSI3 = '1 cup corn (frozen or fresh)'
QBBSI4 = '1 cup cherry tomatoes, halved'
QBBSI5 = '1 avocado, diced'
QBBSI6 = '2 tablespoons lime juice'
QBBSI7 = '1/4 cup chopped cilantro'
QBBSI = f'{QBBSI1}.{QBBSI2}.{QBBSI3}.{QBBSI4}.{QBBSI5}.{QBBSI6}.{QBBSI7}'
BSLDI1 = '4 salmon fillets'
BSLDI2 = '1 lemon, sliced'
BSLDI3 = '2 tablespoons fresh dill'
BSLDI4 = '1 tablespoon olive oil'
BSLDI5 = '2 cloves garlic, minced'
BSLDI =f'{BSLDI1}.{BSLDI2}.{BSLDI3}.{BSLDI4}.{BSLDI5}'
CSCI1 = '1 can chickpeas (15 oz), drained and rinsed'
CSCI2 = '2 cups fresh spinach'
CSCI3 = '1 can coconut milk (14 oz)'
CSCI4 = '2 tablespoons curry powder'
CSCI5 = '1 onion, chopped'
CSCI6 = '2 cloves garlic, minced'
CSCI7 = '1 tablespoon fresh ginger, minced'
CSCI =f'{CSCI1}.{CSCI2}.{CSCI3}.{CSCI4}.{CSCI5}.{CSCI6}.{CSCI7}.'
GYCSI1 = '2 cups cooked, shredded chicken breast'
GYCSI2 = '1 cup Greek yogurt'
GYCSI3 = '1/2 cup celery, chopped'
GYCSI4 = '1/2 cup grapes, halved'
GYCSI5 = '1/4 cup almonds, chopped'
GYCSI6 = '1 tablespoon lemon juice'
GYCSI =f'{GYCSI1}.{GYCSI2}.{GYCSI3}.{GYCSI4}.{GYCSI5}.{GYCSI6}.'
AEBBI1 = '2 eggs'
AEBBI2 = '1 avocado, sliced'
AEBBI3 = '1 cup fresh spinach'
AEBBI4 =  '1/2 cup cherry tomatoes, halved'
AEBBI5 = 'Salt and pepper to taste'
AEBBI =f'{AEBBI1}.{AEBBI2}.{AEBBI3}.{AEBBI4}.{AEBBI5}.'
ZNPI1 ='4 medium zucchinis'
ZNPI2 ='1/2 cup pesto sauce'
ZNPI3 ='1 cup cherry tomatoes, halved'
ZNPI4 ='1/4 cup grated Parmesan cheese'
ZNPI =f'{ZNPI1}.{ZNPI2}.{ZNPI3}.{ZNPI4}.'
ATQBBS ='Potential Allergens: '
AT1QBBS = 'Avocado: Generally safe, but some people might be sensitive to it.'
AT2QBBS = 'Cilantro: Rare, but some might be allergic or have an aversion.'
ATTQBBS =f'{ATQBBS}{AT1QBBS}{AT2QBBS}'
ATBSLD = 'Potential Allergens: '
AT1BSLD ='Salmon (Fish): Common allergen. If someone is allergic '
AT2BSLD = 'to fish, this recipe is not suitable.'
AT3BSLD = 'Dill, Lemon, Olive Oil: Generally non-allergenic.'
ATTBSLD =f'{ATBSLD}{AT1BSLD}{AT2BSLD}{AT3BSLD}'
ATCSC ='Potential Allergens: '
AT1CSC ='Chickpeas: Rare, but some may have legume allergies.'
AT2CSC ='Coconut Milk: Contains coconut, which '
AT3CSC ='is a common allergen for some people.'
AT4CSC ='Spices (Curry Powder): Generally safe, but some'
AT5CSC =' spices might trigger allergies or intolerances.'
ATTCSC =f'{ATCSC}{AT1CSC}{AT2CSC}{AT3CSC}{AT4CSC}{AT5CSC}'
ATGYCS ='Potential Allergens: '
AT1GYCS ='Greek Yogurt: Contains dairy, which is a common allergen.'
AT2GYCS ='Almonds: Nut allergen.'
AT3GYCS ='Chicken: Generally non-allergenic unless there are specific sensitivities.'
ATTGYCS =f'{ATGYCS}{AT1GYCS}{AT2GYCS}{AT3GYCS}'
ATAEBB = 'Potential Allergens: '
AT1AEBB = 'Eggs: Common allergen.'
AT2AEBB = 'Avocado: Generally safe but can cause reactions in sensitive individuals.'
AT3AEBB = 'Spinach and Tomatoes: Generally non-allergenic.'
ATTAEBB =f'{ATAEBB}{AT1AEBB}{AT2AEBB}{AT3AEBB}'
ATZNP = 'Potential Allergens:'
AT1ZNP ='Pesto Sauce: Often contains nuts (e.g., pine nuts)'
AT2ZNP =', dairy (Parmesan cheese), and sometimes garlic.'
AT3ZNP ='Parmesan Cheese: Contains dairy.'
ATTZNP =f'{ATZNP}{AT1ZNP}{AT2ZNP}{AT3ZNP}'
SSQBBS ='About 1.5 cups'
SSBSLD ='1 salmon fillet (approximately 6 oz)'
SSCSC = 'Serving Size: About 1.5 cups'
SSGYCS ='Serving Size: About 1 cup'
SSAEBB = '1 bowl (contains 2 eggs and 1/2 avocado)'
SSZNP = 'Serving Size: About 2 cups'
meal_number = [1,2,3,4,5]
meal_name = [QBBS,BSLD,CSC,GYCS,AEBB,ZNP]
meal_Desc = [QBBSDES,BSLDDES,CSCDES,GYCSDES,AEBBDES,ZNPDES]
meal_time = [20,20,30,15,10,15]
meal_YNaler = [T,T,T,T,T,T]
meal_alertype = [ATTQBBS,ATTBSLD,ATTCSC,ATTGYCS,ATTAEBB,ATTZNP]
meal_calories = [350,250,350,300,350,250]
meal_ingreadients = [QBBSI,BSLDI,CSCI,GYCSI,AEBBI,ZNPI]
meal_servingsize = [SSQBBS,SSBSLD,SSCSC,SSGYCS,SSAEBB,SSZNP]
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
        inp = (input(f'Enter {txt} : '))
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
def passw():
    print_pause('The password needs to be more than 8 characters',2)
    print_pause('and it needs to have a mix of upper and lower case letters',2)
    c = 0
    z = 0
    while True:
        passw=str(input('Enter your password : '))
        confpassw=str(input('Confirm your password : '))
        for x in passw:
            if x.upper() == passw[z]:
                c += 1
            z += 1
        if passw == confpassw and len(passw) >= 8 :
            if c < 1 or c == len(passw):
                print_pause('The password needs to have',1)
                print_pause('Both upper case letters and lower case',1)
            elif c >= 1 and c < len(passw):
                return passw
        elif passw == confpassw and len(passw) < 8:
            print_pause('The password needs to have',1)
            print_pause('Enter more than 8 caracters',1)
        else :
            print_pause('Confirm the password correctly',1)
username = str(input('Enter your user name : '))
email = str(input('Enter your email : '))
password = passw()
age = number_check('your Age')
# YNalergie = check_input('1','2',F,F,'if you have alergies','if you do not have alergies',F,F)
while True:
    print_pause('Welcome to our zen zone healthy lifestyle app',1)
    inp1 = check_input('1','2','3',F,Hlthyrcp,MlRem,MlPrp,F)
    if inp1 == Hlthyrcp :
        print_pause('You have chosen Healthy Recipies ',1)
        print_pause('You can find some healthy recipies that you can have in your diet',2)
        print_pause('We have 6 meals for you',1)
        mlno = 0
        while True :
            print_pause(f'This is the meal number {meal_number[mlno]}',1)
            print_pause(f'The name of this meal is {meal_name[mlno]}',2)
            print_pause(f'These are the steps to cook it {meal_Desc[mlno]}',3)
            print_pause(f'The time it take to the cook is about {meal_time[mlno]} minutes',2)
            print_pause(f'This meal has {meal_calories[mlno]} per serving',2)
            print_pause(f'The serving size is {meal_servingsize[mlno]}',2)
            print_pause(f'The meal ingreadients are : {meal_ingreadients[mlno]}',4)
            print_pause(f'{meal_alertype[mlno]}',3)
            print_pause()
            mlno = number_check('the meal number')
            end = close_app()
            if end is T :
                break
            else:
                print('')

    elif inp1 == MlRem :
        print_pause('You have chosen the meal reminder',2)
        print_pause('you can choose the time in seconds',2)
        RemT =number_check('the time for the reminder')
        time.sleep(RemT)
        print_pause('Notification:The meal alarm')
        end = close_app()
    elif inp1 == MlPrp :
        end = close_app()
    else:
        print('hi')
    if end is T :
        break
    else:
        print('')
