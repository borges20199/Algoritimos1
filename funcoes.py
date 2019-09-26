# from random import randint
#
#
#
#
# def NumeroAleatorio(num):
#     return randint(1,num)
#
#
#
#
# def pedirNumero():
#     x = int(input(" Digite um número de um mês do ano:  "))
#     return x
#
# def obterMes(x):
#     if(x == 1 ):
#         mes ="Janeiro"
#     elif(x == 2 ):
#         mes ="Fevereiro"
#     elif(x == 3 ):
#         mes ="Março"
#     elif(x == 4 ):
#         mes ="Abril "
#     elif(x == 5 ):
#         mes = "Maio "
#     elif(x == 6 ):
#         mes ="Junho"
#     elif(x == 7 ):
#         mes ="Julho"
#     elif(x == 8 ):
#          mes ="Agosto"
#     elif(x == 9 ):
#          mes ="Setembro"
#     elif(x == 10 ):
#          mes ="Outubro"
#     elif(x == 11 ):
#          mes ="Novembro"
#     elif(x == 12 ):
#         mes ="Dezembro"
#     else:
#         mes = " mês inválido"
#     return mes

# ===================================================================
# ===================================================================


def opcaoMenu():
    p = int(input(" Escolha qual dos poligonos abaixo você deseja calcular a área: "))
    return p

def menuPrincipal():
    print("""
=-=-=-=-Menu dos Polígonos-=-=-=-=-


1. Quadrado

2. Retângulo

3. Triângulo

4. Trapézio

5. Sair

    """)



def areaPoligonos(p):
    if( p == 1 ):

        L = int(input("Digite o valor do lado do quadrado: "))

        A = L*L

        print(" A área do quadrado é ", A)

    elif( p == 2 ):

        a = int(input("Digite o valor da altura do retângulo: "))

        b = int(input("Digite o valor da base do retângulo: "))

        A = b*a

        print(" A área do retângulo é ", A)

    elif( p == 3 ):

        a = int(input("Digite o valor da altura do triângulo: "))

        b = int(input("Digite o valor da base do triângulo: "))

        A = b*a

        q = A / 2

        print(" A área do triângulo é ", q)


    elif( p == 4 ):

        B = int(input("Digite o valor da maior base do trapézio : "))

        b = int(input("Digite o valor da menor base do trapézio: "))

        h = int(input("Digite o valor da altura do trapézio: "))

        m = (B+h)*h

        n = m/2

        print(" A área do trapézio é ", n)

    # elif(p == 5 ):
    #     break


    else:
        print(" opção inválida")
# ===================================================================
# ===================================================================
