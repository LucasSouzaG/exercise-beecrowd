# Ultimamente, diversas pessoas estão indo à Dra. Cláudia Café com Leite para saber se estão consumindo a quantidade recomendada diária de vitamina C. Isso tem a deixado exausta, e por isso ela lhe pediu para escrever um programa que, dado o consumo diário de alimentos ricos em vitamina C por uma pessoa, indique o quanto essa pessoa deve consumir a mais ou a menos para atingir o recomendado.

# Para tal, você poderá utilizar a tabela a seguir:

# Considere que o consumo diário recomendado de vitamina C está entre 110 mg e 130 mg, inclusive.

# Entrada
# Cada caso de teste é composto um inteiro T (1 ≤ T ≤ 7) indicando que a pessoa consome diariamente T alimentos entre os 7 alimentos da tabela. Em seguida, haverá T linhas com um inteiro N e um alimento (totalmente em caixa baixa e sem acentuações), indicando que a pessoa consome uma quantidade N daquele alimento. A entrada termina com T = 0.

# Saída
# Para cada caso de teste (T), se o consumo ultrapassou o limite recomendado, imprima "Menos X mg", em que X representa a quantidade a menos a ser consumida para atingir o limite recomendado; se o consumo não atingiu o recomendado, imprima "Mais X mg", em que X representa a quantidade a mais para atingir o recomendado; se o consumo está dentro do intervalo recomendado, imprima "X mg", em que X representa a quantidade consumida diariamente pela pessoa.

# Exemplo de Entrada & Exemplo de Saída
# 2

# 2 suco de laranja

# 3 mamao

# Menos 365 mg

# 1

# 3 brocolis

# Mais 8 mg

# 2

# 1 manga

# 1 laranja

# Mais 4 mg

# 1

# 1 suco de laranja

# 120 mg

# 0

alimentos = {
    'suco de laranja': 120,
    'morango fresco': 85,
    'mamao': 85,
    'goiaba vermelha': 70,
    'manga': 56,
    'laranja': 50,
    'brocolis': 34
}


def calculo_vitamina_c(alimento_e_quantidade:str):
    valor_vitamina = alimentos.get(alimento_e_quantidade[1])

    return int(alimento_e_quantidade[0]) * valor_vitamina

while True:
    casos_de_uso = int(input())
    if casos_de_uso == 0:
        break
    else:
        resultado = 0

        for i in range(casos_de_uso):
            alimento_e_quantidade = input()
            
            resultado += calculo_vitamina_c(alimento_e_quantidade.split(None,1))

        if resultado <= 110:
            print(f'Mais {110 - resultado} mg')
        elif resultado >= 130:
            print(f'Menos {resultado - 130} mg')
        else:
            print(f'{resultado} mg')