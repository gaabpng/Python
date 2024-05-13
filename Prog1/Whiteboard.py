colunas = 4
linhas = 4
matriz = []

for i in range(colunas):
    matriz.append([])
    for j in range(linhas):
        inserção = int(input(f"Digite o valor da linha {i+1} e coluna {j+1}: "))
        matriz[i].append(inserção)
        
print(matriz)