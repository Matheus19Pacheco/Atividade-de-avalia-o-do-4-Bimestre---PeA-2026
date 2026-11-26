################################################################
# Descrição: Lê dois vetores A e B com 12 elementos cada, com  #
# validação na entrada, e constrói um vetor C com a junção de  #
# A e B (24 elementos).                                        #
# Parâmetros de entrada: 12 inteiros divisíveis por 2 ou 3     #
# (vetor A) e 12 inteiros não múltiplos de 5 (vetor B).        #
# Valores de saída: Elementos do vetor C.                      #
# Autor: Matheus Ferreira Pacheco                              #
################################################################

A = []
B = []

while len(A) < 12:
    valor = int(input("Vetor A (divisível por 2 ou 3): "))
    if valor % 2 == 0 or valor % 3 == 0:
        A.append(valor)
    else:
        print("Valor inválido.")

while len(B) < 12:
    valor = int(input("Vetor B (não múltiplo de 5): "))
    if valor % 5 != 0:
        B.append(valor)
    else:
        print("Valor inválido.")

C = A + B

print("Vetor C:", C)