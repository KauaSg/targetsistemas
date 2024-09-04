def fibonacci(n):
    a, b = 0, 1
    
    while a <= n:
        if a == n:
            return f"O número {n} pertence à sequência de Fibonacci."
        a, b = b, a + b 
    
    return f"O número {n} não pertence à sequência de Fibonacci."


numero = int(input("insira um numero")) 
fibonacci(numero)