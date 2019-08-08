# def pedeMostra():
#     x = int(input(" Digite um número "))
#     print('o número digitado foi', x)
# pedeMostra()

# def exibirMenu():
#     print("""
#     ****Menu Principal****         
#         1. incluir
#         2. alterar
#         3. excluir 
#         4. sair 
#     """)
# exibirMenu()


######lista de exercicos#######
# ex 1)
# a)

def somar():
    x = int(input(" Digite o primeiro número: "))
    y = int(input(" Digite o segundo número: "))
    soma = (x + y)
    print(" a soma desses números é: ", soma)
# somar()

# b)


def multiplicar():
    x = int(input(" Digite o primeiro número: "))
    y = int(input(" Digite o segundo número: "))
    mlt = (x * y)
    print(" a Multiplicação desses números é: ", mlt)
# multiplicar()


#c)

import math
def raiz():
    x = int(input(" Digite um número: "))
    y = math.sqrt(x)
    print(y)
# raiz()

#d)


def potencia():
    x = int(input(" Digite um número: "))
    y = int(input(" Digite um número: "))
    z = math.pow(x,y)
    print(Z)
# potencia()

#e)

def tabuada():
    x = int(input(" Digite um número: "))
    cont = 1
    while(cont <= 10 ):
        multi = cont * x
        print(cont,"*", x, "=", multi)
        cont = cont + 1
# tabuada()

#2)
def menuOperacoes():
    print("""
    Menu Principal 
    1.Soma
    2.Multiplicação
    3.Raiz
    4.Potência
    5.Tabuada
    6.Sair
    """)





while(True):    
    menuOperacoes()
    opcao = int(input("Escolha a opção desejada:"))
    if(opcao == 1):
        somar()
    elif(opcao == 2):
        multiplicar()
    elif(opcao == 3):
        raiz()
    elif(opcao == 4):
        potencia()
    elif(opcao == 5):
        tabuada()
    elif(opcao == 6):
        break
    else:
        print(" Opção invalida")
        

