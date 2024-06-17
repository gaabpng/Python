import sys
input = sys.stdin.read
data = input().strip().split('\n')

c = 0
i = 0
while True:
    P, R = map(int, data[i].split())
    if P == 0 and R == 0:
        break
    c += 1
    i += 1
    ordem = list(map(int, data[i].split()))
    vivos = ordem[:]
    
    for _ in range(R):
        i += 1
        rodada = list(map(int, data[i].split()))
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

    i += 1