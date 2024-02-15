# loop control statements = change a loops execution from its normal sequence

# break =       used to terminate the loop entirely
# continue =    skips to the next iteration of the loop
# pass =        does nothing, acts as a placeholder

# while True:
#     name = input("enter your name: ")
#     if name != "":  # != means don't equal
#         break  # breaks the loop if user types something, terminates the loop
# phone_number = '123-456-7890'
# for i in phone_number:  # for each character in our number we check
#     if i == "-":  # if checked number is a dash skip to the next iteration of the loop
#         continue
#     print(i, end="")  # prints every character and end prevents from moving to the next row

for i in range(1, 21):  # remember that last digit is exclusive (21)

    if i ==13:
        pass  # acts as a placeholder and won't do anything
    else:
        print(i)  # prints every number and skips 13 because of pass control statement



