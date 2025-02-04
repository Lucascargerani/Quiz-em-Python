from colorama import init, Fore

init()

print("Seja muito bem vindo ao Quiz do Ale!")
answer_user = input("Quer começar? (S/N) ").upper()
print(answer_user)

if answer_user != "S":
    quit()

print("Começando...\n")
print(Fore.YELLOW + "Quem desenvolveu o jogo Grand Theft Auto (GTA)? \n" + Fore.WHITE + " (A) Rockstar Games \n (B) Ubisoft \n (C) Activision \n (D) EA \n")
answer1 = input("Resposta: ").upper()

if answer1 == "A":
    print(Fore.GREEN + "Correto!\n" + Fore.WHITE)
else: 
    print(Fore.RED + "Incorreto\n" + Fore.WHITE)

print(Fore.YELLOW + "Qual o nome do protagonista do jogo GTA San Andreas?\n" + Fore.WHITE + " (A) Carlos John\n (B) Carl Johnson\n (C) Carl Jaqueline\n (D) Carlos Jonhson")
answer2 = input("Resposta: ").upper()

if answer2 == "B":
    print(Fore.GREEN + "Correto!\n" + Fore.WHITE)
else: 
    print(Fore.RED + "Incorreto\n" + Fore.WHITE)