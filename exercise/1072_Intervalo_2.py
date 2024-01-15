# Leia um valor inteiro N. Este valor será a quantidade de valores inteiros X que serão lidos em seguida.
# Mostre quantos destes valores X estão dentro do intervalo [10,20] e quantos estão fora do intervalo, mostrando essas informações.

# Entrada
# A primeira linha da entrada contém um valor inteiro N (N < 10000), que indica o número de casos de teste.
# Cada caso de teste a seguir é um valor inteiro X (-107 < X <107).
 

# Saída
# Para cada caso, imprima quantos números estão dentro (in) e quantos valores estão fora (out) do intervalo.

# Exemplo de Entrada
# 4
# 14
# 123
# 10
# -25


# Exemplo de Saída
# 2 in
# 2 out

sequencia = int(input())
numero_in = 0
numero_out = 0

for i in range(sequencia):
    n = int(input())

    if n >= 10 and n <= 20:
        numero_in += 1
    else:
        numero_out += 1

print(f"{numero_in} in")
print(f"{numero_out} out")