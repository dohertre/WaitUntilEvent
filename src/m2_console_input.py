"""
This module demonstrates lets you practice INPUT from the CONSOLE.

Authors: David Mutchler, Valerie Galluzzi, Mark Hays, Amanda Stouder,
         their colleagues and Rebekah Doherty.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import math

def main():
    """ TESTs the functions in this module (by calling them). """
    # double_a_float()
    # print_an_integer_many_times()
    print_an_integer_many_times_on_one_row()
    input_it_all()


def double_a_float():
    """
    What comes in: Nothing.
    What goes out: Nothing (i.e. None)
    Side effects:
       a. Prompts the user for and inputs a floating point number.
       b. Prints the input number, doubled (i.e., multiplied by 2).
    No input validation is required.  Nothing else should be printed.

    Example:
    Here is a sample run, where the user input is to the right
    of the colon:
         Enter a number: -3.14
         -6.28
    """
    # ------------------------------------------------------------------
    # DONE: 2. Implement and test this function.
    #   The testing code is already written for you (above).
    # ------------------------------------------------------------------
    msg = 'Enter a Floating Point Number'
    x = float(input(msg))
    y = x * 2
    print(y)


def print_an_integer_many_times():
    """
    What comes in: Nothing.
    What goes out: Nothing (i.e. None)
    Side effects:
       a. Prompts the user for and inputs a positive integer.
       b. Prints the input integer, doubled (i.e., multiplied by 2),
          the input number of times.  (See the example.)
    No input validation is required.  Nothing else should be printed.

    Example:
    Here are two sample runs, where the user input is to the right
    of the colon:
         Enter an integer: 3
         6
         6
         6

         Enter an integer: 5
         10
         10
         10
         10
         10
    """
    # ------------------------------------------------------------------
    # DONE: 3. Implement and test this function.
    #   The testing code is already written for you (above).
    # ------------------------------------------------------------------
    msg = 'Enter an Integer'
    x = int(input(msg))
    y = x * 2
    print(y)


def print_an_integer_many_times_on_one_row():
    """
    Same as the previous problem, but print the numbers
    on a single line with no spaces in between them.

    Here are two sample runs, where the user input is to the right
    of the colon:
         Enter an integer: 3
         666

         Enter an integer: 5
         1010101010
    """
    # ------------------------------------------------------------------
    # DONE: 4. Implement and test this function.
    #   The testing code is already written for you (above).
    #
    # HINT: One way to print on a SINGLE line is to build up a string
    #       and then print that (single) string.
    # ------------------------------------------------------------------
    msg = 'Enter an Integer'
    x = int(input(msg))
    y = x * 2
    for k in range(x):
        print(y, end='')


def input_it_all():
    """
    What comes in: Nothing.
    What goes out: Nothing (i.e. None)
    Side effects:
      Prompts the user for and inputs:
        -- A positive floating point number
        -- A positive integer
        -- A string
      in that order (via three separate INPUT statements).
      Then prints, in this order, all on separate lines:
        a. The square root of the floating point number,
           repeated the input integer number of times.
        b. The string, repeated the input integer number of times.
      No input validation is required.  Nothing else should be printed.

    Example:
    Here is a sample run, where the user input is to the right
    of the colons:
         Enter a positive floating point number: 1.44
         Enter a positive integer: 4
         Enter a string: Peace & Love.
         1.2
         1.2
         1.2
         1.2
         Peace & Love.
         Peace & Love.
         Peace & Love.
         Peace & Love.
    """
    # ------------------------------------------------------------------
    # DONE: 5. Implement and test this function.
    #   The testing code is already written for you (above).
    # ------------------------------------------------------------------
    msg1 = 'Enter a Floating Point Number'
    x1 = float(input(msg1))

    msg2 = 'Emter a Positive Integer'
    x2 = int(input(msg2))

    msg3 = 'Enter a String'
    x3 = str(input(msg3))

    y = math.sqrt(x1)
    z = int(x1)
    for k in range(z):
        print(y, end='')

    for h in range(x2):
        print(x3, end='')
# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
