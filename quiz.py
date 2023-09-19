perguntas = [
    {
        "Pergunta": "Quanto é 2+2",
        "Opcoes": ["1", "2", "3", "4"],
        "Resposta": "4",
        "Score": "5",
    },
    {
        "Pergunta": "Quanto é 5 x 5",
        "Opcoes": ["25", "55", "30", "45"],
        "Resposta": "25",
        "Score": "5",
    },
    {
        "Pergunta": "Quanto é 10 / 2",
        "Opcoes": ["5", "10", "0", "20"],
        "Resposta": "5",
        "Score": "5",
    },
    {
        "Pergunta": "Quanto é 10 x 10",
        "Opcoes": ["100", "50", "10", "0"],
        "Resposta": "100",
        "Score": "5",
    },
]

while True:
    print("Começar Quiz?")
    start_stop = int(input("Yes [1] --  No [0] :"))
    score = 0

    if start_stop == 1:
        for questao in perguntas:
            print(questao["Pergunta"])
            opcoes = questao["Opcoes"]
            resposta = input(f"Responda de acordo com as opçoes : {opcoes} : ")
            
            if resposta == questao["Resposta"]:
                print("voce acertou !!! ")
                score = score + int(questao["Score"])

            if resposta != questao["Resposta"]:
                print("voce errou")
                continue

    print(f"sua pontuação foi : {score}")
    print("Fim do Quiz")
    score = 0
    
    if start_stop == 0:
        break
