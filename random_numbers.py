# will generate some random numbers. To be more specific we will create pseudo-random numbers instead of true-numbers

import random
# generate random numbers between 1 and 6
x = random.randint(1,6)
y = random.random()  # random numbers between 0 and 1
# random choice from a list or other collection
myList = ['rock','paper','scissors']
z = random.choice(myList)
# u can also use a shuffle method to shuffle a list

cards = [1,2,3,4,5,6,7,8,9,'J','Q','K','A']

random.shuffle(cards)

print(cards)


