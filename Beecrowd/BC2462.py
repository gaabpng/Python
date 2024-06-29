horarios = list(map(str, input().split()))

for i in range (len(horarios)):
    horarios[i] = horarios[i].split(":")

Partida_a_b = [int(horarios[0][0]), int(horarios[0][1])]
Chegada_a_b = [int(horarios[1][0]), int(horarios[1][1])]
Partida_b_a = [int(horarios[2][0]), int(horarios[2][1])]
Chegada_b_a = [int(horarios[3][0]), int(horarios[3][1])]

trajeto_a_b = (Chegada_a_b[0] * 60 + Chegada_a_b[1]) - (Partida_a_b[0] * 60 + Partida_a_b[1])
trajeto_b_a = (Chegada_b_a[0] * 60 + Chegada_b_a[1]) - (Partida_b_a[0] * 60 + Partida_b_a[1])

fuso_horario = 0

if trajeto_a_b < trajeto_b_a:
    fuso_horario = trajeto_b_a - trajeto_a_b

if trajeto_a_b > trajeto_b_a:
    fuso_horario = trajeto_a_b - trajeto_b_a

total = trajeto_a_b + fuso_horario

print(total, total)