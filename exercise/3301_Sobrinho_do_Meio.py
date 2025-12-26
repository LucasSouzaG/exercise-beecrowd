'''
Tio Patinhas era um milionário que vivia em sua mansão, e tinha três sobrinhos: Huguinho, Zezinho e Luisinho. Ele se confundia facilmente entre os três sobrinhos, pois eram bem parecidos, apesar de terem idades diferentes. Um dia, os três fizeram uma aposta com o tio: se ele acertasse quem era o sobrinho do meio, ou seja, nem o mais novo, nem o mais velho, eles dariam uma moeda de ouro para ele, e se ele errasse, teria que dar uma moeda de ouro para cada um. Assim, o tio pede a tua ajuda para que ele possa ganhar essa aposta.


Entrada
A entrada consiste em vários casos de teste. Cada caso contém três valores inteiros H, Z e L, que representam as idades de Huguinho, Zezinho e Luisinho, respectivamente.

Saída
Para cada caso de teste imprima o nome do sobrinho do meio, com letras minúsculas.

5 6 7 -> zezinho
7 5 6 -> luisinho
6 7 5 -> huguinho
5 7 8 -> zezinho
6 11 8 -> luisinho
10 9 11 -> huguinho
'''

input_idades = input()
lista_idades = [int(idade) for idade in input_idades.split()]
lista_idades_ordenada = lista_idades.copy()
lista_idades_ordenada.sort(reverse=True)

'''
primeiro valor = huguinho
segundo valor = zezinho
terceio valor = luisinho
'''

'''Busca o valor da 2º posicaoposicao da lista ordenada'''
buscar_posicao = lista_idades.index(lista_idades_ordenada[1])

if buscar_posicao == 0:
    print('huguinho')
elif buscar_posicao == 1:
    print('zezinho')
elif buscar_posicao == 2:
    print('luisinho')

