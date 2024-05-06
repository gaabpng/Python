nome = input("digite seu nome")
altura = float(input("digite sua altura"))
peso = float(input("digite seu peso"))
imc = peso/(altura   * altura)

if imc < 18.5:
    
    print("ola" , nome , " voce esta abaixo do peso")
    print("seu imc é de" , imc )
    
elif imc == 18.6  <= 24.9:
    print("ola" , nome , " Parabens vc esta no peso ideal")
    print("seu imc é de" , imc )
    
elif imc == 25.0 <= 29.9:
    print("ola" , nome , " voce esta levemente acima do peso")
    print("seu imc é de" , imc )
    
elif imc == 30.0 <= 34.9:
    print("ola" , nome , " voce com obesidade de grau 1")
    print("seu imc é de" , imc )   
    
elif imc == 35.0 <= 39.9:
    print("ola" , nome , " voce com obesidade de grau 2 (severa)")
    print("seu imc é de" , imc )
else: 
    print("ola" , nome , " voce com obesidade de grau 3(morbido")
    print("seu imc é de" , imc )