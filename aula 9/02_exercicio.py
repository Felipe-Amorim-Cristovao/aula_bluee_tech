# 02 - Crie um programa que vai ler vários números e colocar em uma lista. Depois
# disso, crie duas listas extras que vão conter apenas os valores pares e os valores
# ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas
# geradas.

num = int(input('Digite quantos valores deseja colocar na lista: '))
a = 0
lista_principal = []
lista_par = []
lista_impar = []
while a < num:
    valor = int(input('Digite um valor: '))
    lista_principal.append(valor)
    
    if valor%2 == 0:
        lista_par.append(valor)
    else:
        lista_impar.append(valor)
    
    a += 1

print(f'Lista principal: {lista_principal}\n')
print(f'Lista com os valores pares: {lista_par}\n')
print(f'Lista com os valores ímpares: {lista_impar}\n')