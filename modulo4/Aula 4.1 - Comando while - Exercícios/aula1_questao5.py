N = int(input("Digite a quantidade de respondentes: "))

soma_idades = 0
contador = 0 

while contador < N:

    idade = int(input(f"Digite a idade do respondente: "))
    soma_idades = soma_idades + idade
    contador = contador + 1

if N > 0:
    media = soma_idades / N
    print(f"\nA média de idade dos respondentes é: {media:.1f} anos")
