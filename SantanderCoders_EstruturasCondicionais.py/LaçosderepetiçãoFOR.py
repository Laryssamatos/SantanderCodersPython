# For 
# no for podemos criar repetições de forma controlada 

'''
for variavel in range(10):
    #TRADUÇÃO: para(for) variavel dentro da faixa(range) faça tal coisa...
     print(variavel)
     # na terminal aparecera numeros de 0 a 9'''

#exemplo pratico MEDIA DE NOTAS 
soma = 0

for i in range(1, 4):
    nota = float(input(f"Informe sua nota {i}: "))
    # f string = f no print serve para acrescentar o {i} 
    # para que seja possivel injetar uma variavel nesse caso a i
    soma = soma + nota

print(soma)

'''
assim o resultado desse codigo vai mostar a media que o aluno tera
decorrente das 3 notas que sera cSCalculada
'''