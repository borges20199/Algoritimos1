
# array - unidimensional ou multidimensional
#              vetor           matriz
#
# vetor: - Conjunto de dados/valores
#         - Possuem uma sequencia
#         - Todos os valores são do mesmo tipo de dado - /string, inteiro, float, boleano/
# indici é um número vque indica a posição dentro do meu vetor = tamanho - 1

idades = [0] * 6
idades[3] = 18
idades[5] = 1

print(idades)
print(idades[3])

# nome = [""] * 35
# salario = [0.0] * 35
# passou de ano = [false] * 35

cont = 0
while(cont < len(idades)):
    idades[cont] = int(input("idade:"))
    cont = cont + 1
print(idades[0], idades[1], idades[2], idades[3], idades[4], idades[5])
