# Leia 100 valores inteiros. Apresente então o maior valor lido e a posição dentre os 100 valores lidos.

# Entrada
# O arquivo de entrada contém 100 números inteiros, positivos e distintos.

# Saída
# Apresente o maior valor lido e a posição de entrada, conforme exemplo abaixo.

# Exemplo de Entrada
# 2
# 113
# 45
# 34565
# 6
# ...
# 8
 
# Exemplo de Saída
# 34565
# 4

maior_valor = 0
index = 0

for i in range(100):
    number = int(input())

    if number > maior_valor:
        maior_valor = number
        index = i
    else:
        continue

print(maior_valor)
print(index + 1)