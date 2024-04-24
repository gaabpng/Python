# Não Resolvido
def SomaImpar():
    Inteiro1 = int(input())
    Inteiro2 = int(input())
    Saida = 0
    
    if Inteiro1 == Inteiro2:
        print(0)
    else:   
        if Inteiro1 % 2 != 0:
            if Inteiro1 > Inteiro2:
                for i in range(Inteiro1, Inteiro2, 2):
                    Saida += i
            else:
                for i in range(Inteiro1, Inteiro2, -2):
                    Saida += i
                
        else:
            if Inteiro2 > 0:
                for i in range(Inteiro1, Inteiro2+1, 2):
                    Saida += i
            else:
                for i in range(Inteiro1, Inteiro2+1, -2):
                    Saida += i   
    print(Saida)  
SomaImpar()