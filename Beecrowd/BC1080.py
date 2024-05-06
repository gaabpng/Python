valores = []
for i in range(100):
    valor = int(input())
    valores.append(valor)

maior_valor = max(valores)
posicao_maior_valor = valores.index(maior_valor) + 1

print(maior_valor)
print(posicao_maior_valor)
