#importing time module
import time

#importing random
import random

#list of guessed letters
guessed_letters =[]

#asks user their name
def user_name():
  name = input("What is your name?: ")
  print("Hello {}! Are you ready to play Spaceman?".format(name))

#dramatic pause before the game begins
time.sleep(1)

#the word is randomly chosen and loaded from the file
def load_word():
  with open("words.txt","r") as file:
    words = file.readlines()
    word = random.choice(words)
    return word

def user_guess():
  letter = input("Guess a letter!: ")
  if len(letter) > 1:
    print("Not a valid guess! Try again")
    user_guess()
  elif not letter.isalpha():
    print("Not a valid guess! Try again")
    user_guess()
  elif letter == "":
    print("Not a valid guess! Try again")
    user_guess()

  return letter

def letter_dashes():
  word = load_word()
  dashes = " _ " * (len(word))
  return dashes

def get_guess():
  word = load_word()
  dashes = letter_dashes()
  guesses_left = 7
  while guesses_left > -1 and dashes != word:
    print(dashes)
    print(str(guesses_left))
    guess = user_guess()
    if guess in word:
      print ("That letter is in the word!")
      dashes = update_dashes()
    else:
      print("That letter is incorrect!")
      guesses_left -= 1
    
    if guesses_left < 0:
      print ("You lose! The word was: " + str(word))
    
    else:
      print ("Good Job!")
def update_dashes ():
  word = load_word()
  guess = user_guess()
  dash = letter_dashes()
  result = ""

  for i in range (len(word)):
    if word[i] == guess:
      result = result + guess

    else:
      result = result + dash[i]
  
  return result

  
  

 




def main():
  user_name()
  # load_word()
  # letter_dashes()
  get_guess()
  update_dashes()
  



# #test rounds
# for _ in list(range(1,5)):
#   letter_dashes()
#   guess_letter()

main()
