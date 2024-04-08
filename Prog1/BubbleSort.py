import random
debug = True

# Sub-programa
def BubbleSort(baralho):
    numero_de_cartas = len(baralho)
    for i in range(numero_de_cartas):
        for j in range (0, numero_de_cartas-i-1):
            if baralho[j] > baralho[j+1]:
                baralho[j], baralho[j+1] = baralho[j+1], baralho[j]
                print(baralho)
                
    return baralho

# Declarações
baralho = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
baralho_embaralhado = baralho[:]
random.shuffle(baralho_embaralhado)

# Debug
if debug == True :
    print("Baralho organizado", baralho)
    print("Embaralhado", baralho_embaralhado)
    print("")

print("Baralho ordenado:", BubbleSort(baralho_embaralhado))