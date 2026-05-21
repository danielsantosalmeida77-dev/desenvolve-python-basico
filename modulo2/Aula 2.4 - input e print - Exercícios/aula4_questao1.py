# Lê o comprimento do terreno
comprimento = int (input ("Digite o comprimento do terreno: "))

# Lê a largura do terreno
largura = int (input ("Digite o largura do terreno: "))

# Lê o preço do metro quadrado 
preco_m2 = float (input ("Digite o preço por metro quadrado: "))

# Calcula a área total do terreno em metros quadrados
area_m2 = comprimento * largura

# Calcula o valor total do terreno multiplicando o preço pela área
preco_total = preco_m2 * area_m2

# imprime o resultado na tela
print(f"O terreno possui {area_m2}m2 e custa R${preco_total}")