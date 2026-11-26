#################################################################
# Descrição: Programa que calcula e apresenta as potências de   #
#            base 3 com expoente de 0 a 15, usando laço de      #
#            repetição                                          #
# Parâmetros de entrada: Nenhum                                 #
# Valores de saída: Apresentação dos valores das potências      #
# Autor: Matheus Ferreira Pacheco                               #
#################################################################

potencia = 1

for expoente in range(16):
    print(f"3 elevado a {expoente} = {potencia}")
    potencia = potencia * 3