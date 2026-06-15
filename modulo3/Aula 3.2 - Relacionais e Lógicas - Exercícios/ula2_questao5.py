genero = input("Qual seu gênero?(M ou F) ")
idade = int(input("Qual sua idade? "))
tempo = int(input("Qual seu tempo de contribuição? "))

pode_aposentar = (
    ((genero == "F" and idade > 60) or (genero == "M" and idade > 65)) or  
    (tempo >= 30) or                                              
    (idade >= 60 and tempo >= 25)
)

print(pode_aposentar)