predio = [int(input()) for i in range(3)]

tempo_gasto = [
    predio[0]*4 + predio[1]*2,
    predio[0]*2 + predio[2]*2,
    predio[1]*2 + predio[2]*4
]

print(min(tempo_gasto))
