Vo = int(input())
Acougue = int(input())
Farmacia = int(input())
Padaria = int(input())
Pagas = 0
monte=0

contas=[]
contas.append(Acougue)
contas.append(Farmacia)
contas.append(Padaria)

contas.sort()

if contas[0] <= Vo:
    monte=1
    Vo = Vo-contas[0]

if contas[1] <= Vo:
    monte=2
    Vo = Vo-contas[1]

if contas[2] <= Vo:
    monte=3
    Vo = Vo-contas[2]

print(monte)