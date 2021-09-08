# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos 2 e 3. 
# A solução será apresentada no próximo capítulo!
# Assista o vídeo com a execução do programa!

print("\n******************* Python Calculator *******************")
print("\n")

# imprimir opções 
print("Selecione a opção desejada: ")
print("\n")
print("\n******************* Opções Existentes *******************")
print("\n")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")
print("\n")
# pedir ao user a opção

opcao = int(input("Digite sua opção (apenas números: 1/2/3/4): "))

# numeros para calculadora funcionar
x = int(input("Digite o primeiro número: "))
y = int(input("Digite o segundo número: "))
       
# Tratar e iniciar as funções de acordo com a opção
# funções - Utilizei Lambda para simplicar o código
soma = lambda x,y: x+y
sub = lambda x,y: x-y
mult = lambda x,y: x*y
div = lambda x,y: x/y

# condições
if opcao == 1:
    print("O resultado da soma é: %s" %(soma(x,y)))
elif (opcao == 2):
    print("O resultado da subtração é: %s" %(sub(x,y)))
elif (opcao == 3):
    print("O resultado da multiplicação é: %s" %(mult(x,y)))
elif (opcao == 4):
    if x == 0 or y == 0:
        print("Não existe divisão por 0")
    else:
        print("O resultado da divisão é: %s" %(div(x,y)))
else:
    print("Opção de calculo escolhida de forma incorreta, você infomou: %s enquanto esperavamos opções 1/2/3/4" %(opcao))

