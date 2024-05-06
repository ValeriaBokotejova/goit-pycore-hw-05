# Implement the caching_fibonacci function, which creates and utilizes a cache to store and reuse
# already computed Fibonacci numbers.

# The Fibonacci series is a sequence of numbers like: 0, 1, 1, 2, 3, 5, 8, ..., where each 
# subsequent number in the sequence is obtained by adding the two previous members of the series.
# In general, to compute the n-th member of the Fibonacci series, the expression needs to be 
# calculated: Fn = Fn-1 + Fn-2
# This task can be solved recursively by calling a function that computes the numbers of the 
# sequence until the call reaches members of the series less than n = 1, where the sequence is defined.

# Task requirements:
# 1. The caching_fibonacci() function should return an inner function fibonacci(n).
# 2. fibonacci(n) computes the n-th Fibonacci number. If the number is already in the cache, 
# the function should return the value from the cache.
# 3. If the number is not in the cache, the function should compute it, store it in the cache, 
# and return the result.
# 4. Use recursion to compute Fibonacci numbers.

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
