'''Thanos gostaria de viver em um ano perfeito. Depois de muito tempo pesquisando em diversas literaturas, ele descobriu que um ano é perfeito se este for múltiplo do valor Y.

Inicialmente Thanos se encontra no ano de número A e gostaria de se mudar para um ano perfeito. Assim que alcançar esse ano ideal, ele pretende utilizar as Joias do Infinito para fazer com que esse período nunca tenha fim, garantindo que possa viver em paz pelo restante de sua existência. Thanos tem o poder de viajar pelo tempo, podendo avançar para o futuro ou retornar ao passado, com limite de 1 ano por vez em cada viagem. Cada tipo de viagem no tempo tira uma certa quantidade de dias de vida de Thanos. Formalmente:

- Avançar para o futuro : Se Thanos encontra-se no ano A e gostaria de ir para o ano A+1 , então ele perderia F dias de vida.

- Retornar para o passado : Se Thanos encontra-se no ano A e gostaria de ir para o ano A-1 , então ele perderia P dias de vida.

Thanos pode utilizar seu poder de viajar no tempo quantas vezes quiser, desde que consiga alcançar um ano perfeito. No entanto, ele deseja fazer isso perdendo a menor quantidade possível de dias de vida. Você pode ajudá-lo a determinar qual é essa quantidade mínima?


Entrada
A entrada consiste de 4 inteiros (1 ≤ A, Y, F, P ≤ 10^9 ) , o ano em que Thanos se encontra, o valor no qual um ano perfeito deve ser múltiplo e o custo de viajar para o futuro e para o passado, respectivamente.


Saída
A saída deve conter o menor número de dias de vida que Thanos irá perder se escolher a melhor estratégia para chegar em um ano perfeito.

Explicação do primeiro caso de teste:

➔ O valor de A é 12 , ou seja, Thanos encontra-se no ano 12 .

➔ O valor de Y é 5 , ou seja, um ano só é perfeito se for múltiplo de 5 .

➔ O valor de F é 10 . Ou seja, o custo para viajar 1 ano para o futuro é 10 dias de vida a menos .

➔ O valor de P é 3 . Ou seja, o custo para viajar 1 ano para o passado é 3 dias de vida a menos .

➔ Thanos pode ir do ano 12 para o ano 10 , já que o ano 10 é múltiplo de 5 , fazendo isso ele vai perder 6 dias de vida , já que usou o poder de ir para o passado 2 vezes .

➔ Thanos pode ir do ano 12 para o ano 15 , já que o ano 15 é múltiplo de 5 , fazendo isso ele vai perder 30 dias de vida , já que usou o poder de ir para o futuro 3 vezes .

➔ Se Thanos escolher a melhor estratégia, vai perder apenas 6 dias de vida .
'''


def encontrar_ano_perfeito_passado(ano_atual: int, multiplo_ano_perfeito: int) -> int:
    ano_perfeito_passado = ano_atual

    while(True):
        # ano-1
        if (ano_perfeito_passado % multiplo_ano_perfeito) == 0:
            return ano_perfeito_passado
        ano_perfeito_passado -= 1 

def encontrar_ano_perfeito_futuro(ano_atual: int, multiplo_ano_perfeito: int) -> int:
    ano_perfeito_futuro = ano_atual

    while(True):
        # ano+1
        if (ano_perfeito_futuro % multiplo_ano_perfeito) == 0:
            return ano_perfeito_futuro
        ano_perfeito_futuro += 1 


input_values = input().split()

ano = int(input_values[0])
multiplo_ano_perfeito = int(input_values[1])
dias_perdidos_viagem_futuro = int(input_values[2])
dias_perdidos_viagem_passado = int(input_values[3])

ano_perfeito_futuro = encontrar_ano_perfeito_futuro(ano_atual=ano, multiplo_ano_perfeito=multiplo_ano_perfeito)
ano_perfeito_passado = encontrar_ano_perfeito_passado(ano_atual=ano, multiplo_ano_perfeito=multiplo_ano_perfeito)

ano_perfeito = ano_perfeito_futuro if ano_perfeito_futuro <= ano_perfeito_passado else ano_perfeito_passado

diff_ano_perfeito_futuro = ano_perfeito_futuro - ano
result_ano_perfeito_futuro = diff_ano_perfeito_futuro * dias_perdidos_viagem_futuro

diff_ano_perfeito_passado = ano - ano_perfeito_passado
result_ano_perfeito_passado = diff_ano_perfeito_passado * dias_perdidos_viagem_passado


resultado = result_ano_perfeito_futuro if result_ano_perfeito_futuro <= result_ano_perfeito_passado else result_ano_perfeito_passado
print(resultado)
