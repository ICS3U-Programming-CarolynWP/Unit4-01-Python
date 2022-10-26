# !/usr/bin/env python3
# Created by: Carolyn Webster Pless
# Created on: 2022/10/26
# Takes the user input for a positive integer and uses
# A while loop to calculate the sum of all numbers from
# 0 to the user input.


def main():

    # Title of the program
    print("Sum of all Numbers")
    counter = 0
    sum = 0

    # User inputs for the integer
    integer_input = input("Enter a positive number: ")

    # Try Catch statement to make sure the input is an integer
    try:
        input_as_integer = int(integer_input)

    # Exception which tells the user to enter an integer
    except Exception:
        print("Your input must be a integer!")

    else:
        # IF statement to make sure the input is positive
        if input_as_integer < 0:
            print("Please enter a POSITIVE integer!")
        else:
            # WHILE loop to calculate the sum of all numbers up to the input
            while counter <= input_as_integer:
                print("{} + ".format(counter))
                sum = counter + sum
                counter = counter + 1
            print("The sum of all numbers is {}".format(sum))


if __name__ == "__main__":
    main()
