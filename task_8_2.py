"""
    Task 2

    Creating a dictionary.

    Create a function called make_country, which takes in a country’s name
    and capital as parameters. Then create a dictionary from those two,
    with ‘name’ as a key and ‘capital’ as a parameter. Make the function print
    out the values of the dictionary to make sure that it works as intended.
"""
country = input("enter without commas: ").split()
capital = input("Enter capital: ").split()


def make_country(country, capital, *kwargs):
    country_dict = dict(zip(country, capital))
    return print(country_dict)


make_country(country, capital)
