# exceptions = events detected during execution that interrupt the flow of a program
try:  # if you consider the code dangerous surround any code withing a try block
    numerator = int(input("Enter a number to divide: "))
    denominator = int(input("Enter a number to divide by: "))
    result = numerator / denominator
except ZeroDivisionError as e:  # Use specific exception block to handle specific exceptions
    print(e)
    print("You can't divide by zero dummy!")
except ValueError as e:  # it stores the error as e
    print(e)  # you can print for user what type of mistake he's making but it's totally optional
    print("You can divide only number you asshole!")
except Exception as e:  # this part of will catch any exceptions that occur during running of the program
    print(e)
    # and will prevent our program from being interrupted
    print("Something went wrong :(")
else:  # if there are no exceptions we will execute this else statement if not then we won't
    print(result)
finally:  # always at end, whether or not we catch an exception we will execute any code that is within finally block
    print("this will always execute")
# good for closing the files
# it's not a good practice to have one exception block to handle all of the  exceptions
# it's better to handle specific exception when they occur
# dividing by zero will cause a exception, event that interrupts the flow of a program

