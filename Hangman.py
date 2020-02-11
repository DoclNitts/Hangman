import random

def get_guess():
  
 
  dashes = "-" * len(hidden_word)
  guesses_left = 10
  
 
  while guesses_left > -1 and not dashes == hex:
    
  
    print(dashes)
    print (str(guesses_left))
    
    guess = input("Guess:")
    
  
    if len(guess) != 1:
      print ("One character at a time.")     
    elif guess in hidden_word:
      print ("That letter is in the secret word!")
      dashes = update_dashes(hidden_word, dashes, guess)      
    else:
      print ("That letter is not in the secret word!")
      guesses_left -= 1
    
  if guesses_left < 0:
    print ("You lose. The secret word was: " + str(hidden_word))
  

  else:
    print ("You win. The secret word was: " + str(hidden_word))
    
def update_dashes(hidden, cur_dash, rec_guess):
  result = ""
  
  for i in range(len(hidden)):
    if hidden[i] == rec_guess:
      result = result + rec_guess    
      
    else:

      result = result + cur_dash[i]
      
  return result

words = ["omega", "silent", "solitude", "hangman", "chef", "world", "expectation", "order", "intel", "amd"]

hidden_word = random.choices(words)
get_guess()
