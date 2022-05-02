from math import ceil, log, floor
import argparse

parser = argparse.ArgumentParser(description="Loan calculator")

parser.add_argument("--type", action='store', choices=["annuity", "diff"], help="Action type")
parser.add_argument("--principal", type=int, action='store')
parser.add_argument("--periods", type=int, action='store')
parser.add_argument("--payment", type=int, action='store')
parser.add_argument("--interest", type=float, action='store')
args = parser.parse_args()


def annuity():
    try:
        if args.type == "annuity" and args.principal and args.periods and args.interest:
            interest_rate = args.interest / (12 * 100)
            payment = ceil(args.principal * ((interest_rate * (1 + interest_rate) ** args.periods) /
                                             ((1 + interest_rate) ** args.periods - 1)))
            overpayment = (payment * args.periods) - args.principal
            print(f'Your annuity payment = {payment}!')
            print(f'Overpayment = {overpayment}')

        if args.type == "annuity" and args.payment and args.periods and args.interest:
            interest_rate = args.interest / (12 * 100)
            loan_principal2 = \
                floor(args.payment / ((interest_rate * (1 + interest_rate)
                                       ** args.periods) / ((1 + interest_rate) ** args.periods - 1)))
            overpayment = ceil((args.payment * args.periods) - loan_principal2)
            print(f'Your loan principal = {loan_principal2}!')
            print(f'Overpayment = {overpayment}')
        if args.type == "annuity" and args.principal and args.payment and args.interest:
            interest_rate = args.interest / (12 * 100)
            months = log((args.payment / (args.payment - interest_rate * args.principal)), interest_rate + 1)
            overpayment = (args.payment * ceil(months)) - args.principal
            years = int(months // 12)
            month = ceil(months % 12)
            if ceil(months) % 12 != 0:
                print(f'It will take {years} years and {month} months to repay this loan')
            if month == 12:
                years = years + 1
                print(f'It will take {years} years to repay this loan')
            print(f'Overpayment = {overpayment}')
        else:
            print('Incorrect parameter')
    except TypeError:
        print('Incorrect parameter')


def differ():
    try:
        count = 0
        for i in range(1, args.periods + 1):
            interest_rate = args.interest / (12 * 100)
            differ = args.principal / args.periods + interest_rate * (args.principal - args.principal * (i-1) /
                                                                      args.periods)
            print(f'Month {i} payment is {ceil(differ)}')
            count += ceil(differ)
        overpayment = count - args.principal

        print(f'Overpayment = {overpayment}')
    except TypeError:
        print('Incorrect parameter')


if args.type == "diff":
    differ()
if args.type == "annuity":
    annuity()

