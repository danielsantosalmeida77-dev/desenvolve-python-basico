a = int(input("Digite um numero: "))
b = int(input("Digite um numero: "))

soma = a + b 
criterio = soma % 2 

print("A soma é par") if criterio == 0 else print ("A soma é impar")