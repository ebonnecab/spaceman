#importing random and time module
import time
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
    words = file.read().splitlines()
    word = random.choice(words)
    return word

word = load_word().lower()


def user_guess():
  letter = input("Guess a letter!: ")
  if len(letter) > 1 or not letter.isalpha() or letter == "":
    print("Not a valid guess! Try again")
    user_guess()
  else:
    return letter

def letter_dashes():
  word = load_word()
  dashes = list( "_" * (len(word)))
  return dashes


def guess_message():
  print("These are the letters you already guessed: {}".format(guessed_letters))

def get_guess():
  dashes = letter_dashes()
  guesses_left = 7
  while guesses_left > -1 and dashes != word:
    print(dashes)
    print(str(guesses_left))
    guess = user_guess()
    if guess in guessed_letters:
      print("You already guessed: {}".format(guess))
    if guess in word:
      print ("That letter is in the word!")
      dashes[word.index(guess)] = guess
      print(dashes)
      guess_message()
    else:
      print("That letter is incorrect!")
      guesses_left -= 1
      guessed_letters.append(guess)
      guess_message()
    if guesses_left == 0:
      print ("You lose! The word was: " + str(word))
    
    else:
      print ("Good Job!")
  

  

 




def main():
  user_name()
  # load_word()
  # letter_dashes()
  get_guess()
  
  



# #test rounds
# for _ in list(range(1,5)):
#   letter_dashes()
#   guess_letter()

main()
