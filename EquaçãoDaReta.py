print ("Insira abaixo os valores de:")
a = float(input("X1:  "))
b = float(input("Y1:  "))
c = float(input("X2:  "))
d = float(input("Y2:  "))

# Fórmula da equação da reta
# a * d + b * x + c * y + (d * x + a * y + c * b) * -1

parte1 = a * d
parte2 = b # + x
parte3 = c # + y
parte4 = d * -1 # + x
parte5 = a * -1 # + y 
parte6 = c * b * -1

calculo1 = 0
calculo2 = 0
calculo3 = 0

calculo1 = parte1 + parte6 # N
calculo2 = parte2 + parte4 # X
calculo3 = parte3 + parte5 # Y

calculoFinal = str(calculo2) + "x + " + str(calculo3) + "y + " + str(calculo1)
print(calculoFinal) 

#=================================================================================================================

#trechos de código que nao deram certo

#calculo1 = 0
#calculo2 = parte3 + parte4 
#calculo3 = parte5 + str(parte6) 
#calculo4 = 0
#calculo5 = 0
#calculo6 = 0

#print("cálculo 1: " + str(parte1) + " + " + parte2)
#print("calculo 2: " + parte3 + " + " + parte4)
#print("calculo 3: " + parte5 + "+" + str(parte6))

#print (calculo1)
#print (calculo2)
#print (calculo3)

#parte2.replace ("x", "" )
#calculo1 = float(parte1) + float(parte2)

#if calculo1.count(x) & calculo2.count(x):
#    calculo1.replace ("x", "")
#    calculo1.replace ("x", "")
#    calculo2.replace ("x", "")
#    calculo2.replace ("x", "")
#    calculo4 = float(calculo1) + float(calculo2)

#cálculoFinal = cálculo1 + cálculo2 + cálculo3

#print (cálculoFinal)
