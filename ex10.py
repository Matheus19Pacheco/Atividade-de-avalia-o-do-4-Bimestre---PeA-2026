################################################################
# Descrição: Lê um vetor A com 10 inteiros e apresenta o total #
# de elementos ímpares e o percentual deles em relação ao      #
# total de elementos do vetor.                                 #
# Parâmetros de entrada: 10 valores inteiros.                  #
# Valores de saída: Quantidade de números ímpares e            #
# percentual.                                                  #
# Autor: Matheus Ferreira Pacheco                              #
################################################################

A = []
impares = 0

for i in range(10):
    valor = int(input("Digite um valor inteiro: "))
    A.append(valor)
    if valor % 2 != 0:
        impares = impares + 1

print("Total de ímpares:", impares)
print("Percentual de ímpares:", impares * 10, "%")