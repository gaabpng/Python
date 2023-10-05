inp = int(input())

ano = 0
mes = 0
dia = 0

while inp >= 365:
    inp = inp - 365
    ano = ano + 1

while inp >= 30:
    inp = inp - 30
    mes = mes + 1

while inp > 0:
    inp = inp - 1
    dia = dia + 1

print(str(ano) + " ano(s)")
print(str(mes) + " mes(es)")
print(str(dia) + " dia(s)")
