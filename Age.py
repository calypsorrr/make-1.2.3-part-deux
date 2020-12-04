#!/usr/bin/env python


"""
Age.py: How to calculate age.
"""

import time

__author__ = "Bo Claes"
__email__ = "bo.claes@student.kdg.be"
__status__ = "Development"


YEAR = 2020                                                                   # this will be used for a calculation
x = 50                                                                        # this will be used for a calculation


def use_year():
     print("The year you where born in is "+str(int(YEAR)-int(age)))              # printing when he was born

def use_year_50():
    print("The year when you turn 50 is "+str(int(YEAR)-int(age)+int(x)))         # printing the year when you become 50

def user_age():
    global age
    try:                                             # try and except functions for detecting an error
        age = int(input("How old are you user? "))
    except ValueError as err:
        print(err)
        time.sleep(2)
        print("\n")
        user_age()


def restart():
    # Asking the user if he want to end it here or want to go again with different inputs or not
    print("\n")
    print("Do you want to continue with the same age or you want to put another in? ")
    print("1. change age")
    print("2. the same age")
    print("3. exit")

    restart = input()

    if restart == "1":
        main_change_age()
    elif restart == "2":
        main_no_change()
    else:
        exit()



def main_change_age():
    user_age()
    print("\n")
    print("Which one do you want to know? ")
    print("\n")
    print("1. The year you where born in? ")
    print("2. The year when you turn 5O? ")

    user_1 = input()

    if user_1 == "1":
        use_year()

    elif user_1 == "2":
        use_year_50()

    restart()

def main_no_change():
    print("\n")
    print("Which one do you want to know? ")
    print("\n")
    print("1. The year you where born in? ")
    print("2. The year when you turn 5O? ")

    user_1 = input()

    if user_1 == "1":
        use_year()

    elif user_1 == "2":
        use_year_50()

    restart()

if __name__ == '__main__':  # code to execute if called from command-line
    main_change_age()
