"""
Write a function that takes in two numbers from the user via input(),
call the numbers a and b, and then returns the value of squared a divided
by b, construct a try-except block which raises an exception if the two
values given by the input function were not numbers, and if value b was zero
(cannot divide by zero).
"""
a = input("Enter first num: ")
b = input("Enter secound num: ")


def numb():
    try:
        res = (float(a) ** 2) / float(b)
        return print(res)
    except ZeroDivisionError:
        print("You can`t divide by zero")
    except ValueError:
        print("You can`t input str")

numb()
