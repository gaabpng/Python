a, b, c, d = input().split()

a = int(a)
b = int(b)
c = int(c)
d = int(d)

if b > c:
    if d > a:
       if c+d > a + b:
          if c > 0:
             if d > 0:
                if a%2 == 0:
                   print("Valores aceitos")
else:
    print("Valores nao aceitos")

