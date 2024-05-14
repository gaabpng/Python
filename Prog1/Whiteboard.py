telefone = 0
presente = 0
moraPerto = 0
devia = 0
trabalhou = 0

telefone = input("telefonou?")
if telefone == "Sim":
    telefone = 1
    
presente = input("deu presente?")
if presente == "Sim":
    presente = 1
    
moraPerto = input("mora perto?")
if moraPerto == "Sim":
    moraPerto = 1

devia = input("devia?")
if devia == "Sim":
    devia = 1
    
trabalhou = input("trabalhou?")
if trabalhou == "Sim":
    trabalhou = 1

if telefone + presente + moraPerto + devia + trabalhou <= 1:
    print("Inocente")
else:
    if telefone + presente + moraPerto + devia + trabalhou == 2:
        print("Suspeito")
    else:
        if telefone + presente + moraPerto + devia + trabalhou == 3 or telefone + presente + moraPerto + devia + trabalhou == 4:
            print("Cúmplice")
        else:
            print("Assassino")