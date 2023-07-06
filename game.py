


def second_choice():
    choice = input("Would like to cut grass? or buy scissors for $5? Respond with 'cut grass' or 'buy scissors' ").lower()
    if choice == 'cut grass':
        player.cut_grass()
    elif choice == 'buy scissors':
        player.buy_scissors()
    else:
        print('do what??')
        second_choice()

def third_choice():
    choice = input("Would like to cut grass? or buy an old timey push lawnmower for $25? Respond with 'cut grass' or 'buy lawnmower' ").lower()
    if choice == 'cut grass':
        player.cut_grass()
    elif choice == 'buy lawnmower':
        player.buy_lawnmower()
    else:
        print('do what??')
        third_choice()

def fourth_choice():
    choice = input("Would like to cut grass? or buy a fancy battery powered mower for $250? Respond with 'cut grass' or 'buy fancy lawnmower' ").lower()
    if choice == 'cut grass':
        player.cut_grass()
    elif choice == 'buy fancy lawnmower':
        player.buy_fancy_lawnmower()
    else:
        print('do what??')
        fourth_choice()

def fifth_choice():
    choice = input("Would like to cut grass? or buy a team of starving students for $500? Respond with 'cut grass' or 'buy team of students' ").lower()
    if choice == 'cut grass':
        player.cut_grass()
    elif choice == 'buy team of students':
        player.buy_student_team()
    else:
        print('do what??')
        fifth_choice()

def win_message():
    print('You win the game yay!')


class User():
    def __init__(self, name, money=0):
        self.name = name
        self.money = money
        self.earn = 1
        self.tool = 'teeth'

    def current_tool(self):
        self.tool = self.tool
       
       
    def second_choice():
        choice = input("Would like to cut grass? or buy scissors for $5? Respond with 'cut grass' or 'buy scissors' ")
        if choice == 'cut grass':
            player.cut_grass()
        elif choice == 'buy scissors':
            player.buy_scissors()

    def cut_grass(self):
       self.money += self.earn
       print(f'You cut the grass with your {self.tool} and earned ${self.earn}. You have ${self.money} ')
       if self.money < 5:
            first_choice()    
       elif self.money >= 5 and self.tool == 'teeth':
            second_choice()
            first_choice()
       elif self.money >= 25 and self.tool == 'rusty scissors':
           third_choice()
           first_choice()
       elif self.money >= 250 and self.tool == 'old timey push lawnmower':
           fourth_choice()
           first_choice()
       elif self.money >= 500 and self.tool == 'fancy battery powered lawnmower':
           fifth_choice()
           first_choice()
       elif self.money >= 1000 and self.tool == 'team of starving students':
           win_message()

    def buy_scissors(self):
        if self.money < 5:
            print('You do not have enough money')
            second_choice()
        self.money -= 5
        self.tool = 'rusty scissors'
        self.earn = 5
        print(f'You now have ${self.money}, your tool is {self.tool}, and you can earn ${self.earn} per day')
        first_choice()

    def buy_lawnmower(self):
        if self.money < 25:
            print('You do not have enough money')
            third_choice()
        self.money -= 25
        self.tool = 'old timey push lawnmower'
        self.earn = 50
        print(f'You now have ${self.money}, your tool is {self.tool}, and you can earn ${self.earn} per day')
        first_choice()

    def buy_fancy_lawnmower(self):
        if self.money < 250:
            print('You do not have enough money')
            fourth_choice()
        self.money -= 250
        self.tool = 'fancy battery powered lawnmower'
        self.earn = 100
        print(f'You now have ${self.money}, your tool is {self.tool}, and you can earn ${self.earn} per day')
        first_choice()

    def buy_student_team(self):
        if self.money < 500:
            print('You do not have enough money')
            fifth_choice()
        self.money -= 500
        self.tool = 'team of starving students'
        self.earn = 250
        print(f'You now have ${self.money}, your tool is {self.tool}, and you can earn ${self.earn} per day')
        first_choice()
            



print('Welcome to the lawnmower game. You are starting a landscaping buisness and can only use your teeth to cut grass')
name = input('What is your name?')
player = User(name)
print(f'Hello {player.name}!')

choice = None
def first_choice():
    choice = input('Would you like to cut grass? Yes or No?').lower()
    if choice == 'yes':
        player.cut_grass()
    else:
        print("That's too bad")
        first_choice()

first_choice()

# def second_choice():
#     choice = input("Would like to cut grass? or buy scissors for $5? Respond with 'cut grass' or 'buy scissors' ").lower()
#     if choice == 'cut grass':
#         player.cut_grass()
#     elif choice == 'buy scissors':
#         player.buy_scissors()