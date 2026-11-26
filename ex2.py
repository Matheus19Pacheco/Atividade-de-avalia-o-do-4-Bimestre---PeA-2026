################################################################
# Descrição: Calcula o somatório de grãos de trigo em um       #
# tabuleiro de xadrez (64 quadros), colocando 1 grão no        #
# primeiro quadro e o dobro do quadro anterior nos seguintes.  #
# Parâmetros de entrada: Nenhum                                #
# Valores de saída: Total de grãos de trigo no tabuleiro.      #
# Autor: Matheus Ferreira Pacheco                              #
################################################################

graos_quadro = 1
total = 0

for quadro in range(1, 65):
    total = total + graos_quadro
    graos_quadro = graos_quadro * 2

print("Total de grãos no tabuleiro:", total)