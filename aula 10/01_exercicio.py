# 1 - Crie uma lista composta que recebe 5 nomes e 5 idades de clientes, utilizando o for e o if, 
# verifique quais clientes são maiores de idade e quais são menores de idade e mostre na tela 
# a seguinte frase para cada um deles: 'Fulano é maior de idade' ou 'Fulana é menor de idade' 
# e também quantos são maiores e quantos são menores de idade.

galera = list()
dado = list()
totmai = totmen = 0
for c in range(0,5):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade:')))
    galera.append(dado[:])
    dado.clear()

for p in galera:
    if p[1] >= 18:
        print(f'{p[0]} é maior de idade')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade')
        totmen += 1

print(f'Temos {totmai} maiores e {totmen} menores de idade.')
