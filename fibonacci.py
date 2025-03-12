def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b

    return a

def fibonacciRecursive(n):
    if n <= 1:
        return 1
    
    return fibonacciRecursive(n-1) + fibonacciRecursive(n - 2)

for n in range(50):
    print(fibonacciRecursive(n), end=" | ")