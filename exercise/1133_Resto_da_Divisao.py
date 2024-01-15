# Escreva um programa que leia 2 valores X e Y e que imprima todos os valores entre eles cujo resto da divisão dele por 5 for igual a 2 ou igual a 3.

# Entrada
# O arquivo de entrada contém 2 valores positivos inteiros quaisquer, não necessariamente em ordem crescente.

# Saída
# Imprima todos os valores conforme exemplo abaixo, sempre em ordem crescente.

# Exemplo de Entrada
# 10
# 18

# Exemplo de Saída
# 12
# 13
# 17

def maior(x,y):
  if x>y:
    return x
  elif x==y:
    return x
  else:
    return y
  
def menor(x,y):
  if x>y:
    return y
  elif x==y:
    return y
  else:
    return x

x=int(input())
y=int(input())

numero_maior = maior(x,y)
numero_menor = menor(x,y)

for i in range(numero_menor+1,numero_maior):
  if ((i % 5) == 2) or ((i % 5) == 3):
    print(i)