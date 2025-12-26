'''
Keanu estava testando novos modelos de tabuleiros de xadrez quanto teve a seguinte duvida:

Quantas casas brancas e quantas casas pretas tem um tabuleiro de xadrez de tamanho nxn?

Entrada
O input consiste de uma linha com um único inteiro n.

2 ≤ n ≤ 100

Saída
Imprima "a casas brancas e b casas pretas" sem aspas, sendo a a quantidade de casas brancas e b a quantidade de casas pretas.

3 -> 5 casas brancas e 4 casas pretas
4 -> 8 casas brancas e 8 casas pretas

'''


tamanho_tabuleiro = int(input())
tamanho_tabuleiro_total = tamanho_tabuleiro ** 2
casas_pares = 0
casas_impares = 0

for numero_casa in range(1,tamanho_tabuleiro_total+1):
    if numero_casa % 2 != 0:
        casas_impares += 1
    else:
        casas_pares += 1

print(f'{casas_impares} casas brancas e {casas_pares} casas pretas')