'''
Você terá como uma entrada várias linhas, cada uma com uma string. O valor de cada caracter é computado como segue:

Valor = (Posição no alfabeto) + (Elemento de entrada) + (Posição do elemento)

Todas posições são baseadas em zero. 'A' tem posição 0 no alfabeto, 'B' tem posição 1 no alfabeto, ... O cálculo de hash retornado é a soma de todos os caracteres da entrada. Por exemplo, se a entrada for:
CBA
DDD

então cada caractere deverá ser computado como segue:

2 = 2 + 0 + 0 : 'C' no elemento 0 posição 0
2 = 1 + 0 + 1 : 'B' no elemento 0 posição 1
2 = 0 + 0 + 2 : 'A' no elemento 0 posição 2
4 = 3 + 1 + 0 : 'D' no elemento 1 posição 0
5 = 3 + 1 + 1 : 'D' no elemento 1 posição 1
6 = 3 + 1 + 2 : 'D' no elemento 1 posição 2

O cálculo final de hash será 2+2+2+4+5+6 = 21.

Entrada
A entrada contém vários casos de teste. A primeira linha de entrada contém um inteiro N que indica a quantidade de casos de teste. Cada caso de teste inicia com um inteiro L (1 ≤ L ≤ 100) que indica a quantidade de linhas que vem a seguir. Cada uma destas L linhas contém uma string com até 50 letras maiúsculas ('A' - 'Z').

Saída
Para cada caso de teste imprima o valor de hash que é calculado conforme o exemplo apresentado acima.

5
2
CBA
DDD -> 21
1
Z -> 25
6
A
B
C
D
E
F -> 30
6
ABCDEFGHIJKLMNOPQRSTUVWXYZ
ABCDEFGHIJKLMNOPQRSTUVWXYZ
ABCDEFGHIJKLMNOPQRSTUVWXYZ
ABCDEFGHIJKLMNOPQRSTUVWXYZ
ABCDEFGHIJKLMNOPQRSTUVWXYZ
ABCDEFGHIJKLMNOPQRSTUVWXYZ -> 4290
1
ZZZZZZZZZZ -> 295

'''

casos_teste = int(input())


dict_alfabeto = {
    'A':0,
    'B':1,
    'C':2,
    'D':3,
    'E':4,
    'F':5,
    'G':6,
    'H':7,
    'I':8,
    'J':9,
    'K':10,
    'L':11,
    'M':12,
    'N':13,
    'O':14,
    'P':15,
    'Q':16,
    'R':17,
    'S':18,
    'T':19,
    'U':20,
    'V':21,
    'W':22,
    'X':23,
    'Y':24,
    'Z':25
}

def calcularValor(list_string: list, elemento_entrada: int) -> int:
    '''Valor = (Posição no alfabeto) + (Elemento de entrada) + (Posição do elemento)'''
    valor = 0
    posicao_alfabeto = 0
    value_elemento_entrada = elemento_entrada
    posicao_string_in_list = 0

    for index, value in enumerate(list_string):
        posicao_alfabeto = dict_alfabeto.get(str(value).upper())
        posicao_string_in_list = index
        
        valor += posicao_alfabeto + value_elemento_entrada + posicao_string_in_list
    
    return valor

for caso in range(casos_teste):
    qtd_strings = int(input())
    valor_final = 0
    
    for numero_entrada in range(qtd_strings):
        string = input()
        valor_final += calcularValor(list_string=list(string), elemento_entrada=numero_entrada)
    
    print(valor_final)
    
