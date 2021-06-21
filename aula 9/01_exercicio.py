# Aula 09 - CodeLab - Estruturas de Repetição e Listas

# 01 - Crie um programa onde o usuário possa digitar vários valores numéricos e
# cadastre-os em uma lista. Caso o número já esteja lá dentro, ele não será
# adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem
# crescente.

lista = []
resp = 's'
while resp == 's':
    num = int(input('Digite um numero para a lista: '))
    
    if num not in lista:
        lista.append(num)
    
    resp = input('Deseja continuar (S/N)').lower()

    while resp not in ['s', 'n']:
        resp = input('Digite apenas s ou n: ')

print(sorted(lista))

