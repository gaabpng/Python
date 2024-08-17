def comparar_prefixo(pal1, pal2):
    pal1 = list(pal1)
    pal2 = list(pal2)
    contador = 0

    for i in range(min(len(pal1), len(pal2))):
        if pal1[i] == pal2[i]:
            contador += 1
        else:
            break
    
    print(contador)

letras_1 = input()
pal1 = input()
letras_2 = input()
pal2 = input()

comparar_prefixo(pal1, pal2)
