# Neste problema você deverá ler 15 valores colocá-los em 2 vetores conforme estes valores forem pares ou ímpares. Só que o tamanho de cada um dos dois vetores é de 5 posições. Então, cada vez que um dos dois vetores encher, você deverá imprimir todo o vetor e utilizá-lo novamente para os próximos números que forem lidos. Terminada a leitura, deve-se imprimir o conteúdo que restou em cada um dos dois vetores, imprimindo primeiro os valores do vetor impar. Cada vetor pode ser preenchido tantas vezes quantas for necessário.

# Entrada
# A entrada contém 15 números inteiros.

# Saída
# Imprima a saída conforme o exemplo abaixo.

# Exemplo de Entrada
# 1
# 3
# 4
# -4
# 2
# 3
# 8
# 2
# 5
# -7
# 54
# 76
# 789
# 23
# 98

# Exemplo de Saída
# par[0] = 4
# par[1] = -4
# par[2] = 2
# par[3] = 8
# par[4] = 2
# impar[0] = 1
# impar[1] = 3
# impar[2] = 3
# impar[3] = 5
# impar[4] = -7
# impar[0] = 789
# impar[1] = 23
# par[0] = 54
# par[1] = 76
# par[2] = 98

def imprime_lista (lista:list, indicador:str):
    
    for i in range(len(lista)):
        print(f'{indicador}[{i}] = {lista[i]}')


lista_par = []
lista_impar = []

for i in range(15):
    numero = int(input())

    if numero % 2 == 0:
        lista_par.append(numero)
    else:
        lista_impar.append(numero)
    
    if len(lista_par) == 5:
        imprime_lista(lista_par, 'par')
        lista_par.clear()
    elif len(lista_impar) == 5:
        imprime_lista(lista_impar, 'impar')
        lista_impar.clear()

imprime_lista(lista_impar, 'impar')
imprime_lista(lista_par, 'par')
