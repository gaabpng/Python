Base = "AATCTGCAC"

matriz = [["A", "T"],
          ["C", "G"],
          ["G", "C"],
          ["T", "A"]]

Cadeia = list(Base)
for i in range(len(Cadeia)):
    for j in range(len(matriz)):
        if Cadeia[i] == matriz[j][0]:
            Cadeia[i] = matriz[j][1]
            break
        
print()
print("".join(Cadeia))