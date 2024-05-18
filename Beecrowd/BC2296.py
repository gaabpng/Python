import sys
Numero_de_trilhas = int(input())
trilhas = []
distância_das_trilhas = []
menor_trilha = sys.maxsize 
trilha_atual=0

for i in range(Numero_de_trilhas):
    trilhas.append(list(map(int, input().split())))