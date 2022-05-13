# Write your code here
machine = {'water': 400, 'milk': 540, 'beans': 120, 'cups': 9, 'money': 550}
    
    

def check(water, milk, beans, cups):
    if machine['water'] >= water and machine['milk'] >= milk and machine['beans'] >= beans and cups > 0:
        print('I have enough resources, making you a coffee!')
        return True
    else:
        print(f'Sorry, not enough!')
        return False


def take():
    print(f"I gave you ${machine['money']}")
    print(' ')
    machine['money'] = 0


def status():
    print("The coffee machine has:")
    print(f"{machine['water']} ml of water")
    print(f"{machine['milk']} ml of milk")
    print(f"{machine['beans']} g of beans")
    print(f"{machine['cups']} disposable cups")
    print(f"${machine['money']} of money")
    print(' ')


def fill():
    print('Write how many ml of water you want to add:')
    water = int(input())
    print('Write how many ml of milk you want to add:')
    milk = int(input())
    print('Write how many grams of coffee beans you want to add:')
    beans = int(input())
    print('Write how many disposable cups of coffee you want to add:')
    cups = int(input())
    machine['water'] = machine['water'] + water
    machine['milk'] = machine['milk'] + milk
    machine['beans'] = machine['beans'] + beans
    machine['cups'] = machine['cups'] + cups


def espresso():
    water = 250
    milk = 0
    beans = 16
    cups = 1
    cost = 4
    if check(water, milk, beans, cups):
        machine['water'] = machine['water'] - water
        machine['milk'] = machine['milk'] - milk
        machine['beans'] = machine['beans'] - beans
        machine['cups'] = machine['cups'] - cups
        machine['money'] = machine['money'] + cost


def latte():
    water = 350
    milk = 75
    beans = 20
    cups = 1
    cost = 7
    if check(water, milk, beans, cups):
        machine['water'] = machine['water'] - water
        machine['milk'] = machine['milk'] - milk
        machine['beans'] = machine['beans'] - beans
        machine['cups'] = machine['cups'] - cups
        machine['money'] = machine['money'] + cost


def cappuccino():
    water = 200
    milk = 100
    beans = 12
    cups = 1
    cost = 6
    if check(water, milk, beans, cups):
        machine['water'] = machine['water'] - water
        machine['milk'] = machine['milk'] - milk
        machine['beans'] = machine['beans'] - beans
        machine['cups'] = machine['cups'] - cups
        machine['money'] = machine['money'] + cost


def main():
    while True:
        action = input('Write action (buy, fill, take, remaining, exit):\n',)
        if action == 'buy':
            print('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino , back - to main menu:')
            type_of_coffee = input()
            if type_of_coffee == '1':
                espresso()
            if type_of_coffee == '2':
                latte()
            if type_of_coffee == '3':
                cappuccino()
            if type_of_coffee == 'back':
                continue
        if action == 'fill':
            fill()
        if action == 'take':
            take()
        if action == 'remaining':
            status()
        if action == 'exit':
            break


if __name__ == '__main__':
    main()
