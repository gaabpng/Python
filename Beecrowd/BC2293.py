linhas, colunas = map(int, input().split())
matriz = []

for _ in range(linhas):
    matriz.append(list(map(int, input().split())))

maior_valor = sum(matriz[0])

for i in range(1, linhas):
    soma_linha = sum(matriz[i])
    if soma_linha > maior_valor:
        maior_valor = soma_linha

for j in range(colunas):
    soma_coluna = sum(matriz[i][j] for i in range(linhas))
    if soma_coluna > maior_valor:
        maior_valor = soma_coluna

print(maior_valor)