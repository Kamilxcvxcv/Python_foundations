# 2D lists = list of lists

drinks = ["coffe","sode","tea"]
dinner = ["pizza","Hamburbur","Hotdog"]
dessert = ["cake","ice cream"]

# add all of these lists into one list
food = [drinks, dinner, dessert]  # 2D list
# prints all lists
# print(food)
# if you want to access only one list add index to print
# print(food[0])  # prints only list of drinks
# if you want to access only one list and a specific element add another index
print(food[0][0])
