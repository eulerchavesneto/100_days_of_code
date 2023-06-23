import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']


#Testing code
print(f'Pssst, the solution is {chosen_word}.')

display = []
length = len(chosen_word)
lives = 6

#imprimir as quantidade de linhas _
for i in range(length):
    display += "_"
print(display)

#tentativas para adivinhar a palavra


end_of_game = False

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    for position in range(length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
        else:
            lives -= 1
            print("Errou!")
    print(display)
    if "_" not in display:
        end_of_game = True
        print("You win!")
    if lives == 0:
        end_of_game = True
        print("You lose!")



