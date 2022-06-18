# write your code here
import random


class TestCalc:
    def __init__(self):
        self.count = 0
        self.mark = 0
        self.fist_digit = 0
        self.second_digit = 0
        self.action = ''

    def hard_test(self):
        while self.count != 5:
            self.fist_digit = random.randrange(11, 30)
            result = self.fist_digit * self.fist_digit
            print(self.fist_digit)
            if self.user_input(result) is True:
                self.mark += 1
            self.count += 1
        print(f'Your mark is {self.mark}/5.')

    def simple_test(self):
        while self.count != 5:
            self.fist_digit = random.randrange(2, 10)
            self.second_digit = random.randrange(2, 10)
            self.action = random.choice('*-+')
            if self.action == '*':
                result = self.fist_digit * self.second_digit
                print(self.fist_digit, self.action, self.second_digit)
                if self.user_input(result) is True:
                    self.mark += 1
            if self.action == '-':
                result = self.fist_digit - self.second_digit
                print(self.fist_digit, self.action, self.second_digit)
                if self.user_input(result) is True:
                    self.mark += 1
            if self.action == '+':
                result = self.fist_digit + self.second_digit
                print(self.fist_digit, self.action, self.second_digit)
                if self.user_input(result) is True:
                    self.mark += 1
            self.count += 1
        print(f'Your mark is {self.mark}/5.')

    def user_input(self, result):
        try:
            user_inp = int(input())
            if result == user_inp:
                print('Right!')
                return True
            else:
                print('Wrong!')
                return False
        except ValueError:
            print('Incorrect format.')
            if self.user_input(result) is True:
                self.mark += 1

    def user_choice(self):
        lst = ['yes', 'YES', 'y', 'Yes']
        try:
            print('Which level do you want? Enter a number:')
            print('1 - simple operations with numbers 2-9')
            print('2 - integral squares of 11-29')
            user_choice = int(input(''))
            if user_choice == 1:
                self.simple_test()
                choice = input('Would you like to save your result to the file? Enter yes or no.\n')
                if choice in lst:
                    file = open('results.txt', 'a')
                    name = input('What is your name?\n')
                    file.write(f'{name}: {self.mark}/5 in level {user_choice} (simple operations with numbers 2-9)')
                    print('The results are saved in "results.txt".')
                if choice == 'no':
                    exit()

            if user_choice == 2:
                self.hard_test()
                choice = input('Would you like to save your result to the file? Enter yes or no.\n')
                if choice in lst:
                    file = open('results.txt', 'a')
                    name = input('What is your name?\n')
                    file.write(f'{name}: {self.mark}/5 in level {user_choice} (integral squares operations with numbers 11-29)')
                    print('The results are saved in "results.txt".')
                if choice == 'no':
                    exit()
        except ValueError:
            print('Incorrect format.')

    def save_progress(self):
        pass


calculator = TestCalc()
calculator.user_choice()
