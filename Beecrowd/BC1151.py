def fibonacci(n):
    fib = [0, 1] 

    for i in range(2, n):
        fib.append(fib[-1] + fib[-2])

    return fib[:n]
n = int(input())
print(*fibonacci(n))
