import os
import json


def listar(tarefas):
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
    listar(tarefas)


def refazer(tarefas, tarefas_refazer):
    if not tarefas_refazer:
        print("nenhuma tarefa para refazer")
        return

    tarefa = tarefas_refazer.pop()
    tarefas.append(tarefa)
    print()
    listar(tarefas)


def adicionar(tarefa, tarefas):
    tarefa = tarefa.strip()
    if not tarefa:
        print("digite uma tarefa")
        return

    tarefas.append(tarefa)
    print()
    listar(tarefas)


def ler(tarefas, caminho_arquivo):
    dados = []
    try:
        with open(caminho_arquivo, "r", encoding="utf8") as arquivo:
            dados = json.load(arquivo)
    except FileExistsError:
        print("Arquivo não existe")
        salvar(tarefas, caminho_arquivo)
    return dados


def salvar(tarefas, caminho_arquivo):
    dados = tarefas
    with open(caminho_arquivo, "w", encoding="utf8") as arquivo:
        dados = json.dump(tarefas, arquivo, indent=2, ensure_ascii=False)
    return dados

CAMINHO_ARQUIVO = "tarefas.json"
tarefas = ler([], CAMINHO_ARQUIVO)
tarefas_refazer = []

while True:
    print("Comandos: listar, desfazer, refazer")
    tarefa = input("Digite uma tarefa ou um comando: ")

    comandos = {
        "listar": lambda: listar(tarefas),
        "desfazer": lambda: desfazer(tarefas, tarefas_refazer),
        "refazer": lambda: refazer(tarefas, tarefas_refazer),
        "clear": lambda: os.system("cls"),
        "adicionar": lambda: adicionar(tarefa, tarefas),
    }

    comando = (
        comandos.get(tarefa)
        if comandos.get(tarefa) is not None
        else comandos["adicionar"]
    )

    comando()
    salvar(tarefas, CAMINHO_ARQUIVO)
