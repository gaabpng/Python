Value = int(input())
teste = 0

while Value != 0:
    
    I = 0 # notas de 50
    J = 0 # notas de 10
    K = 0 # notas de 5
    L = 0 # notas de 1
    
    teste +=1
    
    while Value >= 50:
        Value -= 50
        I += 1
    
    while Value >= 10:
        Value -= 10
        J += 1
        
    while Value >= 5:
        Value -= 5
        K += 1
        
    while Value >= 1:
        Value -= 1
        L += 1
    
    print("Teste",teste)
    print(I, J, K, L)
    print()
    Value = int(input())