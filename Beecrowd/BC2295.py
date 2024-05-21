Preco_Alcool, Preco_Gasolina, Rendimento_Alcool, Rendimento_Gasolina = map(float, input().split())

if Preco_Alcool / Rendimento_Alcool < Preco_Gasolina / Rendimento_Gasolina:
    print("A")
else:
    print("G")