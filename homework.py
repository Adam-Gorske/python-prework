# Question 1
# Write a function to print "hello_USERNAME!" USERNAME is the input of the function. The first line of the code has been defined as below.

def hello_name(user_name):
    """print hello_USERNAME"""
    user_name = input("What is your username? ")
    print(f"hello_{user_name.upper()}!")


hello_name('user_name')


# Question 2
# Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing

def first_odds():
    """print odd numbers from 1-100"""
    current_number = 0
    while current_number < 100:
        current_number += 1
        if current_number % 2 == 0:
            continue

        print(current_number)


first_odds()


Question 3
Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined as below.


def max_num_in_list(a_list):
    """return max number of a given list"""


a_list = [100, 23, 2444, 4, 249093]
print(max(a_list))


# Question 4
# Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. The return should be boolean Type (true/false).

def is_leap_year(a_year):
    """is the year a leap year?"""
    year = int(input("Enter a year to see if it's a leap year! "))

    if year % 4 == 0:
        print("True")
    elif year % 100 == 0:
        print("True")
    elif year % 400 == 0:
        print("True")
    else:
        print("False")


is_leap_year('a_year')


# Question 5
# Write a function to check to see if all numbers in list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean Type.

def is_consecutive(a_list):
    """check to see if all numbers are consecutive"""
    return sorted(a_list) == list(range(min(a_list), max(a_list)+1))


sorted_list = [2, 3, 4, 5, 6, 7]
not_sorted_list = [1, 2, 4, 5]
print(is_consecutive(sorted_list))
print(is_consecutive(not_sorted_list))
