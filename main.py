calc = True
num1 = None
num2 = None
while calc:
    try:
        if num1 == None:
            num1 = int(input("Задайте перше число: "))
        if num2 == None:
            num2 = int(input("Задайте друге число: "))
        op = input("Задайте операцію ")

        if op == "+":
            print(num1 + num2)
            num1 = None
            num2 = None
        elif op == "-":
            print(num1 - num2)
            num1 = None
            num2 = None
        elif op == "*":
            print(num1 * num2)
            num1 = None
            num2 = None
        elif op == "/":
            print(num1 / num2)
            num1 = None
            num2 = None
        else:
            print("Невідома операція")
    except ZeroDivisionError:
        print("error: you can't divide by zero")
    except ValueError:
        print("error: You can only enter a number")
    except:
        print("Unknown error")