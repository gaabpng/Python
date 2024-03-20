import random

def BubbleSort(baralho):
    n = len(baralho)
    for i in range(n):
        for j in range(0, n-i-1):
            if baralho[j] > baralho[j+1]:
                baralho[j], baralho[j+1] = baralho[j+1], baralho[j]

    return baralho

baralho = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
baralho_embaralhado = baralho[:]
random.shuffle(baralho_embaralhado)
print("Baralho embaralhado:", baralho_embaralhado)
print("Baralho ordenado:", BubbleSort(baralho_embaralhado)) 
