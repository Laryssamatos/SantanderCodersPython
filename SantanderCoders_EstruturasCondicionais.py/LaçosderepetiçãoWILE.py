#Laços de repetição ou loops
#for: Executa um bloco de código repetidamente para cada item em uma sequência (como uma lista ou uma string).
#while: Continua executando um bloco de código enquanto uma condição booleana for verdadeira.
'''
usados para executar um bloco de código repetidamente enquanto uma condição especificada é atendida. 
Eles são uma ferramenta fundamental para automatizar e repetir tarefas sem a necessidade de escrever o mesmo código várias vezes.
'''
# WILE
# exemplos com e sem while
numero_sorteado = 10
escolha_usuario = int(input("Escolha um numero entre 1 e 10: " ))

#com if e else
'''
if numero_sorteado == escolha_usuario:
   print("Acertou")
else: 
   print("Errou") 
   #apos isso sem tentativas mais. Sem repetiçao automatica
'''
# com while
while escolha_usuario != numero_sorteado:  #enquanto um numero escolhido for diferente do numero sorteado
    print("Errou, tente novamente...")

    escolha_usuario = int(input("Escolha um numero entre 1 e 10: " ))
print("Acertou! ")



