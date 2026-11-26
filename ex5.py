################################################################
# Descrição: Calcula o quociente inteiro da divisão de dois    #
# números usando subtrações sucessivas, sem o operador de      #
# divisão inteira.                                             #
# Parâmetros de entrada: Dividendo e divisor                   #
# Valores de saída: Quociente inteiro da divisão.              #
# Autor: Matheus Ferreira Pacheco                              #
################################################################

dividendo = int(input("Dividendo: "))
divisor = int(input("Divisor: "))

if divisor == 0:
    print("Divisor não pode ser zero.")
else:
    quociente = 0
    while dividendo >= divisor:
        dividendo = dividendo - divisor
        quociente = quociente + 1
    print("Quociente:", quociente)