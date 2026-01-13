"""
O rodízio municipal de veículos de São Paulo é uma restrição à circulação de veículos automotores na cidade. Implantado desde 1996 com o propósito de melhorar as condições ambientais reduzindo a carga de poluentes na atmosfera, se consolidou como um instrumento para reduzir congestionamentos nas principais vias da cidade, nos horários de maior movimento. Nas vias delimitadoras não é permitido o tráfego de caminhões e automóveis que estejam dentro da restrição. Há uma escala que determina em quais dias da semana quais veículos não podem circular. Essa escala é regida pelo último dígito da placa do veículo, sendo:

Segunda-feira, digito final da placa 1 e 2
Terça-feira, digito final da placa 3 e 4
Quarta-feira, digito final da placa 5 e 6
Quinta-feira, digito final da placa 7 e 8
Sexta-feira, digito final da placa 9 e 0
Os motoristas que são flagrados violando a restrição de circulação são autuados com multa e quatro pontos na carteira de habilitação.

Entrada
A primeira linha de entrada representa a quantidade de testes N (0 <= N < 1000) que deverão ser considerados. As demais entradas são cadeia de caracteres com tamanho máximo S (1 <= S <= 100) que representam cada placa que deverá ser analisada, de tal forma que, cada placa fique em uma única linha de entrada. O formato esperado para uma placa veicular válida em São Paulo é "AAA-9999", tal que A é um caracter válido em [A-Z], e 9 um dígito numérico válido em [0-9].

Saída
O conjunto de valores válidos como saída são: MONDAY, TUESDAY, WEDNESDAY, THURSDAY e FRIDAY, de acordo com a tabela de restrições predefinida, e FAILURE caso a placa não apresente o padrão definido.

Exemplos de Entrada	Exemplos de Saída
3
ABC-1234
XYZ-1010
AAA3333

TUESDAY
FRIDAY
FAILURE

4
abc-1234
a-1010
ABCD-1234
AIQ-2001

FAILURE
FAILURE
FAILURE
MONDAY


"""
casos = int(input())

for i in range(casos):
    placa = list(input())
    ultimo_digito = placa[-1]
    primeira_validacao = True if len(placa) == 8 else False
    segunda_validacao = True if '-' in placa else False
    terceira_validacao = False
    if '-' in placa:
        index = placa.index('-')
        if index == 3: terceira_validacao = True

    letras = ''.join(placa)
    quarta_validacao = any(c.islower() for c in letras)
    quinta_validacao = True if index and ''.join(placa[index+1:]).isdigit() else False
    sexta_validacao = True if index and ''.join(placa[:index]).isalpha() else False

    if primeira_validacao and segunda_validacao and terceira_validacao and not quarta_validacao and quinta_validacao and sexta_validacao:
        if ultimo_digito == '1' or ultimo_digito == '2':
            print('MONDAY')
        elif ultimo_digito == '3' or ultimo_digito == '4':
            print('TUESDAY')
        elif ultimo_digito == '5' or ultimo_digito == '6':
            print('WEDNESDAY')
        elif ultimo_digito == '7' or ultimo_digito == '8':
            print('THURSDAY')
        elif ultimo_digito == '9' or ultimo_digito == '0':
            print('FRIDAY')
    else:
        print('FAILURE')