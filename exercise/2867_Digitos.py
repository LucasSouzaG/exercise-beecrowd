# Dados dois números inteiros, n e m, quantos dígitos tem nm ?

# Exemplos:

# 2 e 10 - 210 = 1024 - 4 dígitos

# 3 e 9 - 39 = 19683 - 5 dígitos

# Entrada
# A entrada é composta por vários casos de teste. A primeira linha tem um número inteiro C, representando a quantidade de casos de teste. As C linhas seguintes contém dois números inteiros N e M (1 <= N, M <= 100).

# Saída
# Para cada caso de teste de entrada do seu programa, você deve imprimir um número inteiro contendo a quantidade de dígitos do resultado da potência calculada no respectivo caso de teste.

# Exemplo de Entrada
# 4
# 1 1
# 2 10
# 3 9
# 100 100

# Exemplo de Saída
# 1
# 4
# 5
# 201

def fatorial(n, m):
    resultado = 1
    for i in range(m):
        resultado *= n
    return str(resultado)

casos_de_teste = int(input())

for caso in range(casos_de_teste):
    fatorial_ = input()
    lista_fatorial = fatorial_.split()
    digitos = fatorial(int(lista_fatorial[0]), int(lista_fatorial[1]))
    print(len(list(digitos)))
