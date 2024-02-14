# if statement = block fo code that will execute if it's condition is true

age = int(input("How old are you?: "))
# order of if statements matter
if age == 100:  # if a value is equal to a particular value use == (comparison operator  for equality)
    print("You are a century old!")
elif age >= 18:  # if statements works from top to bottom if first is false then second then third
    print("you are an adult!")  # if the condition is true perform this
elif age < 0:
    print("you haven't been born yet!")  # if the condition is true perform this
else:
    print("You are a Child!")  # if the conditions above are false perform this



