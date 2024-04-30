def soma_impares_entre_numeros(x, y):
    if x > y:
        x, y = y, x
    
    soma = 0
    for num in range(x+1, y):
        if num % 2 != 0:
            soma += num
    return soma

x = int(input())
y = int(input())

print(soma_impares_entre_numeros(x, y))
