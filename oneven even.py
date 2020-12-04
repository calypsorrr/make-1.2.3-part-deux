#!/usr/bin/env python
"""
Info about our project comes here
"""

import time

__author__ = "Bo Claes"
__email__ = "bo.claes@student.kdg.be"
__status__ = "Development"


def user_1():
    global num
    try:                                          # try and except for detecting errors
        num = int(input("Enter a number: "))
    except ValueError as err:
        print(err)
        time.sleep(2)
        print("\n")
        user_1()


# calculating if a number is odd or even
def calculations():
    if (num % 2) == 0:
        print("{0} is a Even number".format(num))
    else:
        print("{0} is a Odd number".format(num))


def restart():
    # Asking the user if he want to end it here or want to go again
    restart = input("Do you want to start again? if so type 'yes' else type 'no' ").lower()
    if restart == "yes":
        print('\n' * 80)
        main()
    else:
        exit()

# main function
def main():
    user_1()
    print("\n")
    calculations()
    print("\n")
    restart()


if __name__ == '__main__':  # code to execute if called from command-line
    main()
