'''
Faça um programa que leia uma frase e informe se ela é palíndrome.
Uma frase ou palavra é chamada de palíndrome quando pode ser lida de traz para frente e de frente para traz, que ela eh igual.
ex: arara -> é palíndrome
Arara -> nao é palíndrome pq A é diferente de a
a rara -> nao é palíndrome pq espaço é diferente de r


Entrada
Consiste um uma única linha, contendo uma frase com letras, números, símbolos e espaços, com no máximo 1000 caracteres. 

Saída
O Programa deve escrever "A frase[" seguido da frase lida, depois "] nao eh palindrome" caso não seja palíndrome ou "] eh palindrome"  caso seja palíndrome. 
Não se esqueça do pulo de linha no final.

arara -> A frase [arara] eh palindrome
socorrammesubinoonibusemmarrocos -> A frase [socorrammesubinoonibusemmarrocos] eh palindrome
socorram-me subi no onibus em-marrocos -> A frase [socorram-me subi no onibus em-marrocos] nao eh palindrome
:?'"!@#>--$%&*() 12345678900987654321 )(*&%$-->#@!"'?: -> A frase [:?'"!@#>--$%&*() 12345678900987654321 )(*&%$-->#@!"'?:] eh palindrome
socorram-me subino onibus em-marrocos -> A frase [socorram-me subino onibus em-marrocos] eh palindrome
'''


string = input()
string_original = list(string)
string_inverted = list(reversed(string))

for i in range(0, len(string_original)):
    if string_original[i] == string_inverted[i]:
        continue
    print(f'A frase [{string}] nao eh palindrome')
    break
else:
    print(f'A frase [{string}] eh palindrome')