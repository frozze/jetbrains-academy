# Write your code here
class CoffeeMachine:

    def __init__(self):
        self.waterMl = 400
        self.milkMl = 540
        self.beansGr = 120
        self.disposableCups = 9
        self.cashInSafe = 550

    def take_cash(self):
        print(f"I gave you ${self.cashInSafe}")
        print(' ')
        self.cashInSafe = 0

    def machine_status(self):
        print("The coffee machine has:")
        print(f"{self.waterMl} ml of water")
        print(f"{self.milkMl} ml of milk")
        print(f"{self.beansGr} g of beans")
        print(f"{self.disposableCups} disposable cups")
        print(f"${self.cashInSafe} of money")
        print(' ')

    def fill_ingredients(self):
        print('Write how many ml of water you want to add:')
        water = int(input())
        print('Write how many ml of milk you want to add:')
        milk = int(input())
        print('Write how many grams of coffee beans you want to add:')
        beans = int(input())
        print('Write how many disposable cups of coffee you want to add:')
        cups = int(input())
        self.waterMl += water
        self.milkMl += milk
        self.beansGr += beans
        self.disposableCups += cups

    def coffee_buy(self, coffee_choice):
        if coffee_choice == '1':
            if self.waterMl < 250:
                print(f'Sorry, not enough water!')
                self.user_action()
            elif self.beansGr < 16:
                print(f'Sorry, not enough beans!')
                self.user_action()
            elif self.disposableCups < 1:
                print(f'Sorry, not enough cups!')
                self.user_action()
            else:
                print('I have enough resources, making you a coffee!')
                self.waterMl -= 250
                self.beansGr -= 16
                self.disposableCups -= 1
                self.cashInSafe += 4
                self.user_action()
        if coffee_choice == '2':
            if self.waterMl < 350:
                print(f'Sorry, not enough water!')
                self.user_action()
            elif self.milkMl < 75:
                print(f'Sorry, not enough milk!')
                self.user_action()
            elif self.beansGr < 20:
                print(f'Sorry, not enough beans!')
                self.user_action()
            elif self.disposableCups < 1:
                print(f'Sorry, not enough cups!')
                self.user_action()
            else:
                print('I have enough resources, making you a coffee!')
                self.waterMl -= 350
                self.milkMl -= 75
                self.beansGr -= 20
                self.disposableCups -= 1
                self.cashInSafe += 7
                self.user_action()
        if coffee_choice == '3':
            if self.waterMl < 200:
                print(f'Sorry, not enough water!')
                self.user_action()
            elif self.milkMl < 100:
                print(f'Sorry, not enough milk!')
                self.user_action()
            elif self.beansGr < 12:
                print(f'Sorry, not enough beans!')
                self.user_action()
            elif self.disposableCups < 1:
                print(f'Sorry, not enough cups!')
                self.user_action()
            else:
                print('I have enough resources, making you a coffee!')
                self.waterMl -= 200
                self.milkMl -= 100
                self.beansGr -= 12
                self.disposableCups -= 1
                self.cashInSafe += 6
                self.user_action()
        else:
            self.user_action()

    def user_action(self):
        while True:
            user_action = input('Write action (buy, fill, take, remaining, exit):\n',)
            if user_action == 'buy':
                print('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino , back - to main menu:')
                user_action = input()
                if user_action == '1':
                    self.coffee_buy(user_action)
                if user_action == '2':
                    self.coffee_buy(user_action)
                if user_action == '3':
                    self.coffee_buy(user_action)
                if user_action == 'back':
                    self.user_action()
            if user_action == 'fill':
                self.fill_ingredients()
            if user_action == 'take':
                self.take_cash()
            if user_action == 'remaining':
                self.machine_status()
            if user_action == 'exit':
                exit()


coffee = CoffeeMachine()
coffee.user_action()
