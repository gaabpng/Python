n = int(input())   
fat = 1
for n in range(n, 1, -1):
    fat *= n
print(fat)