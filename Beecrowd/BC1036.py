#AINDA NÃO RESOLVIDO

# Função
def bhaskara(entrada):
    #Coversão
    entrada = entrada.split()
    
    #Declarando Variáveis
    A = float(entrada[0])
    B = float(entrada[1])
    C = float(entrada[2])
    
    delta = B ** 2 
    delta1 = delta * (-1 * (4 * A * C))
    if A != 0 and delta1 > 0:
        eq1 = (- B + (delta1 ** 0.5)) / 2 * A
        eq2 = (- B - (delta1 ** 0.5)) / 2 * A

        # CORREÇÃO
        eq1 = eq1 / 100
        eq2 = eq2 / 100

        
        # METODO 1
        # print ("R1 = {:.5f}".format(eq1))
        # print ("R2 = {:.5f}".format(eq2))

        # METODO 2      
        print ("R1 = {:.5f}".format(eq1))
        print ("R2 = {:.5f}".format(eq2))

    else:
        print ("Impossivel calcular")


# Código Principal
entrada=input()
bhaskara(entrada)