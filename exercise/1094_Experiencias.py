# Maria acabou de iniciar seu curso de graduação na faculdade de medicina e precisa de sua ajuda para organizar os experimentos de um laboratório o qual ela é responsável. Ela quer saber no final do ano, quantas cobaias foram utilizadas no laboratório e o percentual de cada tipo de cobaia utilizada.

# Este laboratório em especial utiliza três tipos de cobaias: sapos, ratos e coelhos. Para obter estas informações, ela sabe exatamente o número de experimentos que foram realizados, o tipo de cobaia utilizada e a quantidade de cobaias utilizadas em cada experimento.

# Entrada
# A primeira linha de entrada contém um valor inteiro N que indica os vários casos de teste que vem a seguir. Cada caso de teste contém um inteiro Quantia (1 ≤ Quantia ≤ 15) que representa a quantidade de cobaias utilizadas e um caractere Tipo ('C', 'R' ou 'S'), indicando o tipo de cobaia (R:Rato S:Sapo C:Coelho).

# Saída
# Apresente o total de cobaias utilizadas, o total de cada tipo de cobaia utilizada e o percentual de cada uma em relação ao total de cobaias utilizadas, sendo que o percentual deve ser apresentado com dois dígitos após o ponto.

# Exemplo de Entrada
# 10
# 10 C
# 6 R
# 15 S
# 5 C
# 14 R
# 9 C
# 6 R
# 8 S
# 5 C
# 14 R

# Exemplo de Saída
# Total: 92 cobaias
# Total de coelhos: 29
# Total de ratos: 40
# Total de sapos: 23
# Percentual de coelhos: 31.52 %
# Percentual de ratos: 43.48 %
# Percentual de sapos: 25.00 %

casos_de_teste = int(input())
total_de_cobaias = 0
total_de_coelhos = 0
total_de_ratos = 0
total_de_sapos = 0

for caso in range(casos_de_teste):
    quantidade_e_tipo = input()
    lista_quantidade_e_tipo = quantidade_e_tipo.split()
    total_de_cobaias += int(lista_quantidade_e_tipo[0])

    if lista_quantidade_e_tipo[1] == 'C':
        total_de_coelhos += int(lista_quantidade_e_tipo[0])
    elif lista_quantidade_e_tipo[1] == 'R':
        total_de_ratos += int(lista_quantidade_e_tipo[0])
    elif lista_quantidade_e_tipo[1] == 'S':
        total_de_sapos += int(lista_quantidade_e_tipo[0])

print(f'Total: {total_de_cobaias} cobaias')
print(f'Total de coelhos: {total_de_coelhos}')
print(f'Total de ratos: {total_de_ratos}')
print(f'Total de sapos: {total_de_sapos}')

percentual_coelhos = (total_de_coelhos * 100) / total_de_cobaias
percentual_ratos = (total_de_ratos * 100) / total_de_cobaias
percentual_sapos = (total_de_sapos * 100) / total_de_cobaias

print(f'Percentual de coelhos: {percentual_coelhos:.2f} %')
print(f'Percentual de ratos: {percentual_ratos:.2f} %')
print(f'Percentual de sapos: {percentual_sapos:.2f} %')
