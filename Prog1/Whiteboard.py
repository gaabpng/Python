linhas = 3
colunas = 3
matriz = []

for i in range(linhas):
    linha = []
    for j in range(colunas):
        valor = float(input())
        linha.append(valor)
    matriz.append(linha)
    
linha1 = matriz[0][0:3]
linha1 = sum(linha1)
print(linha1)

linha2 = matriz[1][0:3]
linha2 = sum(linha2)
print(linha2)

linha3 = matriz[2][0:3]
linha3 = sum(linha3)
print(linha3)

resultado = linha1+linha2+linha3
print(resultado)
