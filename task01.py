def caching_fibonacci():
    cache = {}

    def fibonacci(n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        elif n in cache:
            return cache[n]
        else:
            cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
            return cache[n]

    return fibonacci


# Getting the Fibonacci function
fib = caching_fibonacci()
# Using the Fibonacci function to calculate Fibonacci numbers
print(fib(10))  # Display 55
print(fib(15))  # Display 610
