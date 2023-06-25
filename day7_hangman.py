import random
import day7_hangman_wordlist
import day7_hangman_logo


print(day7_hangman_logo.logo)
categoria = input("\nSeja bem vindo(a) ao jogo da forca!\nEscolha uma categoria para jogar:\nFRUTAS, PAÍSES OU ANIMAIS?\nOu, se quiser jogar no modo super difícil em inglês, digite ENGLISH!\n").lower()
if categoria == "frutas":
    categoria = day7_hangman_wordlist.frutas
elif categoria == "paises":
    categoria = day7_hangman_wordlist.paises
elif categoria == "animais":
    categoria = day7_hangman_wordlist.animais
else:
    categoria = day7_hangman_wordlist.english
chosen_word = random.choice(categoria)


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

display = []
letras_chutadas = []
length = len(chosen_word)
lives = 6

#imprimir as quantidade de linhas _
for i in range(length):
    display += "_"
print(display)

#tentativas para adivinhar a palavra

end_of_game = False

while not end_of_game:
    guess = input("Chute uma letra: ").lower()
    for position in range(length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter



    if guess not in chosen_word:
        if guess in letras_chutadas:
            print(f"Você já chutou essa letra e não perdeu uma vida! Até agora você já escolheu as seguintes letras: {letras_chutadas}")

        else:
            lives -= 1
            print(f"Você chutou a letra {guess}, mas ela não contém na palavra. Você perdeu uma vida.")
            letras_chutadas += guess
            if lives == 0:
                end_of_game = True
                print(f"SINTO MUITO... VOCÊ PERDEU O JOGO! A palavra era {chosen_word.upper()} ;(")

    print(display)
    if "_" not in display:
        end_of_game = True
        print("PARABÉNS! VOCÊ VENCEU O JOGO DA FORCA!")
    print(stages[lives])



