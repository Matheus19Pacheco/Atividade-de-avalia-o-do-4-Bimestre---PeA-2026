################################################################
# Descrição: Calcula a área de cada cômodo de uma residência   #
# (largura x comprimento) e, ao final, apresenta a área total  #
# acumulada em metros quadrados.                               #
# Parâmetros de entrada: Nome, largura e comprimento (em       #
# metros) de cada cômodo e a resposta SIM/NÃO para continuar.  #
# Valores de saída: Área de cada cômodo e área total da        #
# residência.                                                  #
# Autor: Matheus Ferreira Pacheco                              #
################################################################

area_total = 0
resposta = "SIM"

while resposta == "SIM":
    nome = input("Nome do cômodo: ")
    largura = float(input("Largura (m): "))
    comprimento = float(input("Comprimento (m): "))

    area = largura * comprimento
    area_total = area_total + area
    print("Área de", nome, ":", area, "m2")

    resposta = input("Deseja calcular outro cômodo? (SIM/NÃO): ").upper()

print("Área total da residência:", area_total, "m2")