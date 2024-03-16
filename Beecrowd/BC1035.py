# Requisitos
req1 = False # B maior que C
req2 = False # D maior que A
req3 = False # C + D maior que A + B
req4 = False # C e D maior que 0
req5 = False # A é par

# Function
def regras(entrada):
    valores = entrada.split() 
    A = int(valores[0])
    B = int(valores[1])
    C = int(valores[2])
    D = int(valores[3])
    
    if B > C:
        global req1 
        req1 = True
    
    if D > A:
        global req2
        req2 = True

    if C + D > A + B:
        global req3
        req3 = True
    
    if C > 0 and D > 0: 
        global req4
        req4 = True
    
    if A % 2 == 0:
        global req5
        req5 = True
    
    if req1 and req2 and req3 and req4 and req5:  
        print("Valores aceitos")
    else:
        print("Valores não aceitos")

# Main Code
entrada = input()
regras(entrada)
