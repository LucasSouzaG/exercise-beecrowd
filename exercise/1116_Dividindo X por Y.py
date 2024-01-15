# Escreva um algoritmo que leia 2 números e imprima o resultado da divisão do primeiro pelo segundo. Caso não for possível mostre a mensagem “divisao impossivel” para os valores em questão.

# Entrada
# A entrada contém um número inteiro N. Este N será a quantidade de pares de valores inteiros (X e Y) que serão lidos em seguida.

# Saída
# Para cada caso mostre o resultado da divisão com um dígito após o ponto decimal, ou “divisao impossivel” caso não seja possível efetuar o cálculo.

# Obs.: Cuide que a divisão entre dois inteiros em algumas linguagens como o C e C++ gera outro inteiro. Utilize cast :)

# Exemplo de Entrada
# 3
# 3 -2
# -8 0
# 0 8

# Exemplo de Saída
# -1.5
# divisao impossivel
# 0.0

while True:
    qtd_divisao = input('Digite a quantidade de valores inseridos: ')
    
    if qtd_divisao.isnumeric():
        qtd_divisao = int(qtd_divisao)
        for integer in range(qtd_divisao):
           
            divisor = float(input('digite o divisor: '))
            dividendo = float(input('digite o dividendo: '))
            if dividendo != 0:
                resultado = divisor / dividendo
                print(resultado,'\n')
            else:
                print('divisao impossivel\n')
        else:
            break
    else:
        print('\nDigite um numero inteiro valido\n')
        continue