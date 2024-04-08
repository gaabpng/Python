# AINDA NÃO RESOLVIDO
notas = input().split()
notas = [float(i) for i in notas]

def calcular_media():
    media = ((notas[0] * 2) + (notas[1] * 3) + (notas[2] * 4) + notas[3]) / 10
    print ("Media: {:.1f}".format(media))
    
    if media >= 7:
        print("Aluno aprovado.")
    elif media < 5:
        print("Aluno reprovado.")
    else:
        print("Aluno em exame.")
        novo_exame = float(input("Nota do exame: "))
        media = (media + novo_exame) / 2
        if media > 5:
            print("Aluno Aprovado.")
        else:
            print("Aluno Reprovado.")
        print("Media final: {:.1f}".format(media))    
        
calcular_media()