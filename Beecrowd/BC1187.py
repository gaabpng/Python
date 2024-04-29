#Não Resolvido
linhas = 12
colunas = 12
matriz = []

op = input()
for i in range(linhas):
    linha = []
    for j in range(colunas):
        valor = float(input())
        linha.append(valor)
    matriz.append(linha)
    
linha1 = matriz[0][1:10]
linha1 = sum(linha1)

linha2 = matriz[1][2:9]
linha2 = sum(linha2)

linha3 = matriz[2][3:8]
linha3 = sum(linha3)

linha4 = matriz[3][4:7]
linha4 = sum(linha4)

linha5 = matriz[4][5:6]
linha5 = sum(linha5)

resultado = float(linha1+linha2+linha3+linha4+linha5)
if op == "S":
    print("{:.1f}".format(resultado))
else:
    resultado = resultado/30
    print("{:.1f}".format(resultado))