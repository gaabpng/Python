import math

# Função
def bhaskara(entrada):
    #Coversão
    entrada = entrada.split()
    
    #Declarando Variáveis
    A = float(entrada[0])
    B = float(entrada[1])
    C = float(entrada[2])
    
    delta = B * B - (4 * A * C)
    if A != 0 and delta > 0:
        eq1 = (- B + math.sqrt(delta)) / 2 * A
        eq2 = (- B - math.sqrt(delta)) / 2 * A

        # CORREÇÃO
        eq1 = eq1 / 100
        eq2 = eq2 / 100

        
        # METODO 1
        # print ("R1 = {:.5f}".format(eq1))
        # print ("R2 = {:.5f}".format(eq2))

        # METODO 2
        print ("R1 =", eq1)
        print ("R2 =", eq2)

    else:
        print ("Impossivel calcular")


# Código Principal
entrada=input()
bhaskara(entrada)