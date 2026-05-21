# 2 - Leia um valor inteiro correspondente a uma temperatura em graus Fahrenheit e apresente-a convertida em graus Celsius. 
# Fórmula de conversão: C = (F - 32) * (5/9), sendo C o valor em graus Celsius e F o valor em Fahrenheit. Antes de imprimir, converta o valor em Celsius para inteiro. A mensagem deve estar formatada da seguinte maneira:
# 86 graus Fahrenheit são 30 graus Celsius.

# Lê a temperatura em Fahrenheit
F = int (input("Digite a temperatura em graus Fahrenheit: "))

# Calcula a conversão para Celsius
C = int ((F - 32) * (5/9))

# imprime o resultado na tela
print(f"{F} graus Fahrenheit são {C} graus Celsius.")