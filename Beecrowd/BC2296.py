import sys
entrada = sys.stdin.read
dados = entrada().strip().split('\n')

N = int(dados[0])
menor_esforco = float('inf')
melhor_trilha = -1

for i in range(1, N + 1):
    dados_trilha = list(map(int, dados[i].split()))
    M = dados_trilha[0]
    alturas = dados_trilha[1:]
    
    esforco_normal = 0
    esforco_reverso = 0
    
    for j in range(1, M):
        if alturas[j] > alturas[j - 1]:
            esforco_normal += alturas[j] - alturas[j - 1]
        if alturas[M - j - 1] > alturas[M - j]:
            esforco_reverso += alturas[M - j - 1] - alturas[M - j]
    
    menor_esforco_trilha = min(esforco_normal, esforco_reverso)
    
    if menor_esforco_trilha < menor_esforco:
        menor_esforco = menor_esforco_trilha
        melhor_trilha = i

print(melhor_trilha)
