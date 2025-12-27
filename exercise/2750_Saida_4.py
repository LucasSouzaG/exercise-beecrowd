'''
O seu professor de programação gostaria que você fizesse um programa com as seguintes características:

Criar 16 variáveis inteiras;
Atribuir a elas valores de 0 a 15 a cada um das variáveis anteriores;
Ter 39 traços (-) na primeira linha;
Ter uma | embaixo do primeiro traço, décimo terceiro, vigésimo terceiro e do trigésimo nono traço da primeira linha, embaixo do 4o traço deve começar a escrever “decimal”, embaixo do 16o traço deve começar a escrever “octal”, embaixo do 26o traço deve começar a escrever “Hexadecimal” e o restante preencher com espaço em branco;
Repita o procedimento 3;
Ter uma | embaixo do primeiro traço, décimo terceiro, vigésimo terceiro e do trigésimo nono traço da primeira linha, embaixo do 8o traço deve imprimir o valor da primeira variável em valor decimal, embaixo do 18o traço deve imprimir o valor da primeira variável em valor octal, embaixo do 31o traço deve imprimir o valor da primeira variável em valor hexadecimal e o restante preencher com espaço em branco;
Repita o procedimento 6 para as outras 15 variáveis;
Repita o procedimento 3.
No final deve ficar igual a imagem a seguir:

--------------------------------------- (39 traços)
| decimal   |  octal  |  Hexadecimal  |
---------------------------------------
|      0    |    0    |       0       |
|      1    |    1    |       1       |
|      2    |    2    |       2       |
|      3    |    3    |       3       |
|      4    |    4    |       4       |
|      5    |    5    |       5       |
|      6    |    6    |       6       |
|      7    |    7    |       7       |
|      8    |   10    |       8       |
|      9    |   11    |       9       |
|     10    |   12    |       A       |
|     11    |   13    |       B       |
|     12    |   14    |       C       |
|     13    |   15    |       D       |
|     14    |   16    |       E       |
|     15    |   17    |       F       |
--------------------------------------- (39 traços)
'''

zero = 0
um = 1
dois = 2
tres = 3
quatro = 4
cinco = 5
seis = 6
sete = 7
oito = 8
nove = 9
dez = 10
onze = 11
doze = 12
treze = 13
quatorze = 14
quinze = 15

list_values = []

hexadecimal_values = {
    dez:'A',
    onze:'B',
    doze:'C',
    treze:'D',
    quatorze:'E',
    quinze:'F'
}

def converter_octal_hexadecimal(numero: int, divisor: int) -> list:
    '''
    Técnica de função recussiva utilizada, que converterá um valor decimal em octadecimal ou em hexadecimal
    
    :param numero: valor que será o dividendo do divisor
    :type numero: int
    :param divisor: valor que será o divisor do dividendo (sendo 8 ou 16)
    :type divisor: int
    :return: retornará uma lista com o resto da divisão
    :rtype: list
    '''
    if numero < divisor:
        
        if divisor == 16:
            string_value = str(hexadecimal_values.get(numero, numero))
            list_values.append(string_value)
        else:
            list_values.append(str(numero))
      
        return list_values
    else: 
        divisao = int(numero / divisor)
        resto = numero % divisor

        if divisor == 16:
            string_value = str(hexadecimal_values.get(resto, resto))
            list_values.append(string_value)
        else:
            list_values.append(str(resto))

        return converter_octal_hexadecimal(numero=divisao, divisor=divisor)

def handler_convert(numero: int, divisor: int) -> int:
    '''
    Função para lidar com a lista do valor que será convertido
    
    :param numero: valor que será o dividendo do divisor
    :type numero: int
    :param divisor: valor que será o divisor do dividendo (sendo 8 ou 16)
    :type divisor: int
    :return: Description
    :return: reordenará a lista retornada pela funcão converter_octal_hexadecimal e retorna o valor já convertido
    :rtype: str
    '''
    list_values_ = converter_octal_hexadecimal(numero=numero, divisor=divisor)
    list_values_.reverse()
    join_values = ''.join(list_values_)

    list_values.clear()
    return join_values


print("---------------------------------------")
print("| decimal   |  octal  |  Hexadecimal  |")
print("---------------------------------------")
print(f"|      {zero}    |    {handler_convert(zero,divisor=8)}    |        {handler_convert(zero,divisor=16)}       |")
print(f"|      {um}    |    {handler_convert(um,divisor=8)}    |       {handler_convert(um,divisor=16)}       |")
print(f"|      {dois}    |    {handler_convert(dois,divisor=8)}    |       {handler_convert(dois,divisor=16)}       |")
print(f"|      {tres}    |    {handler_convert(tres,divisor=8)}    |       {handler_convert(tres,divisor=16)}       |")
print(f"|      {quatro}    |    {handler_convert(quatro,divisor=8)}    |       {handler_convert(quatro,divisor=16)}       |")
print(f"|      {cinco}    |    {handler_convert(cinco,divisor=8)}    |       {handler_convert(cinco,divisor=16)}       |")
print(f"|      {seis}    |    {handler_convert(seis,divisor=8)}    |       {handler_convert(seis,divisor=16)}       |")
print(f"|      {sete}    |    {handler_convert(sete,divisor=8)}    |       {handler_convert(sete,divisor=16)}       |")
print(f"|      {oito}    |   {handler_convert(oito,divisor=8)}    |       {handler_convert(oito,divisor=16)}       |")
print(f"|      {nove}    |   {handler_convert(nove,divisor=8)}    |       {handler_convert(nove,divisor=16)}       |")
print(f"|     {dez}    |   {handler_convert(dez,divisor=8)}    |       {handler_convert(dez,divisor=16)}       |")
print(f"|     {onze}    |   {handler_convert(onze,divisor=8)}    |       {handler_convert(onze,divisor=16)}       |")
print(f"|     {doze}    |   {handler_convert(doze,divisor=8)}    |       {handler_convert(doze,divisor=16)}       |")
print(f"|     {treze}    |   {handler_convert(treze,divisor=8)}    |       {handler_convert(treze,divisor=16)}       |")
print(f"|     {quatorze}    |   {handler_convert(quatorze,divisor=8)}    |       {handler_convert(quatorze,divisor=16)}       |")
print(f"|     {quinze}    |   {handler_convert(quinze,divisor=8)}    |       {handler_convert(quinze,divisor=16)}       |")
print("---------------------------------------")