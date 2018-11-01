# import random

# def load_word():
#    f = open('words.txt', 'r')
#    words_list = f.readlines()
#    f.close()

#    words_list = words_list[0].split(' ')
#    secret_word = random.choice(words_list)
#    return secret_word

# def is_word_guessed(secret_word, letters_guessed):
#     '''
#     secretWord: string, the random word the user is trying to guess.  This is selected on line 9.
#     lettersGuessed: list of letters that have been guessed so far.
#     returns: boolean, True only if all the letters of secretWord are in lettersGuessed;
#       False otherwise
#     '''

#     # FILL IN YOUR CODE HERE...

# def get_guessed_word(secret_word, letters_guessed):
#     '''
#     secretWord: string, the random word the user is trying to guess.  This is selected on line 9.
#     lettersGuessed: list of letters that have been guessed so far.
#     returns: string, of letters and underscores.  For letters in the word that the user has
#     guessed correctly, the string should contain the letter at the correct position.  For letters
#     in the word that the user has not yet guessed, shown an _ (underscore) instead.
#     '''
#     # FILL IN YOUR CODE HERE...




# def get_available_letters(letters_guessed):
#     '''
#     lettersGuessed: list of letters that have been guessed so far
#     returns: string, comprised of letters that represents what letters have not
#       yet been guessed.
#     '''




# def spaceman(secret_word):
#     '''
#     secretWord: string, the secret word to guess.
#     Starts up a game of Spaceman in the command line.
#     * At the start of the game, let the user know how many
#       letters the secretWord contains.
#     * Ask the user to guess one letter per round.
#     * The user should receive feedback immediately after each guess
#       about whether their guess appears in the computer's word.
#     * After each round, you should also display to the user the
#       partially guessed word so far, as well as letters that the
#       user has not yet guessed.
#     '''
#     # FILL IN YOUR CODE HERE...


# #
# # secret_word = load_word()
# # spaceman(load_word())


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


time.sleep(1)

def load_word():
  with open("words.txt","r") as file:
    words = file.readlines()
    word = random.choice(words)
    return word

def guess_letter():
  letter = input("Guess a letter!: ")
  if len(letter) > 1:
    print("Not a valid guess! Try again")
  
  elif not letter.isalpha():
    print("Not a valid guess! Try again")

  elif letter == "":
    print("Not a valid guess! Try again")
  
  elif letter == " ":
    print("Not a valid guess! Try again")

  return letter
  
def letter_dashes():
  word = load_word()
  dashes = list("_" * (len(word) - 1))
  return dashes




def main():
  # user_name()
  print(letter_dashes())
  # guess_letter()



# #test rounds
# for _ in list(range(1,5)):
#   letter_dashes()
#   guess_letter()

main()
