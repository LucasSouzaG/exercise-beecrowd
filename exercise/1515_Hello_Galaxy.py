# Atualmente, no ano de 2114, o conhecimento de que não estamos sozinhos no universo não é novidade, porém um século atrás isto ainda era um mistério. Diversas civilizações na Via Láctea já emitiram algum tipo de sinal provando sua existência, e outras até estabeleceram um contato aberto com a Terra em busca de informações sobre a tal Árvore Hexagonária (afinal, estamos em 2114).

# Rafael tem muito interesse pelo assunto, e em um trabalho para a escola se encarregou de descobrir qual foi a civilização mais antiga que enviou um Hello Galaxy para toda a galáxia. Hello Galaxy nada mais é que o primeiro dos passos do Protocolo de Iniciação na Sociedade Via Láctea, PISVL, garantindo que a nova civilização possa entrar em contato com as demais caso necessário.

# A mensagem Hello Galaxy traz consigo duas informações básicas: o texto “Hello Galaxy”, que faz parte da tradição, e o nome do planeta da civilização que enviou a mensagem. O CMSVL, Centro de Monitoramento da Sociedade Via Láctea, instalado, por algum motivo, na Terra, recebe tais mensagens, armazenando em um registro o ano em que foi recebida a mensagem e a quantidade de anos que tal mensagem levou para chegar até ali.

# A tarefa de Rafael é simples: descobrir quem foi a primeira civilização a enviar a mensagem Hello Galaxy.

# Entrada
# Haverá diversos casos de teste.

# Cada caso de teste inicia com um inteiro N (1 ≤ N ≤ 100), que indica quantas mensagens Hello Galaxy foram coletados por Rafael em sua pesquisa.

# Em seguida haverão N linhas, cada uma representando uma mensagem. Cada mensagem é representada pelo nome do planeta da civilização, contendo entre 1 e 50 caracteres (somente letras), e dois inteiros A e T (2014 ≤ A ≤ 2113, 1 ≤ T ≤ 1000), representando, respectivamente, o ano em que a mensagem foi recebida no planeta Terra, e a quantidade de anos que tal mensagem levou para chegar do planeta de origem até o planeta Terra.

# O último caso de teste é indicado quando N = 0, o qual não deverá ser processado.

# Saída
# Para cada caso de teste, deverá ser impressa uma linha, contendo o nome do planeta da primeira civilização a enviar a mensagem Hello Galaxy. Pode-se supor que não haverá empates.

# Exemplo de Entrada
# 3
# PlanetaXYZ 2014 5
# PlanetaDosMacacos 2020 7
# JINQEWIOSDFaa 2043 20
# 2
# PlanetaA 2050 10
# PlanetaB 2055 16
# 0

# Exemplo de Saída
# PlanetaXYZ
# PlanetaB

while True:
    casos_de_teste = int(input())
    primeiro_planeta = []
    
    if casos_de_teste == 0:
        break
    else:
        for caso in range(casos_de_teste):
            planetas = input()
            lista_planetas = planetas.split()
            diff_ano_planeta = lista_planetas.append(int(lista_planetas[1]) - int(lista_planetas[2]))
            primeiro_planeta.append(lista_planetas)
            primeiro_planeta.sort(key= lambda diff_ano: diff_ano[3])

        print(primeiro_planeta[0][0])
