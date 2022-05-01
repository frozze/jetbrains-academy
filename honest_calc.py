# write your code here


msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"
msg_10 = "Are you sure? It is only one digit! (y / n)"
msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"
msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"


def check_oper(x, oper, y):
    try:
        result = 0
        if oper == "+":
            result = float(x) + float(y)
            return result
        elif oper == "-":
            result = float(x) - float(y)
            return result
        elif oper == "/":
            result = float(x) / float(y)
            return result
        elif oper == "*":
            result = float(x) * float(y)
            return result
        else:
            return msg_2
    except ZeroDivisionError:
        return msg_3


def check(v1, v2, v3):
    msg = ""
    if is_one_digit(v1) and is_one_digit(v3):
        msg = msg + msg_6
    if v1 == 1 or v3 == 1 and v2 == "*":
        msg = msg + msg_7
    if (v1 == 0 or v3 == 0) and (v2 == "*" or v2 == "+" or v2 == "-"):
        msg = msg + msg_8
    if msg != "":
        msg = msg_9 + msg
    return msg


def is_one_digit(v):
    if v > -10 and v < 10 and v.is_integer():
        return True
    else:
        return False


def calc():
    memory = 0
    while True:
        try:
            print(msg_0)
            user_input = list((input().split()))
            x = user_input[0]
            oper = user_input[1]
            y = user_input[2]
            if x == "M":
                x = memory
            if y == "M":
                y = memory
            print(check(float(x), oper, float(y)))

            calc_result = check_oper(x, oper, y)
            print(calc_result)

            if isinstance(calc_result, float):
                print(msg_4)
                answ = input()
                if answ == "y":
                    if is_one_digit(calc_result):
                            print(msg_10)
                            answ11 = input()
                            if answ11 == answ:
                                print(msg_11)
                                answ12 = input()
                                if answ12 == answ11:
                                    print(msg_12)
                                    answ13 = input()
                                    if answ13 == answ12:
                                        memory = check_oper(x, oper, y)
                    else:
                        memory = check_oper(x, oper, y)
                else:
                    pass
            else:
                continue

            print(msg_5)
            answer = input()
            if answer == "y":
                continue
            else:
                break

        except ValueError:
            print(msg_1)
            continue


calc()
