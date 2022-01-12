import random
from typing import Counter
jackpot = random.randint(1,100)
guess = int(input("Guess the lucky number"))
Counter = 1
while guess != jackpot:
  if guess < jackpot:
    print("Guess higher")
  else: 
    print("Guess lower")
  guess = int(input("Take another shot"))   
  Counter += 1
print("Bingo!!")
print("you took", Counter, "attempts")
