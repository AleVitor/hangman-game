import time
import random
def validateNumberWord(letterU):
  return letterU.isalpha()

win = False
lose = False
attempts = 5
nickname = input('What\'s your nickname? ')
letterL = []
time.sleep(0.5)

while nickname == '':
  nickname = input('[ERROR: Empty Input!] What\'s your nickname? ')
  time.sleep(0.5)


print(20*'-=')
print(f'Welcome to hangman game, {nickname}!!!')
print(20*'-=')
time.sleep(0.5)

randomWord = random.choice(['apple', 'dog', 'blue', 'table', 'happy', 'mountain', 'flower', 'computer', 'sun', 'book',
              'water', 'friend', 'city', 'tree', 'sky', 'music', 'school', 'red', 'cat', 'family',
              'run', 'beach', 'coffee', 'smile', 'car', 'summer', 'love', 'door', 'work', 'green',
              'phone', 'time', 'food', 'dance', 'park', 'dream', 'sleep', 'star', 'bird', 'game',
              'ocean', 'watch', 'pen', 'baby', 'shoe', 'cloud', 'film', 'road', 'money'])

while True:
    #hangman-game
    for letter in randomWord:
      if letter.lower() in letterL:
        print(letter, end=' ')
      else:
        print('_', end=' ')
        
  #validation of letter
    letterU = str(input('Choose a one letter: '))
    while letterU in letterL:
      letterU = str(input('[ERROR: You already chose that letter!] Choose other letter: '))
    while not validateNumberWord(letterU):
      letterU = str(input('[ERROR: Nuber/Empty Input!] Choose a one letter: '))
    letterU = letterU[0]
    
  #validation of word
    letterL.append(letterU.lower())
    if letterU.lower() not in randomWord.lower():
      attempts -= 1
    print(f'You have {attempts} attempt(s).')
    print(f'Last words: {letterL}')
    time.sleep(0.5)
    
    win = True
    for letter in randomWord:
      if letter.lower() not in letterL:
        win = False
    
    if attempts == 0 or win:
      break

#messages
if win == True:
  print(f'The correct word is {randomWord}. You won!!')

if attempts == 0:
  print(f'The correct word is {randomWord}. You lost!!')