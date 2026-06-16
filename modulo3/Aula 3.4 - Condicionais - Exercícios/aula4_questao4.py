distancia = int(input("Digite a distância em km: "))
peso = int(input("Digite o peso do pacote: "))

if distancia <= 100:
    preco_por_kg = 1.00
else:
    if distancia <= 300:
         preco_por_kg = 1.50
    else:
        preco_por_kg = 2

frete = peso * preco_por_kg

if peso > 10:
    frete = frete + 10

print("Valor do frete: R$", frete)