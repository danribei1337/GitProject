
# Desafio Python

import random


def jogo_adivinhacao():
    numero_aleatorio = random.randint(0, 50)
    tentativas_restantes = 10

    print("Bem-vindo ao jogo de adivinhação!")
    print("Tente adivinhar o número que estou pensando entre 0 e 50.")
    print(f"Você tem {tentativas_restantes} chances para acertar.")

    while tentativas_restantes > 0:
        try:
            palpite = int(input("\nDigite seu palpite: "))
            if palpite < 0 or palpite > 50:
                print("Por favor, escolha um número entre 0 e 50.")
                continue

            if palpite == numero_aleatorio:
                print(
                    f"Parabéns! Você acertou! O número era {numero_aleatorio}.")
                break
            elif palpite > numero_aleatorio:
                print(f"Seu palpite foi maior (>X). Tente novamente.")
            else:
                print(f"Seu palpite foi menor (<X). Tente novamente.")

            tentativas_restantes -= 1
            print(f"Você tem {tentativas_restantes} tentativa(s) restante(s).")

        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")

    if tentativas_restantes == 0:
        print(
            f"\nVocê esgotou todas as suas chances. O número correto era {numero_aleatorio}.")


# Rodar o jogo
jogo_adivinhacao()
