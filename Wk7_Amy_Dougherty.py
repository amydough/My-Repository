
# Program name     : Wk7_Amy_Dougherty.py
# Student Name     : Amy Dougherty
# Course           : ENTD220
# Instructor       : Robert Haluska
# Date             : Augus 20, 2020
# Description      : Edit code to instantiate and use Operations class
# Copy Wrong       : This is my work

import Mylib

print("This is my seventh programming assignment.\n")

tryAgain = "Y"  # initializing variable for loop

# loop for user input to continue
while tryAgain == "Y" or tryAgain == "y":

    # Range assignment from user
    print("Enter the range of values between -100 and 100:")

    # Try loop to check input for correct Low range value
    goodLowRange = True
    while goodLowRange:
        try:
            lowRange = input("Enter your lower range ---> ")
            # Check the numbers are between -100 and 100. Throw Exception if true
            if int(lowRange) < -100 or int(lowRange) > 100:
                raise Mylib.OutOfRangeError
        except ValueError:  # Check for int value
            print("You must type a number for the range.")
        except Mylib.OutOfRangeError:  # Exception thrown for range values set <-100 and >100
            print("You entered {}. Enter a number between -100 and 100.".format(lowRange))
        else:
            goodLowRange = False  # Loop stopped if no exceptions found

    # Try loop to check input for correct High range value
    goodHighRange = True
    while goodHighRange:
        try:
            highRange = input("Enter your higher range ---> ")
            # Check the numbers are between -100 and 100. Throw Exception if true
            if int(highRange) < -100 or int(highRange) > 100:
                raise Mylib.OutOfRangeError
            # Check that the lower range < higher range. Throw Exception if true
            elif int(highRange) < int(lowRange):
                raise Mylib.LowerTooHighError
        except ValueError:  # Check for int value
            print("You must type a number for the range.")
        except Mylib.OutOfRangeError:  # Exception thrown for range values set <-100 and >100
            print("You entered {}. Enter a number between -100 and 100.".format(highRange))
        except Mylib.LowerTooHighError:  # Exception thrown for low range > high range
            print("Your lower range number of {0} is higher than your high range number of {1}".format(lowRange, highRange))
        else:
            goodHighRange = False  # Loop stopped if no exceptions found

    # Number assignments from user
    print("\nEnter the numbers you wish to add, subtract, multiply and divide.")

    # Try loop to check for correct input value and if number falls within range for the first number
    goodNum1 = True
    while goodNum1:
        try:
            num1 = input("Enter your first number ---> ")
            # Check if number falls within range
            if int(lowRange) > int(num1) or int(highRange) < int(num1):
                raise Mylib.OutOfRangeError
        # Exception thrown for improper value type
        except ValueError:
            print("You must type a number.")
        # Exception thrown for input out of range
        except Mylib.OutOfRangeError:
            print("You entered, {}. It is outside the range you specified above.".format(num1))
        else:
            goodNum1 = False        # Stop loop when no exception found

    # Try loop to check for correct input value and if number falls within range for the second number
    goodNum2 = True
    while goodNum2:
        try:
            num2 = input("Enter your second number ---> ")
            # Check if number falls within range
            if int(lowRange) > int(num2) or int(highRange) < int(num2):
                raise Mylib.OutOfRangeError
        # Exception thrown for improper value type
        except ValueError:
            print("You must type a number.")
        # Exception thrown for input out of range
        except Mylib.OutOfRangeError:
            print("You entered, {}. It is outside the range you specified above.".format(num2))
        else:
            goodNum2 = False    # Stop loop when no exception found

    # Add a list menu to choose from for math operation

    menu = ["1) Add two numbers",
            "2) Subtract two numbers",
            "3) Multiply two numbers",
            "4) Divide two numbers",
            "5) All math operations"]
    # Display each item in the list like a menu
    for a in menu:
        print(a)

    # Try loop to check for correct input value and if using correct math function
    goodMath = True
    while goodMath:
        try:
            action = input("Enter the number of the operation you wish to perform ---> ")
            # Check if number falls within range
            if int(action) < 6:
                goodMath = False    # Stop loop when no exception found
            else:
                raise Mylib.NotAnOperationError
        # Exception thrown for improper value type
        except ValueError:
            print("You must type a number 1 - 5 from the menu.")
        # Exception thrown for not putting in the required math operation
        except Mylib.NotAnOperationError:
            print("You must enter a math operation\n"
                  "1 for adding\n"
                  "2 for subtracting\n"
                  "3 for multiplying\n"
                  "4 for division\n"
                  "5 for all")

    # combine input to single string
    p1 = [num1, num2, action]

    # instantiate the Operations class
    ops = Mylib.Operations()

    # Use calculation method within Operations class
    ops.scalc(p1)

    # User input to continue?
    tryAgain = input("Do you wish to use the calculator again? Y/N ")
    print("\n")

# final message to inform user end of program
print("Thanks for using our calculator!\n")
