def fibonacci_sequence(n):
    fib_sequence = [0, 1]

    while True:
        next_fib = fib_sequence[-1] + fib_sequence[-2]
        if next_fib > n:
            break
        fib_sequence.append(next_fib)

    return fib_sequence


def belongs_to_fibonacci(n):
    fib_sequence = fibonacci_sequence(n)
    return n in fib_sequence


num = int(input("Digite um número: "))

if belongs_to_fibonacci(num):
    print(f"O número {num} pertence à sequência de Fibonacci.")

else:
    print(f"O número {num} não pertence à sequência de Fibonacci.")
