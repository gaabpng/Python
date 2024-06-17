pães_vendidos = int(input())
doces_vendidos = int(input())
bolos_vendidos = int(input())

#pontuação:
doces_vendidos = doces_vendidos * 2
bolos_vendidos = bolos_vendidos * 3

pontos = pães_vendidos + doces_vendidos + bolos_vendidos

if pontos >= 150:
    print("B")
elif pontos >= 120:
    print("D")
elif pontos >= 100:
    print("P")
else:
    print("N")