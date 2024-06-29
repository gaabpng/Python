def mdc(a, b):
    while b:
        a, b = b, a % b
    return a

num1, div1, num2, div2 = map(int, input().split())

num_result = (num1 * div2) + (num2 * div1)
div_result = div1 * div2

gdc = mdc(num_result, div_result)
num_result_simpl = num_result // gdc
div_result_simpl = div_result // gdc

print(num_result_simpl, div_result_simpl)
