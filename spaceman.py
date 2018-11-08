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

def game_over(start_over):
  answer = input("Game over! Would you like to play again? (Y/N): ").lower()
  if answer == 'y':
    start_over()
  elif answer != 'y' or answer != 'n':
    print("Invalid input")
    game_over(start_over)
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


# guessed_letters = []
def guessed_letters_list():
  return "These are the letters you already guessed: {}".format(guessed_letters)

def right_guess():
  print("{} was in the word! +\n{}".format(user_guess(), guessed_letters_list()))

  

def win_guess():
  print("Good job! The word was {}".format(secret_word))

def wrong_guess():
  print("{} is wrong. Try again.\n{}".format(user_guess(), guessed_letters_list()))

# def guess_message():
  # print("You have already guessed{}. Try again\n{}".format(guessed_letters_list(), )

def game():
  user_rules()
  guesses_left = 7
  dashes = letter_dashes()
  print(dashes)

  correct_guess = []

  while guesses_left > -1 and dashes != secret_word:
    letter = user_guess()
    if guesses_left == 0:
      game_over(game)

    if letter in guessed_letters:
      guesses_left -= 1
      guessed_letters_list()
    
    elif letter in secret_word:
      right_guess()
      dashes[secret_word.index(letter)] = letter
      print(dashes)
      guessed_letters_list()
    
    elif correct_guess in guessed_letters:
      win_guess()
    

    else:
      guesses_left -= 1
      guessed_letters.append(letter)
      wrong_guess()


  

 



def test():
  game()

test()
