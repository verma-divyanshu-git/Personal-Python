import random
from typing import Counter
jackpot = random.randint(1,100)
guess = int(input("chal guess kar ab"))
Counter = 1
while guess != jackpot:
  if guess < jackpot:
    print("guess higher")
  else: 
    print("guess lower")
  guess = int(input("chal guess kar ab"))   
  Counter += 1
print("sahi jawab!!")
print("you took", Counter, "attempts")