N = int(input("Digite a quantidade de experimentos: "))

total_sapos = 0
total_ratos = 0
total_coelhos = 0

contador = 0 

while contador < N:
  
    quantia = int(input("Quantidade de cobaias: "))
    tipo = input("Tipo (S para Sapo, R para Rato, C para Coelho): ").upper().strip()
   
    if tipo == "S":
        total_sapos = total_sapos + quantia
    elif tipo == "R":
        total_ratos = total_ratos + quantia
    elif tipo == "C":
        total_coelhos = total_coelhos + quantia
        
    contador = contador + 1

total_geral = total_sapos + total_ratos + total_coelhos
perc_coelhos = (total_coelhos / total_geral) * 100
perc_ratos = (total_ratos / total_geral) * 100
perc_sapos = (total_sapos / total_geral) * 100

print("Total:", total_geral, "cobaias")
print("Total de coelhos:", total_coelhos)
print("Total de ratos:", total_ratos)
print("Total de sapos:", total_sapos)

if total_geral > 0:
    
    print("Percentual de coelhos:",perc_coelhos, "%" )
    print("Percentual de ratos:",perc_sapos, "%")
    print("Percentual de sapos:,", perc_sapos, "%")