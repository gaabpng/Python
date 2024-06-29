def calcular_lucro_maximo(N, C, cotacoes):
    max_lucro = 0
    
    for i in range(1, N):
        if cotacoes[i] > cotacoes[i - 1]:
            lucro = cotacoes[i] - cotacoes[i - 1] - C
            if lucro > 0:
                max_lucro += lucro
    
    return max_lucro

N, C = map(int, input().split())
cotacoes = list(map(int, input().split()))

resultado = calcular_lucro_maximo(N, C, cotacoes)

print(resultado)
