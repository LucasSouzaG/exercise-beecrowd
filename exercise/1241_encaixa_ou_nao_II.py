# Paulinho tem em suas mãos um novo problema. Agora a sua professora lhe pediu que construísse um programa para verificar, à partir de dois valores muito grandes A e B, se B corresponde aos últimos dígitos de A.

# Entrada
# A entrada consiste de vários casos de teste. A primeira linha de entrada contém um inteiro N que indica a quantidade de casos de teste. Cada caso de teste consiste de dois valores A e B maiores que zero, cada um deles podendo ter até 1000 dígitos.

# Saída
# Para cada caso de entrada imprima uma mensagem indicando se o segundo valor encaixa no primeiro valor, confome exemplo abaixo.


# Exemplo de Entrada & Exemplo de Saída
# 4

# 56234523485723854755454545478690 78690
# encaixa

# 5434554 543
# nao encaixa

# 1243 1243
# encaixa

# 54 64545454545454545454545454545454554
# nao encaixa


casos_de_teste = int(input())

for caso in range(casos_de_teste):
    valores_a_b = input()
    lista_valores_a_b = valores_a_b.split()
    
    # A condicional lista_valores_a_b[0][-len(lista_valores_a_b[1]):] faz um recorte dos ultimos caracteres do primeiro valor da lista com base no tamanho total dos caracteres do segundo valor da lista
    if lista_valores_a_b[0][-len(lista_valores_a_b[1]):] == lista_valores_a_b[1]:
        print('encaixa')
    else:
        print('nao encaixa')
    