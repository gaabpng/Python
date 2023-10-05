dist = int(input())

velocidade = 90 - 60  # Velocidade do carro Y - Velocidade do carro X

horas = dist / velocidade

minutos = horas * 60
minutos = int(minutos)

print(str(minutos) +" minutos")