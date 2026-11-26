################################################################
# Descrição: Lê um vetor A com 15 valores reais e constrói um  #
# vetor B: elementos de índice par são divididos por 2 e os    #
# de índice ímpar são multiplicados por 1,5.                   #
# Parâmetros de entrada: 15 valores reais.                     #
# Valores de saída: Elementos do vetor B.                      #
# Autor: Matheus Ferreira Pacheco                              #
################################################################

A = []
B = []

for i in range(15):
    valor = float(input("Digite um valor real: "))
    A.append(valor)

for i in range(15):
    if i % 2 == 0:
        B.append(A[i] / 2)
    else:
        B.append(A[i] * 1.5)

print("Vetor B:", B)