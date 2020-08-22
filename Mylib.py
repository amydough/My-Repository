# Program name     : Mylib.py
# Student Name     : Amy Dougherty
# Course           : ENTD220
# Instructor       : Robert Haluska
# Date             : August 20, 2020
# Description      : Class created to hold mathematical operation methods
# Copy Wrong       : This is my work

# defining class for customized exception to check for range
class OutOfRangeError(Exception):
    pass

# defining class for customized exception to check for
# lower range < higher range
class LowerTooHighError(Exception):
    pass

# defining class for customized exception to
# check for a math operation to be selected
class NotAnOperationError(Exception):
    pass

# Defining a class to hold the math operations for a calculator
class Operations:

    # defining methods in Operations class to add, subtract,
    # multiply, divide, and output all of the above
    def add(self, a, b):
        addSum = float(a) + float(b)
        return addSum

    def subtract(self, a, b):
        diff = float(a) - float(b)
        return diff

    def multiply(self, a, b):
        product = float(a) * float(b)
        return product

    def divide(self, a, b):
        a = float(a)
        b = float(b)
        # exception handling divide by 0
        try:
            quotient = a / b
        except ZeroDivisionError:
            return
        else:
            return quotient

    def allInOne(self, a, b):
        # create a method that returns results of 4 operations in dictionary
        adding = self.add(a, b)
        subt = self.subtract(a, b)
        mult = self.multiply(a, b)
        div = self.divide(a, b)
        res = {"add" : adding,
               "subtract" : subt,
               "multiply" : mult,
               "divide" : div}
        return res

    def scalc(self, p1):
        a = p1[0]
        b = p1[1]
        c = p1[2]
        # variable assigned to dictionary method to retrieve values
        answer = self.allInOne(a, b)
        if c == "1":
            print("The result of", a, "+", b, "=", answer["add"])
        elif c == "2":
            print("The result of", a, "-", b, "=", answer["subtract"])
        elif c == "3":
            print("The result of", a, "*", b, "=", answer["multiply"])
        elif c == "4":
            # check for divide by zero and display error cleanly
            if answer["divide"] == None:
                print("You cannot divide by zero")  # output for divide by zero error
            else:
                print("The result of", a, "/", b, "=", answer["divide"])
        elif c == "5":
            # check for divide by zero and display error cleanly
            if answer["divide"] == None:
                print("{0} + {1} = {2}\n"
                      "{0} - {1} = {3}\n"
                      "{0} * {1} = {4}\n"
                      "{0} / {1} = You cannot divide by zero".format(a, b, answer["add"], answer["subtract"],
                                                                     answer["multiply"]))
            else:
                print("{0} + {1} = {2}\n"
                      "{0} - {1} = {3}\n"
                      "{0} * {1} = {4}\n"
                      "{0} / {1} = {5}".format(a, b, answer["add"], answer["subtract"],
                                               answer["multiply"], answer["divide"]))
