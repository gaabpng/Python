linhas = 12
colunas = 12
linhas = 12

matriz = []
op = input()

for i in range(colunas):
    matriz.append([])
    for j in range(linhas):
        valor = float(input())
        matriz[i].append(valor)
    
linha1 = sum(matriz[0][1:11])
linha2 = sum(matriz[1][2:10])
linha3 = sum(matriz[2][3:9])
linha4 = sum(matriz[3][4:8])
linha5 = sum(matriz[4][5:7])

resultado = linha1+linha2+linha3+linha4+linha5

if op == "S":
    print("{:.1f}".format(resultado))
else:
    resultado = resultado/30
    print("{:.1f}".format(resultado))
