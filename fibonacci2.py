def fibonacci(n):
    if n == 0 or n == 1:
        return n
    
    if memory[n] is not None:
        return memory[n]
    
    memory[n] = fibonacci(n - 1) + fibonacci(n - 2)

    return memory[n]
    
memory: list = [None] * 1000
    
for n in range(100000):
    print(fibonacci(n), end=" | ")