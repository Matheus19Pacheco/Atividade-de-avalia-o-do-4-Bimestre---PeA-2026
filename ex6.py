################################################################
# Descrição: Lê 20 temperaturas em graus Celsius, armazena em  #
# um vetor e apresenta a menor, a maior e a média.             #
# Parâmetros de entrada: 20 valores reais (temperaturas).      #
# Valores de saída: Menor, maior e média das temperaturas.     #
# Autor: Matheus Ferreira Pacheco                              #
################################################################

A = []

for i in range(20):
    temperatura = float(input("Digite a temperatura (°C): "))
    A.append(temperatura)

menor = A[0]
maior = A[0]
soma = 0

for temperatura in A:
    if temperatura < menor:
        menor = temperatura
    if temperatura > maior:
        maior = temperatura
    soma = soma + temperatura

print("Menor:", menor)
print("Maior:", maior)
print("Média:", soma / 20)