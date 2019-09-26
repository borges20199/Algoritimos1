


def exibirMensagem(x):
    print("valor de x: ", x)
    if (x <= 0):
        return 1
    else:
        return x * exibirMensagem(x-1)

# 10 - ( 9 - ( 8 - ( 7 - ( 6 - ( 5 - ( 4 - ( 3 - ( 2 - ( 1 - ( 0 )  ) ) )  ) ) ) ) ) )


print(exibirMensagem(5))
