# Implemente um programa denominado combinador, que recebe duas strings e deve combiná-las, alternando as letras de cada string, começando com a primeira letra da primeira string, seguido pela primeira letra da segunda string, em seguida pela segunda letra da primeira string, e assim sucessivamente. As letras restantes da cadeia mais longa devem ser adicionadas ao fim da string resultante e retornada.

# Entrada
# A entrada contém vários casos de teste. A primeira linha contém um inteiro N que indica a quantidade de casos de teste que vem a seguir. Cada caso de teste é composto por uma linha que contém duas cadeias de caracteres, cada cadeia de caracteres contém entre 1 e 50 caracteres inclusive.

# Saída
# Combine as duas cadeias de caracteres da entrada como mostrado no exemplo abaixo e exiba a cadeia resultante.

# Exemplo de Entrada
# 2
# Tpo oCder
# aa bb

# Exemplo de Saída
# TopCoder
# abab

casos_de_teste = int(input())

for caso in range(casos_de_teste):
    palavras = input()
    lista_palavras = palavras.split()
    caracteres_palavra_1 = lista_palavras[0]
    caracteres_palavra_2 = lista_palavras[1]
    

    if len(list(caracteres_palavra_1)) >= len(list(caracteres_palavra_2)):
        tamanho_maximo = len(list(caracteres_palavra_1))
    else:
        tamanho_maximo = len(list(caracteres_palavra_2))

    nova_palavra = []
    for i in range(tamanho_maximo):
        if len(list(caracteres_palavra_1)) >= len(list(caracteres_palavra_2)):
            try:
                nova_palavra.append(caracteres_palavra_1[i])    
                nova_palavra.append(caracteres_palavra_2[i])
            except:
                continue
        else:
            try:
                nova_palavra.append(caracteres_palavra_1[i])    
                nova_palavra.append(caracteres_palavra_2[i])
            except:
                nova_palavra.append(caracteres_palavra_2[i])

    print(''.join(map(str, nova_palavra)))