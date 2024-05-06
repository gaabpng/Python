def calcular_esforco_subida(altitudes):
    esforco = 0
    for i in range(1, len(altitudes)):
        if altitudes[i] > altitudes[i - 1]:
            esforco += altitudes[i] - altitudes[i - 1]
    return esforco

N = int(input())

melhor_trilha = 1
menor_esforco = float('inf')

for trilha_id in range(1, N + 1):
    descricao = input().split()
    M = int(descricao[0])
    altitudes = list(map(int, descricao[1:]))

    esforco = calcular_esforco_subida(altitudes)

    if esforco < menor_esforco or (esforco == menor_esforco and trilha_id < melhor_trilha):
        melhor_trilha = trilha_id
        menor_esforco = esforco

print(melhor_trilha)
