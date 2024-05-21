c = 0

while True:
    P, R = map(int, input().split())
    if P == 0 and R == 0:
        break
    
    c += 1
    ordem = list(map(int, input().split()))
    vivos = ordem[:]
    
    for _ in range(R):
        rodada = list(map(int, input().split()))
        N = rodada[0]
        J = rodada[1]
        acoes = rodada[2:]
        
        removidos = []
        for j in range(N):
            if acoes[j] != J:
                removidos.append(vivos[j])
        
        vivos = [v for v in vivos if v not in removidos]
    
    print(f'Teste {c}')
    print(vivos[0])
    print()
