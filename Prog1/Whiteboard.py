entrada = 0
lista = []
menorvalor = 0
maiorvalor = 0
media = 0

while entrada != "FIM":
    entrada = input()
    lista.append(entrada)
    
for i in range(len(lista)-1):
    if lista[i] < lista[i+1]:
        menorvalor = lista[i]
        
    if lista[i] > lista[i+1]:
        maiorvalor = lista[i]
        
for i in range(len(lista)):
    media += lista[i]
    
media = media/len(lista)

print("Menor valor: {}".format(menorvalor))
print("Maior valor: {}".format(maiorvalor))
print("Média: {:.2f}".format(media))
