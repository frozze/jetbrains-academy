from math import ceil, log
import argparse
print('What do you want to calculate?')
print('type "n" - for number of monthly payments,')
print('type "a" for annuity monthly payment amount')
print('type "p" - for the monthly payment:')
answer = input()
if answer == "n":
    print('Enter the loan principal:')
    loan_principal = int(input())
    print('Enter your monthly payment:')
    m_payment = int(input())
    print('Enter the loan interest:')
    loan_interest = float(input())
    interest_rate = loan_interest / (12 * 100)
    months = log((m_payment / (m_payment - interest_rate * loan_principal)), interest_rate + 1)
    years = int(months // 12)
    month = ceil(months % 12)
    if months % 12 != 0:
        print(f'It will take {years} years and {month} months to repay the loan')
    if month == 12:
        years = years + 1
        print(f'It will take {years} months to repay the loan')
        
if answer == "p":
    print("Enter the annuity payment:")
    annuity_payment = float(input())
    print("Enter the numer of periods:")
    m_number = int(input())
    print('Enter the loan interest:')
    loan_interest = float(input())
    interest_rate = loan_interest / (12 * 100)
    loan_principal2 = round(annuity_payment / ((interest_rate * (1 + interest_rate) ** m_number) / ((1 + interest_rate)
                                                                                                    ** m_number - 1)))
    print(f'Your loan principal = {loan_principal2}!')

if answer == "a":
    print('Enter the loan principal:')
    loan_principal = int(input())
    print("Enter the numer of periods:")
    m_number = int(input())
    print('Enter the loan interest:')
    loan_interest = float(input())
    interest_rate = loan_interest / (12 * 100)
    payment = ceil(loan_principal * ((interest_rate * (1 + interest_rate) ** m_number) /
                                     ((1 + interest_rate) ** m_number - 1)))
    print(f'Your monthly payment = {payment}!')
