import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

user_choice = ["pedra", "papel", "tesoura"]
print("Bem vindo ao Rock, Paper, Scissors!")
username = input("Qual seu nome? \n")
print(f"Bem vindo(a), {username}")
user_choice = input("Qual sua escolha? Pedra, papel ou tesoura? \n").lower()

if user_choice == "pedra":
    print(rock)

elif user_choice == "papel":
    print(paper)

elif user_choice == "tesoura":
    print(scissors)

else:
    print("Você não escolheu uma opção válida.")

pc_play = ["pedra", "papel", "tesoura"]
x = len(pc_play)
pc_random = random.randint(0, x - 1)
pc_choice = pc_play[pc_random]

if pc_choice == "pedra":
    print(rock)

if pc_choice == "papel":
    print(paper)

if pc_choice == "tesoura":
    print(scissors)

print(f"Você escolheu {user_choice} e seu oponente escolheu {pc_choice}." )

if (user_choice == "pedra") and (pc_choice == "pedra"):
    print("Deu Empate!")
elif (user_choice == "papel") and (pc_choice == "papel"):
    print("Deu Empate!")
elif (user_choice == "tesoura") and (pc_choice == "tesoura"):
    print("Deu Empate!")
elif ((user_choice == "pedra") and (pc_choice == "papel")) or ((user_choice == "papel") and (pc_choice == "tesoura")) or ((user_choice == "tesoura") and (pc_choice == "pedra")):
    print("Você perdeu!")
else:
    print("Parabéns! Você venceu!")
