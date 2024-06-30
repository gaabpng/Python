L, C, M, N = map(int,input().split()) #matriz LxC, colheita MxN
matriz = []
for e in range (L): #recebe os valores da matriz, linha por linha
    matriz.append(list(map(int,input().split())))
#matriz auxiliar:
A = [[0]*C for _ in range (L)] #matriz auxiliar
A[0][0] = matriz[0][0] #elemento 0,0
for j in range (1,C): #linha 0 
    A[0][j] = matriz[0][j] + A[0][j-1] 
for i in range (1,L): #a partir da linha 1
    A[i][0] = A[i-1][0] + matriz[i][0]
    for j in range (1,C):
        A[i][j] = A[i][j-1] + A[i-1][j] - A[i-1][j-1] + matriz[i][j]

maior = 0
for i in range(L - M + 1):
    for j in range(C - N + 1):
        if i == 0 and j == 0:
            atual = A[M-1][N-1]
        elif i == 0:
            atual = A[M-1][j+N-1] - A[M-1][j-1]
        elif j == 0:
            atual = A[i+M-1][N-1] - A[i-1][N-1]
        else:
            atual = A[i+M-1][j+N-1] - A[i+M-1][j-1] - A[i-1][j+N-1] + A[i-1][j-1]
        
        if atual > maior:
            maior = atual
print(maior)