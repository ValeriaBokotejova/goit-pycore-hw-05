# It is necessary to create the function generator_numbers, which will analyze the text, identify all
# real numbers considered as parts of income, and return them as a generator. Real numbers in the text
# are written without errors and are clearly separated by spaces on both sides. It is also necessary 
# to implement the sum_profit function, which will use generator_numbers to sum up these numbers and 
# calculate the total profit.

# Task requirements:
# 1. The generator_numbers function should take a string as an argument and return a generator that
# iterates over all real numbers in the text. Real numbers in the text are considered to be written
# without errors and are clearly separated by spaces on both sides.
# 2. The sum_profit function should use the generator_numbers generator to compute the total sum of
# numbers in the input string and take it as an argument during invocation.

import re
from typing import Callable

def generator_numbers(text: str):

    pattern = r'\b\d+\.\d+\b'  # Regular expression for finding real numbers
    for match in re.finditer(pattern, text):
        yield float(match.group())  # Returned number in the form of a real number


def sum_profit(text: str, func: Callable):
    total_profit = sum(func(text))
    return total_profit

# Usage example:
text = "An employee's total income consists of several parts: $1000.01 as the base income, supplemented by additional earnings of $27.45 and $324.00."
total_income = sum_profit(text, generator_numbers)
print(f"Total income: {total_income}")  # Display "Total income: 1351.46"