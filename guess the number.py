import random
number=random.randint(1,10)
player_name = input ("hello,what is your name?")
number_of_guesses=0
print("okay! "+player_name + " I am guessing a number between 1 to 10:")
while number_of_guesses <5:
  guess=int(input())
  number_of_guesses+=1
  if guess<number:
    print("your guess is too low")
  if guess>number:
    print("your number is too high")
  if guess==number:
    break
if guess==number:
  print("you have guessed the number in " + str(number_of_guesses) + ' tries')
else:
  print("You did not guess the number it was " + str(number))