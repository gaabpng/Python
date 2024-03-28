pedido = input().split()
pedido = [int(val) for val in pedido]
precos = [4, 4.5, 5, 2, 1.5]
total = precos[pedido[0]-1] * pedido[1]
print("Total: R$ {:.2f}".format(total))



# PROGRAMA QUE EU FIZ PQ NÃO LI O CARALHO DO ENUNCIADO
#
# def comanda(pedido, precos, conta, total):
#     for i in pedido:
#         conta.append(precos[i-1])
    
#     total = sum(conta)
#     print("Total: R$ {:.2f}".format(total))
    
# pedido = input().split()
# pedido = [int(val) for val in pedido]
# conta = []
# precos = [4, 4.5, 5, 2, 1.5]
# total = 0        

# comanda(pedido, precos, conta, total)