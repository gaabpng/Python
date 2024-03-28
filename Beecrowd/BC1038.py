pedido = input().split()
pedido = [int(val) for val in pedido]
precos = [4, 4.5, 5, 2, 1.5]

total = precos[pedido[0]-1] * pedido[1]

print("Total: R$ {:.2f}".format(total))