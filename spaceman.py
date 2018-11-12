#importing random and time module
from time import sleep
import random

#list of guessed letters
guessed_letters =[]

#asks user their name
def user_rules():
  name = input("What is your name?: ")
  print("Hello {}! Are you ready to play Spaceman?".format(name))
  print("There is a secret word.\n You get seven guesses to figure out the letters in the word before you lose. \nGood luck!")
  sleep(2)

#the word is randomly chosen and loaded from the dictionary
def load_word():
  dictonary = {
   "Colors": ["Blue", "Red", "White"],
   "Animals": ["Dog", "Bird", "Lion"] 
  }
  categories = ["Colors", "Animals"]
  categories_index = random.randint(0, 1)
  word = random.randint(0, 2)
  secret_word = dictonary[categories[categories_index]][word]
  return secret_word

secret_word = load_word().lower()

def game_over(reset):
  answer = input("Game over! Would you like to play again? (Y/N): ").lower()
  if answer == 'y':
    reset()
  elif answer != 'y' or answer != 'n':
    print("Invalid input")
    game_over(reset)
  else:
    print("See you next time!")
    return False

def user_guess():
    answer = input("Guess a letter!: ")
    if len(answer) > 1 or not answer.isalpha() or answer == "":
        print("Not a valid guess! Try again")
        user_guess()
    else:
        return answer

def letter_dashes():
  dashes = "_" * (len(secret_word))
  return list(dashes)


guessed_letters = []
def guessed_letters_list():
  print("List of Guessed Letters: {}".format(guessed_letters))

def right_guess(guess, guesses):
  print("{} was in the word! You have {} left.".format(guess, guesses))

  

def win_guess():
  print("Good job! The word was {}".format(secret_word))

def wrong_guess(letter, guesses_left):
  print("{} is wrong. You have {} guesses left.".format(letter, guesses_left))


def game():
  user_rules()
  guesses_left = 7
  dashes = letter_dashes()
  print(((" ").join(dashes)))
  correct_guess = []

  game_on = True

  while game_on:
    letter = user_guess()
    guessed_letters_list()
  

    if letter in secret_word:
      dashes[secret_word.index(letter)] = letter
      right_guess(letter, guesses_left)
      print(dashes)
      correct_guess.append(letter)
      if len(secret_word) == len(correct_guess):
        win_guess()
        game_over(game)
    elif letter not in secret_word:
      guesses_left -= 1
      wrong_guess(letter, guesses_left)
      guessed_letters.append(letter)
      if guesses_left == 0:
        game_over(game)
    else:
      print("Try Again")


  

 



def test():
  game()

test()
