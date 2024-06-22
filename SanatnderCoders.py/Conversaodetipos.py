#Converter uma variavel para outro tipo 
# int
# str
# float
# bool

idade = '22' 
print(idade, type(idade)) #assim mostra o tipo da viariavel

idade_inteira = int(idade)
print(idade_inteira, type(idade_inteira)) 
#aqui esta uma conversão de variavel de str para int

#agora com input (quando o usuario interage)
#altura = input("Informe a sua altura: ")
#print(altura, type(altura))
#a resposta no terminal deu type int e esta errado esse numero é type float
#para que aconteça uma conversão de type correto (independente da resposta do usuario)
#devemos por o type antes do input

altura = float( input("Informe a sua altura: "))
print(altura, type(altura))
#responta = <class 'float'
