#Python program to shuffle a deck of card

#importing modules
import itertools, random

#make a deck of cards
deck = list(itertools.product(range(1,14),['Spade', 'Heart', 'Diamond', 'Club']))

#Shuffle the cards
random.shuffle(deck)

#draw five cards
print("You got: ")
for i in range(5):
    print(deck[i][0], "of", deck[i][1])


#Output
You got: 
3 of Heart
11 of Club
12 of Spade
13 of Heart
13 of Spade
