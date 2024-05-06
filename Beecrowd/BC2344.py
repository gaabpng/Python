nota = int(input())
conceito = ""

if nota == 0:
    conceito = "E"
    
if nota >= 1 and nota <= 35:
    conceito = "D"
    
if nota >= 36 and nota <= 60:
    conceito = "C"
    
if nota >= 61 and nota <= 85:
    conceito = "B"
    
if nota >= 86:
    conceito = "A"
    
print(conceito)