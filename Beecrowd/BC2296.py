import sys
#ler quantidade N de valores
Numero_de_trilhas = int(input())

#sentinela
custo = sys.maxsize 
indice_de_menor_custo = None

#ler valores da trilha1, ou seja, M e Hi
for i in range(1, Numero_de_trilhas-1):
    lista_de_valores = list(map(int, input().split()))
    
    


#Calcular custo de ida (CIda) da T1 
#Calcular custo de volta (CVolta) da T1 
#Calcular o custo da T1, sendo esse o menor entre Cida e Cvolta
#Atualizar a anotação de menor custo, caso CustoT1 seja menor que o menor custo anotado

#repetir o processo para a T2
#repetir o processo para a T3
#repetir o processo até Tn