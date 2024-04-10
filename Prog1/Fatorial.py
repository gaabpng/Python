valor = int(input())

fatorial = 1

while valor > 1:
    fatorial *= valor
    valor -= 1
    
print(fatorial)