#  < maior
#  > menor
#  <= maior ou igual
#  >= menor ou igual
#  == igual
#  != diferente
# print("ok")
# 1) Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
#
# x = int(input("Digite um numero:"))
# if( x >= 0 ):
#     print("O número é positivo")
# else:
#     print("o número é negativo")
#
# 2) Faça um Programa que peça dois números e imprima o maior deles.
#
# x = int(input("digite um número:"))
# y = int(input("digite um número:"))
# if( x > y ):
#     print(" Esse número é o maior ", x)
# else:
#     print(" Esse número é o maior ", y)
#
# 3)Faça um programa que peça um valor e informe na tela se o número é par ou ímpar.
#
# x = int(input("Digite um número:"))
# if(x % 2 == 0):
#     print(" Esse número é par ")
# else:
#     print(" Esse número é impar ")
#
# 4)Faça um Programa que peça um número e informe se este número é múltiplo de 3
# x = int(input("Digite um número qualquer:"))
# if(x % 3 == 0 ):
#     print(" Esse número é multiplo de três ")
# else:
#     print(" Esse número não é multiplo de três ")
#
# 5)Faça um programa que peça dois números e informe se o primeiro é múltiplo do segundo.
# x = int(input(" Digite um numero qualquer: "))
# y = int(input(" Digite um numero qualquer: "))
# if( x % y == 0):
#     print(" Esses numeros são multiplos ")
# else:
#     print(" Esses numeros não são multiplos ")
#
# 6)Faça um Programa que verifique o sexo de uma pessoa. O usuário deve informar ‘F’ ou ‘M’ e o programa deve escrever “Feminino” ou “Masculino”, conforme a letra digitada.
# sexo = input(" Digite seu sexo sendo M ou F: ")
#
# if( sexo == "M" ):
#     print(" Você é do sexo Masculino " )
# else:
#     print(" Você é do sexo Feminino " )
#
# 7)Faça um algoritmo que leia os valores A, B, C e imprima na tela se a soma de A + B é maior que c
# a = int(input(" Digite um valor: "))
# b = int(input(" Digite um valor: "))
# c = int(input(" Digite um valor: "))
#
# soma = int( a + b )
#
# if( soma > c ):
#     print(" a soma de a + b é maior que c " )
# else:
#     print(" a soma de a + b é menor que c " )
#
# 8)Faça um algoritmo que peça um número e se ele for par some 5, se não, some 8.
# x = int(input(" Digite um número qualquer: "))
#
# if( x % 2== 0 ):
#     x = x + 5
#     print(" o numero é par  ", x)
# else:
#     x = x + 8
#     print(" o numero é impar  ", x)
# 9)Crie um programa que peça uma nota de trabalho e uma de prova (as duas de 0 a 100). Se a média aritmética das notas for maior ou igual a 60, escreva “Aprovado”, se não, “Reprovado”.
# np = int(input(" Digite a nota da sua prova: "))
# nt = int(input(" Digite a nota do seu trabalho: "))
#
# media = float(( np + nt )/2)
#
# if( media >= 60 ):
#     print(" Você está aprovado ! ")
# else:
#     print(" Você está reprovado ! ")
#
# 10)Construa um programa que recebe três valores, A, B e C. Em seguida, apresente na tela somente o maior deles.
# a = int(input(" Digite um número: "))
# b = int(input(" Digite um número: "))
# c = int(input(" Digite um número: "))
#
# if( a > b ):
#     if( a > c ):
#         print(" a é o maior ")
#     else:
#         print(" c é maior")
# else:
#     if( b > c):
#         print(" b é o maior ")
#     else:
#         print(" c é o maior ")
# 11)Construa um programa que recebe três valores, A, B e C. Em seguida, apresente na tela os números em ordem crescente.
# n1 = int(input(" Digite o numero 1 : "))
# n2 = int(input(" Digite o numero 2 : "))
# n3 = int(input(" Digite o numero 3 : "))
#
# if( n1 < n2 < n3 ):
#     print("  ")
#     print(" a ordem crescente é ", n1, n2, n3 )
#
# elif( n1 < n3 < n2):
#     print("  ")
#     print(" a ordem crescente é ", n1, n3, n2 )
#
# elif( n2 < n1 < n3 ):
#     print("  ")
#     print(" a ordem crescente é ", n2, n1, n3 )
#
# elif( n2 < n3 < n1 ):
#     print("a ordem crescente é ", n2, n3, n1 )
#
# elif( n3 < n1 < n2 ):
#     print("  ")
#     print("a ordem crescente é", n3, n1, n2 )
#
# elif( n3 < n2 < n1 ):
#     print("  ")
#     print("a ordem crescente é", n3, n2, n1 )




#
# idade = input(" Digite sua idade: ")
# idade = int(idade)
#
# if( idade < 0 ):
#     print(" essa idade não existe ! ")
# elif( idade > 3 ):
#     print(" Bebê detectado ! ")
# elif( idade <= 12 ):
#     print(" Criança ")
# elif( Idade < 18 ):
#     print(" Adolescente ! ")
# elif()


# ex 1
# print(" Cadastro de alunos ")
# print("""
# 1) cadastrar
# 2) Alterar
# 3) Excluir
# 4) Consultar
# 5) Imprimir relatório
#  """)
#
# opção = int(input(" O que deseja realizar? "))
#
# if( opção == 1 ):
#     print(" Você deseja realizar um cadastro de aluno ")
#
# elif( opção == 2 ):
#     print(" Você deseja alterar os dados do aluno  ")
#
# elif( opção == 3 ):
#     print(" Você deseja excluir os dados do aluno ")
#
# elif( opção == 4 ):
#     print(" Você deseja consultar os dados do aluno ")
#
# elif( opção == 5 ):
#     print(" Você deseja imprimir o relatório do aluno ")
#
# else:
#     print(" Esta opção é inválida ")

#operadores logicos

# x = 10
# y =20
# if( not (( x > 0 or y < 0 ) or x == 10)):
#     print(" verdadeira ")
# else:
#     print(" falso ")
