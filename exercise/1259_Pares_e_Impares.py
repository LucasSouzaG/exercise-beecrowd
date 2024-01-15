# Considerando a entrada de valores inteiros não negativos, ordene estes valores segundo o seguinte critério:

# Primeiro os Pares
# Depois os Ímpares
# Sendo que deverão ser apresentados os pares em ordem crescente e depois os ímpares em ordem decrescente.

# Entrada
# A primeira linha de entrada contém um único inteiro positivo N (1 < N <= 105) Este é o número de linhas de entrada que vem logo a seguir. As próximas N linhas conterão, cada uma delas, um valor inteiro não negativo.

# Saída
# Apresente todos os valores lidos na entrada segundo a ordem apresentada acima. Cada número deve ser impresso em uma linha, conforme exemplo abaixo.

# Exemplo de Entrada
# 10
# 4
# 32
# 34
# 543
# 3456
# 654
# 567
# 87
# 6789
# 98

# Exemplo de Saída
# 4
# 32
# 34
# 98
# 654
# 3456
# 6789
# 567
# 543
# 87

casos_de_teste = int(input())
valores_pares = []
valores_impares = []


for caso in range(casos_de_teste):
    valor = int(input())

    if valor % 2 == 0:
        valores_pares.append(valor)
    else:
        valores_impares.append(valor)

valores_pares_ordenados = sorted(valores_pares)
valores_impares_ordenados = sorted(valores_impares, reverse=True)


for i in range(len(valores_pares_ordenados)):
    print(valores_pares_ordenados[i])

for i in range(len(valores_impares_ordenados)):
    print(valores_impares_ordenados[i])