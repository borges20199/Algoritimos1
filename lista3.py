# Vetor

x = 0

v = [0] * 101
while( x < 101 ):
    v[x] = x
    x = x + 1
# A)
# x = 0
# while( x < 101 ):
#     print(v[x])
#     x = x + 1

# B)
# x = 100
# while( x > 0 ):
#     print(v[x])
#     x = x - 1

#C)
# x = 0
# dobro = 0
# while( x < 101 ):
#     dobro = v[x] * 2
#     print(v[x], "*", "2", "=", dobro)
#     x = x + 1

#D)
# x = 0
# soma = 1
# while( x < 101 ):
#     soma = v[x] + soma
#     x = x + 1
# print(soma)

#E)
# x = 0
# soma = 1
# while( x < 101 ):
#     soma = v[x] + soma
#     media = soma / 100
#     x = x + 1
# print(media)

#F)
# x = 0
# while( x < 101 ):
#     if( x % 2==0 ):
#         print(x)
#     x = x + 1
