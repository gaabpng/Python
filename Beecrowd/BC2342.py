import operator

value = int(input())
ops = {"+": operator.add, "*": operator.mul}

x, op, y = map(str, input().split())

x = int(x)
y = int(y)

result = ops[op](x, y)

if result <= value:
    print("OK")
else:
    print("OVERFLOW")