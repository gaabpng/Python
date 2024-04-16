import math

A, B, C = map(float, input().split())
delta = B**2 - 4*A*C

if delta >= 0 and A != 0:
    raiz1 = (-B + math.sqrt(delta)) / (2*A)
    raiz2 = (-B - math.sqrt(delta)) / (2*A)
    
    print("R1 = {:.5f}".format(raiz1))
    print("R2 = {:.5f}".format(raiz2))
else:
    print("Impossivel calcular")