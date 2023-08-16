import os

palavra_secreta = "secreta"
tentativas_acertos = 0
letras_acertos = ""


while True:
    letra_digitada = input(str("Digite uma letra:")).lower()
    tentativas_acertos += 1

    if len(letra_digitada) > 1:
        print("Digite apenas uma letra")
        continue

    if letra_digitada in palavra_secreta:
        letras_acertos += letra_digitada

    palavra_formada = ""
    for letra in palavra_secreta:
        if letra in letras_acertos:
            palavra_formada += letra
        else:
            palavra_formada += "*"

    print("Palavra formada:", palavra_formada)
    
    if palavra_formada == palavra_secreta:
        os.system("cls")
        print("Parabéns você acertou !!! ")
        print("A palavra secreta era: ", palavra_secreta)
        print("Tentativas: ", tentativas_acertos)
        palavra_secreta = "secreta"
        letras_acertos = ""
        tentativas_acertos = 0
