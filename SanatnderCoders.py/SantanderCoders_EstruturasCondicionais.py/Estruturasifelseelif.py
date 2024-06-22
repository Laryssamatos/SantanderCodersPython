#Estruturas de controle de fluxo no Python que permitem direcionar o caminho que um programa irá seguir durante sua execução
#E existe dois tipos as condicionais e laços de repetição

#as CONDICIONAIS decidem ooque vai ser executado no codigo ou não
#Estruturas Condicionais: if, elif, else: base em condições booleanas.
# if = se
# else = do contrario 
# elif = é um else if intermediario

'''
if condição1:
    # Executa este bloco se condição1 for verdadeira
elif condição2:
    # Executa este bloco se condição1 for falsa e condição2 for verdadeira
else:
    # Executa este bloco se todas as condições anteriores forem falsas
'''

idade = 18

if idade >= 18:
    #if = se (idade for maior ou igual (booleano))
    print("Voce é maior. ")
else: 
    print("voce é menor. ")

#importante ter o espaço dentro do if e do else para que o codigo funcione dentro dele
#A respota no terminal vai de acordo com a idade na variavel IDADE


'''
Imprima "Aprovado" caso o aluno tenha uma media superior ou igual a 7
e "Reprovado" se a media for inferior ou seja menor que 7
'''
Media = 7 

if Media >= 7:
   print("Aprovado")
else: 
    print("Reprovado")

#COM INPUT

Media2 = float(input("Informe a media do aluno: "))
if Media2 >= 7:
    print("Aprovado")
else: 
    print("Reprovado")

#COM elif

Media3 = float(input("Informe a media do aluno: "))

if Media3 >= 7:
    print("Aprovado")
elif Media3 >= 5: # media menor que 7 e maior ou igual(>=) a 5
    print("Recuperação")
else: 
    print("Reprovado")




#OPERAÇÕES CONJUNTAS 
'''
Duas condiçoes para o mesmo bloco 

ex: um aluno para ser aprovado precisa ter
uma media maior que 7 
e presença de 70% nas aulas 
se não estiver ok com essas duas condições
não sera aprovado 

#pode se usar o and (e) no caso de ser isso E aquilo
#pode ser or (ou) no caso de ser isso OU aquilo

media = 10
presença = 100

if media >= 7 and presença >= 70:
    print("Aprovado! ")
else:
    print("Reprovado")
'''