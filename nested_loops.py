# nested loops =        the "inner loop" will finish all of it's iterations
#                          before finishing one iteration of the "outer loop"


rows = int(input("How many rows?: "))  # input for rows
columns = int(input("How many columns?: "))  # input for columns
symbols = input("enter a symbol to use: ") # input for symbol to use

for i in range(rows):
    for j in range(columns):  # inner loop will iterate as many times as we have columns
        print(symbols, end="")  # end will prevent from moving cursor to the next line while printing
    print() # prints the next line

# in short its concept that one loops is inside another loop inner loop will finish all of its iterations
# before finishing one iteration of outer loop


