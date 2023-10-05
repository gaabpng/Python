rend = 12

tempo = float(input())
vel = float(input())

dist = vel * tempo
total = dist / rend

print("{:.3f}".format(total))