x = int(input(" Informe o valor inicial: "))
z = int(input(" Informe o valor final: "))
y = int(input(" Digite o valor a ser multiplicado: "))


cont = x

while( cont <= z ):
    tabuada = cont * z
    print(y , "*", cont, "=", tabuada)
    cont = cont + 1
