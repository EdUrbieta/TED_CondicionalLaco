import random

#Coletando input do usuário ao requisitar quantas tentativas ele deseja ter no jogo
tentativa = int(input("\nOlá! Vamos jogar um jogo de adivinhação? Quantas tentativas você gostaria de ter?: "))

#Obtendo número pseudoaleatório na janela de 1 a 100
n = random.randrange(1, 100)
print("\nVocê tem ", tentativa, " tentativas! Boa sorte!\n")

#Contagem para o número de tentativas
contagem = 0

while contagem < tentativa:
    contagem += 1
    adv = int(input("Tente adivinhar o número: "))

    if adv == n:
        print("Acertou mizerávi! O número é o correto! Conseguistes na ", contagem, " tentativa!")
        break
    elif adv < n:
        print("Tente de novo! O seu número foi muito pequeno!")
    elif adv > n:
        print("Tente de novo! O seu número foi muito grande!")

if contagem >= tentativa:
    print("Você falhou! O número era: ", n, ". Tenha mais sorte da próxima vez!")
