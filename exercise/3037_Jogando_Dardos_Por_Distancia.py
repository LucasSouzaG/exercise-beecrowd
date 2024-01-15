# João e Maria criaram sua própria versão de jogar dardos, dardos por distância. Cada um jogava 3 dardos, escolhendo qual distância irão jogar do alvo. No jogo normal de dardos, se pontua um número 
# x pela distância entre onde o dardo acertou e o centro do alvo. No jogo de João e Maria se pontua x × d onde d é a distancia do atirador e o alvo.

# João pede para você fazer um algorítimo que dado a pontuação e a distância de cada jogada devolve o vencedor

# Entrada
# A primeira linha da entrada consite em um número N de casos de teste. Em cada caso de teste haverão 6 linhas, onde as primeiras 3 linhas correspondem aos arremessos de João e as próximas 3 linhas aos arremessos de Maria. Cada linha de um caso de teste consiste em dois números X e D onde X é a pontuação e D é a distância 

# Saída
# A saída consiste no vencedor de cada caso de teste.

# Exemplo de Entrada
# 2
# 1 10
# 2 1
# 1 1
# 10 10
# 1 0
# 2 0
# 10 1
# 1 10
# 2 5
# 1 1
# 2 1
# 3 0

# Exemplo de Saída
# MARIA
# JOAO

casos_de_teste = int(input())

for caso in range(casos_de_teste):
    pontos_joao = 0
    pontos_maria = 0

    for rodada_joao in range(3):
        jogada_joao = input()
        x, d = jogada_joao.split()
        pontos_joao += int(x) * int(d)

    for rodada_maria in range(3):
        jogada_maria = input()
        x, d = jogada_maria.split()
        pontos_maria += int(x) * int(d)

    if pontos_joao > pontos_maria:
        print('JOAO')
    else:
        print('MARIA')