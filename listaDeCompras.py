lista_de_compar = []

while True:
    print("Selecione uma opção")
    try:
        opcao = int(input("[1]inserir [2]apagar [3]listar [0]Sair : "))
        if opcao == 1:
            adicionar = input("adicione um item:")
            lista_de_compar.append(adicionar)
            continue

        if opcao == 2:
            try:
                apagar = input("digite a posição do item em que deseja retirar:")
                lista_de_compar.pop(int(apagar))
                continue
            except IndexError:
                print("Item não encontrado!")
                continue

        if opcao == 3:
            for produto in lista_de_compar:
                print(lista_de_compar.index(produto), produto)
            continue

        if opcao == 0:
            print("Obrigado pela preferencia !!!")
            break
    except ValueError:
        print("digite uma opção valida")
        continue
