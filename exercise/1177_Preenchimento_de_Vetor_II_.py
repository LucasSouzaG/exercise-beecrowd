# Faça um programa que leia um valor T e preencha um vetor N[1000] com a sequência de valores de 0 até T-1 repetidas vezes, conforme exemplo abaixo. Imprima o vetor N.

# Entrada
# A entrada contém um valor inteiro T (2 ≤ T ≤ 50).

# Saída
# Para cada posição do vetor, escreva "N[i] = x", onde i é a posição do vetor e x é o valor armazenado naquela posição.

# Exemplo de Entrada
# 3

# Exemplo de Saída
# N[0] = 0
# N[1] = 1
# N[2] = 2
# N[3] = 0
# N[4] = 1
# N[5] = 2
# N[6] = 0
# N[7] = 1
# N[8] = 2
# ...

valor_maximo = int(input())
valor_auxiliar = 0

for i in range(1000):
    if valor_auxiliar == valor_maximo:
        valor_auxiliar = 0
        print(f'N[{i}] = {valor_auxiliar}')
        valor_auxiliar += 1
    else:
        print(f'N[{i}] = {valor_auxiliar}')
        valor_auxiliar += 1