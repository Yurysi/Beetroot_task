"""
Task 1

Write a function called oops that explicitly raises an IndexError exception
when called. Then write another function that calls oops inside a try/except
statement to catch the error. What happens if you change oops to raise
KeyError instead of IndexError?
"""

def oops(index):
    a = ['a', 'b', 'c', 'd', 'e']
    b = {1: 'aa', 2: 'bb', 3: 'cc'}
    try:
        print('In list attribute: ', a[index], '\n')
        print('In dict value attribute: ', b[index])
    except IndexError:
        print("wrong index\nSomething dropped(")
    except KeyError:
        print("wrong index for dict\nSomething dropped(")
    return


def index_func():
    # a = ['a', 'b', 'c', 'd']
    try:
        index = int(input(" Enter index: "))
        oops(index)
    except (ValueError, TypeError):
        print("wrong value+\nSomething dropped(")


index_func()
