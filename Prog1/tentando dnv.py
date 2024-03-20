import random
baralho = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

def BubbleSort(baralho):
    embaralhado = random.shuffle(baralho)
    for i in range(len(baralho)):
        print(embaralhado)

BubbleSort(baralho)