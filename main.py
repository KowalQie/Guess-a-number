#Clear function
from replit import clear
#Import LOGO
import art
print(art.logo)
#Import random
import random


#FUNCTIONS
def number_choice(number):
  """Zwraca liczbę z zakresu od 1 do 100"""
  # Pętla dla liczb od 1 do 100
  for element in range(1, 101):
    number.append(str(element))
  # Wybór losowej liczby z zakresu od 1 do 100
  random_number = int(random.choice(number))
  return random_number


replay = True
while replay:

  #VARIABLES
  number_of_lifes = 0
  number = []
  
  #START
  random_number = number_choice(number)

  #TESTING
  #print(f"For testing. The solution is {random_number}.")
  
  #CHOOSE THE LEVEL OF GAME
  level = input("Your goal is to guess a number from 1 to 100. Choose the 'hard' or 'easy' level.\n")
  if level == 'easy':
    print("You have 10 attempts remaining to guess the number.")
    number_of_lifes = 10
  elif level == 'hard':
    print("You have 5 attempts remaining to guess the number.")
    number_of_lifes = 5

  game = True
  while number_of_lifes > 0 and game == True:
  
    #WYBÓR LICZBY PRZEZ GRACZA
    guess = input("Choose the number from 1 to 100.\n")
    guess = int(guess)
    
    #STATEMENTS   
    if guess != random_number:
      number_of_lifes -= 1
      if guess > random_number:
        print(f"The number is too high. You have {number_of_lifes} lifes left.")
      elif guess < random_number:
        print(f"The number is too low. You have {number_of_lifes} lifes left.")
    else: # guess == random_number:
      print("You have guessed the number. You win.")
      correct = input("Do you want to replay?\n")
      if correct == "yes":
        clear()
        game = False
        replay = True
      else:
        clear()
        print("I hope you will be back soon. Bye bye.")
        game = False
        replay = False
  
  while number_of_lifes == 0 and game == True:
    print("You are out of lifes. Game over.")
    wrong = input("Do you want to play again ?\n")
    if wrong == "yes":
      clear()
      game = False
      replay = True
    else:
      clear()
      print("I hope you will be back soon. Bye bye.")
      game = False
      replay = False

    