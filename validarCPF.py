import re
import sys

entrada = input("digite um cpf:")
cpf_enviado = re.sub(r"[^0-9]", "", entrada)

entrada_repetida =  entrada == entrada[0] * len(entrada)

if entrada_repetida:
    print("Dados sequenciais são invalidos")
    sys.exit()

cpf_cliente_lista = cpf_enviado[:9]
contador_regressivo = 10

cpf_somado = 0
for numero in cpf_cliente_lista:
    cpf_somado += int(numero) * contador_regressivo
    contador_regressivo -= 1

primeiro_digito = (cpf_somado * 10) % 11
primeiro_digito = primeiro_digito if primeiro_digito <= 9 else 0

cpf_cliente_lista_2 = cpf_enviado[:10]
contador_regressivo_2 = 11

cpf_somado_2 = 0
for numero_2 in cpf_cliente_lista_2:
    cpf_somado_2 += int(numero_2) * contador_regressivo_2
    contador_regressivo_2 -= 1

segundo_digito = (cpf_somado_2 * 10) % 11
segundo_digito = segundo_digito if segundo_digito <= 9 else 0

cpf_gerado = f"{cpf_cliente_lista}{primeiro_digito}{segundo_digito}"

if cpf_enviado == cpf_gerado:
    print(f"{cpf_enviado} é um cpf valido")
else:
    print("CPF inalido")
