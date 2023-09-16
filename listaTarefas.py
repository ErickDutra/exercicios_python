import os

tarefas = []

tarefas_refazer = []


def listar_tarefas(tarefas):
    if not tarefas:
        print("nenhuma tarefa listada")
        print()
        return
    print("tarefas:")
    for tarefa in tarefas:
        print(tarefa)
    print()


def desfazer(tarefas, tarefas_refazer):
    if not tarefas:
        print("nenhuma tarefa para desfazer")
        return

    tarefa = tarefas.pop()
    tarefas_refazer.append(tarefa)
    print()


def refazer(tarefas, tarefas_refazer):
    if not tarefas_refazer:
        print("nenhuma tarefa para refazer")
        return

    tarefa = tarefas_refazer.pop()
    tarefas.append(tarefa)
    print()


def adicionar(tarefa, tarefas):
    tarefa = tarefa.strip()
    if not tarefa:
        print("digite uma tarefa")
        return

    tarefas.append(tarefa)
    print()


while True:
    print("Comandos: listar, desfazer, refazer")
    tarefa = str(input("Digite uma tarefa ou um comando: ")).strip(" ")

    if tarefa == "listar":
        listar_tarefas(tarefas)
        continue

    elif tarefa == "desfazer":
        desfazer(tarefas, tarefas_refazer)
        listar_tarefas(tarefas)
        continue

    elif tarefa == "refazer":
        refazer(tarefas, tarefas_refazer)
        listar_tarefas(tarefas)
        continue

    elif tarefa == "clear":
        os.system("cls")
        continue

    elif tarefa == "sair":
        break

    else:
        adicionar(tarefa, tarefas)
