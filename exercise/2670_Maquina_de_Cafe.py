'''
O novo prédio da Sociedade Brasileira de Computação (SBC) possui 3 andares. Em determinadas épocas do ano, os funcionários da SBC bebem muito café. Por conta disso, a presidência da SBC decidiu presentear os funcionários com uma nova máquina de expresso. Esta máquina deve ser instalada em um dos 3 andares, mas a instalação deve ser feita de forma que as pessoas não percam muito tempo subindo e descendo escadas.

Cada funcionário da SBC bebe 1 café expresso por dia. Ele precisa ir do andar onde trabalha até o andar onde está a máquina e voltar para seu posto de trabalho. Todo funcionário leva 1 minuto para subir ou descer um andar. Como a SBC se importa muito com a eficiência, ela quer posicionar a máquina de forma a minimizar o tempo total gasto subindo e descendo escadas.

Sua tarefa é ajudar a diretoria a posicionar a máquina de forma a minimizar o tempo total gasto pelos funcionários subindo e descendo escadas.

Entrada
A entrada consiste em 3 números, A1 , A2 , A3 (0 ≤ A1 , A2 , A3 ≤ 1000), um por linha, onde Ai representa o número de pessoas que trabalham no i-ésimo andar.

Saída
Seu programa deve imprimir uma única linha, contendo o número total de minutos a serem gastos com o melhor posicionamento possível da máquina.

Exemplos de Entrada
10

20

30

Exemplos de Saída
80

Exemplos de Entrada
10

30

20

Exemplos de Saída
60

Exemplos de Entrada
30

10

20

Exemplos de Saída
100
'''

list_pessoas_andar = []

for i in range(1,4):
    qtd_pessoas = int(input())

    list_pessoas_andar.append(qtd_pessoas)

index_maior_valor = list_pessoas_andar.index(max(list_pessoas_andar))

total_list = []

total_1 = (int(list_pessoas_andar[1]) * 2) + (int(list_pessoas_andar[2]) * 4) 
total_list.append(total_1)
total_2 = (int(list_pessoas_andar[0]) * 2) + (int(list_pessoas_andar[2]) * 2) 
total_list.append(total_2)
total_3 = (int(list_pessoas_andar[1]) * 2) + (int(list_pessoas_andar[0]) * 4) 
total_list.append(total_3)

total = min(total_list)
print(total)