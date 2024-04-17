def ParOuImpar(Teste = 0):
    NumeroDePartidas = int(input())
    Teste = Teste + 1
    if NumeroDePartidas == 0:
        return None
    
    Jogador1 = input()
    Jogador2 = input()
    print ("Teste", Teste)
    
    for i in range(NumeroDePartidas):
        Aposta1, Aposta2 = map(int, input().split())
        
        if (Aposta1 + Aposta2) % 2 == 0:
           print(Jogador1)
        else:
            print(Jogador2)
            
    print()
    ParOuImpar(Teste)

ParOuImpar()