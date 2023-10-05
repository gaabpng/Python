inp = int(input())

hor = 0
min = 0
seg = 0

while inp >= 3600:
    inp = inp - 3600
    hor = hor + 1

while inp >= 60:
    inp = inp - 60
    min = min + 1

while inp > 0:
    inp = inp - 1
    seg = seg + 1

print (str(hor) + ":" + str(min) + ":" + str(seg))