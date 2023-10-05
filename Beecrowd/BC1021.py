# input
valor_init = float(input())

# declaração
valor = int(valor_init * 100)  # Convertendo para centavos
n100 = 0
n50 = 0
n20 = 0
n10 = 0
n5 = 0
n2 = 0
m100 = 0
m50 = 0
m25 = 0
m10 = 0
m5 = 0
m1 = 0

# código
while valor >= 10000:
    valor -= 10000
    n100 += 1

while valor >= 5000:
    valor -= 5000
    n50 += 1

while valor >= 2000:
    valor -= 2000
    n20 += 1

while valor >= 1000:
    valor -= 1000
    n10 += 1

while valor >= 500:
    valor -= 500
    n5 += 1

while valor >= 200:
    valor -= 200
    n2 += 1

while valor >= 100:
    valor -= 100
    m100 += 1

while valor >= 50:
    valor -= 50
    m50 += 1

while valor >= 25:
    valor -= 25
    m25 += 1

while valor >= 10:
    valor -= 10
    m10 += 1

while valor >= 5:
    valor -= 5
    m5 += 1

while valor >= 1:
    valor -= 1
    m1 += 1

# apresentação
print("NOTAS:")
print(str(n100) + " nota(s) de R$ 100.00")
print(str(n50) + " nota(s) de R$ 50.00")
print(str(n20) + " nota(s) de R$ 20.00")
print(str(n10) + " nota(s) de R$ 10.00")
print(str(n5) + " nota(s) de R$ 5.00")
print(str(n2) + " nota(s) de R$ 2.00")

print("MOEDAS:")
print(str(m100) + " moeda(s) de R$ 1.00")
print(str(m50) + " moeda(s) de R$ 0.50")
print(str(m25) + " moeda(s) de R$ 0.25")
print(str(m10) + " moeda(s) de R$ 0.10")
print(str(m5) + " moeda(s) de R$ 0.05")
print(str(m1) + " moeda(s) de R$ 0.01")