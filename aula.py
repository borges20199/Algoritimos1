# 3)

# x = 0
# v = [""] * 5
# while(x < len(v)):
#     v[x] = input(" Digite um nome:")
#     x = x + 1

# x = 0
# while(x < len(v)):
#         print("Os nomes são:", v[x])
#         x = x + 1


# 4)
# n = int(input(" Digite a quantia de números : "))
# v = [0] * n

# x = 0
# while(x < len(v)):
#     v[x] = int(input(" Digite um número: "))
#     x = x + 1
    
# x = 0
# while(x < len(v)):
#     print(v[x])
#     x = x + 1

# 5) 
# a)
# n = int(input(" Digite a quantia de números : "))
# v = [0] * n

# x = 0
# while(x < len(v)):
#     v[x] = int(input(" Digite um número: "))
#     x = x + 1

# x = n - 1
# while(x >= 0 ):
#     print(v[x])
#     x = x - 1

# B)
# soma = 0 
# n=int(input(" Digite a quantia de números : "))
# v = [0] * n

# x = 0
# while(x < len(v)):
#     v[x] = int(input(" Digite um número: "))
#     soma = v[x] + soma
#     x = x + 1
# print(soma)
    
# C)
# soma = 0
# n=int(input(" Digite a quantia de números : "))
# v = [0] * n

# x = 0
# while(x < len(v)):
#     v[x] = int(input(" Digite um número: "))
#     soma = v[x] + soma
#     media = soma/n
#     x = x + 1
# print(media)

# D)
# n = int(input(" Digite a quantia de números : "))
# v = [0] * n

# x = 0
# while(x < len(v)):
#     v[x] = int(input(" Digite um número: "))
#     x = x + 1

# x = 0
# while(x < len(v)):
#     if(x % 2 == 0):
#         print(v[x])
#     x = x + 1

# e)
# n = int(input(" Digite a quantia de números : "))
# inicio = int(input(" Digite o inicio da sequencia : "))
# final = int(input(" Digite o final da sequencia : "))

# v = [0] * n
# cont = 0
# while(cont < len(v)):
#     v[cont] = int(input(" Digite os números:"))
#     cont = cont + 1

# cont = inicio
# while(cont <= final):
#     print(v[cont])
#     cont = cont + 1

# F)
n = int(input(" Digite a quantia de números : "))
inicio = int(input(" Digite o inicio da sequencia : "))
final = int(input(" Digite o final da sequencia : "))
soma = 0
v = [0] * n
cont = 0
while(cont < len(v)):
    v[cont] = int(input(" Digite os números:"))
    cont = cont + 1

cont = inicio
while(cont <= final):
    print(v[cont])
    soma = soma + v[cont]
    cont = cont + 1
print(" A soma dos números desse intervalo é : ",soma)













