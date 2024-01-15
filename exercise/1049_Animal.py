# Neste problema, você deverá ler 3 palavras que definem o tipo de animal possível segundo o esquema abaixo, da esquerda para a direita.  Em seguida conclua qual dos animais seguintes foi escolhido, através das três palavras fornecidas.

# [IMAGEM DO DIAGRAMA]

# Entrada:
# A entrada contém 3 palavras, uma em cada linha, necessárias para identificar o animal segundo a figura acima, com todas as letras minúsculas.

# Saída:
# Imprima o nome do animal correspondente à entrada fornecida.

# Exemplo de Entrada
# vertebrado
# ave
# carnivoro

# Exemplo de Saída:
# aguia

esqueleto = input()
especie = input()
habito_alimentar = input()

if esqueleto == 'vertebrado':
    if especie == 'ave':
        if habito_alimentar == 'carnivoro':
            print('aguia')
        elif habito_alimentar == 'onivoro':
            print('pomba')
    elif especie == 'mamifero':
        if habito_alimentar == 'onivoro':
            print('homem')
        elif habito_alimentar == 'herbivoro':
            print('vaca')
elif esqueleto == 'invertebrado':
    if especie == 'inseto':
        if habito_alimentar == 'hematofago':
            print('pulga')
        elif habito_alimentar == 'herbivoro':
            print('lagarta')
    elif especie == 'anelideo':
        if habito_alimentar == 'hematofago':
            print('sanguessuga')
        elif habito_alimentar == 'onivoro':
            print('minhoca')