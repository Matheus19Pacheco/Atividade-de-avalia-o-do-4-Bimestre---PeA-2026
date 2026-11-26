################################################################
# Descrição: Lê um vetor A com 20 inteiros e constrói um vetor #
# B, onde cada elemento é o somatório de 1 até o valor do      #
# elemento correspondente de A.                                #
# Parâmetros de entrada: 20 valores inteiros.                  #
# Valores de saída: Elementos do vetor B.                      #
# Autor: Matheus Ferreira Pacheco                              #
################################################################

A = []
B = []

for i in range(20):
    valor = int(input("Digite um valor inteiro: "))
    A.append(valor)

for valor in A:
    soma = 0
    for n in range(1, valor + 1):
        soma = soma + n
    B.append(soma)

print("Vetor B:", B)