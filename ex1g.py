x = int(input(" Digite o primeiro valor: "))
y = int(input(" Digite o segundo valor: "))

cont = x

while( cont <= y ):
    if(cont % 2 != 0 ):
        print(cont)

    cont = cont + 1
