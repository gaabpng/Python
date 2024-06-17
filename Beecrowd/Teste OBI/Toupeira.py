numero_saloes, numero_tuneis = map(int, input().split())
caminhos = []
caminhos_invertidos = []
solucoes = 0

for i in range(numero_tuneis):
    caminhos.append(list(map(int, input().split())))

for i in range(len(caminhos)):
    caminhos_invertidos.append(caminhos[i][::-1])


sugestoes = int(input())
matriz_sugestoes = []
verificacao = []

for i in range(sugestoes):
    matriz_sugestoes.append(list(map(int, input().split())))

for i in range(len(matriz_sugestoes)):
    if matriz_sugestoes[i] in caminhos or caminhos_invertidos:
        verificacao.append("S")
    else:
        verificacao.append("N")

for i in range(0, len(verificacao)-1):
    if "N" not in verificacao[i]:
        solucoes= solucoes+1

print(solucoes)
        