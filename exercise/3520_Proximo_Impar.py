'''
Ygor é professor de programação e ensinou aos seus alunos como identificar se um número é par ou ímpar.

Agora ele está preparando uma prova com esse conteúdo e criou a seguinte questão:

Dado um número inteiro N, qual é o primeiro número ímpar maior que N?

Como você é um dos alunos do professor Ygor, também precisa resolver esse problema.

Entrada
A entrada contém um único número inteiro N ( 1 ≤ N ≤ 10^5 ).

Saída
A saída deve conter um número inteiro que representa o primeiro número ímpar maior que N .


10 -> 11
7 -> 9
8 -> 9
3 -> 5
'''

number_imput = int(input())

is_impar_par = number_imput % 2 == 0

if is_impar_par:
    print(number_imput+1)
else:
    print(number_imput+2)