# Leia 1 valor inteiro N, que representa o número de casos de teste que vem a seguir. Cada caso de teste consiste de 3 valores reais, cada um deles com uma casa decimal. Apresente a média ponderada para cada um destes conjuntos de 3 valores, sendo que o primeiro valor tem peso 2, o segundo valor tem peso 3 e o terceiro valor tem peso 5.

# Entrada
# O arquivo de entrada contém um valor inteiro N na primeira linha. Cada N linha a seguir contém um caso de teste com três valores com uma casa decimal cada valor.

# Saída
# Para cada caso de teste, imprima a média ponderada dos 3 valores, conforme exemplo abaixo.

# Exemplo de Entrada
# 3
# 6.5 4.3 6.2
# 5.1 4.2 8.1
# 8.0 9.0 10.0

# Exemplo de Saída
# 5.7
# 6.3
# 9.3

sequencia = int(input())

for casos in range(sequencia):
    notas = input()
    lista_notas = notas.split()

    nota_1 = float(lista_notas[0]) * 2
    nota_2 = float(lista_notas[1]) * 3
    nota_3 = float(lista_notas[2]) * 5

    resultado = (nota_1 + nota_2 + nota_3) / 10
    print(f'{resultado:.1f}')