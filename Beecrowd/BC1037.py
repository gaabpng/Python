intervalo1 = (0, 25)
intervalo2 = (25.00001, 50)
intervalo3 = (50.00001, 75)
intervalo4 = (75.00001, 100)

def intervalo(entrada):
    entrada = float(entrada)
    if intervalo1[0] <= entrada <= intervalo1[1]:
        print ("Intervalo [0,25]")
    elif intervalo2[0] <= entrada <= intervalo2[1]:
        print ("Intervalo (25,50]")
    elif intervalo3[0] <= entrada <= intervalo3[1]:
        print ("Intervalo (50,75]")
    elif intervalo4[0] <= entrada <= intervalo4[1]:
        print ("Intervalo (75,100]")
    else:
        print ("Fora de intervalo")
entrada=input()
intervalo(entrada)