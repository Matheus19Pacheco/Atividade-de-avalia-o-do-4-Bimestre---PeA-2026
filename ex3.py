################################################################
# Descrição: Lê valores numéricos sucessivamente enquanto o    #
# usuário fornecer valores não negativos e, ao final, apresenta#
# o somatório, a média e o total de valores lidos.             #
# Parâmetros de entrada: Valores numéricos digitados pelo      #
# usuário. Um valor negativo encerra a leitura.                #
# Valores de saída: Somatório, média e quantidade de valores   #
# lidos.                                                       #
# Autor: Matheus Ferreira Pacheco                              #
################################################################

soma = 0
quantidade = 0

valor = float(input("Digite um valor (e caso queira encerrar use um número negativo para encerrar): "))

while valor >= 0:
    soma = soma + valor
    quantidade = quantidade + 1
    valor = float(input("Digite um valor (e caso queira encerrar use um número negativo para encerrar): "))

if quantidade > 0:
    media = soma / quantidade
    print("Somatório:", soma)
    print("Média:", media)
    print("Total de valores lidos:", quantidade)
else:
    print("Nenhum valor válido foi informado.")