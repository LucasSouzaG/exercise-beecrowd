# Leia dois valores inteiros M e N indefinidamente. A cada leitura, calcule e escreva a soma dos fatoriais de cada um dos valores lidos. Utilize uma variável apropriada, pois cálculo pode resultar em um valor com mais de 15 dígitos.

# Entrada
# O arquivo de entrada contém vários casos de teste. Cada caso contém dois números inteiros M (0 ≤ M ≤ 20) e N (0 ≤ N ≤ 20). O fim da entrada é determinado por eof.

# Saída
# Para cada caso de teste de entrada, seu programa deve imprimir uma única linha, contendo um número que é a soma de ambos os fatoriais (de M e N).

# Exemplo de Entrada & Exemplo de Saída
# 4 4

# 48 

# 0 0

# 2

# 0 2

# 3

def fatorial(number:int):
    if number == 0:
        return 1
    else:
        return number * fatorial(number - 1)

while True:
    try:
        m_n = input()

        print(fatorial(int(m_n.split()[0])) + fatorial(int(m_n.split()[1])))

    except EOFError:
        break