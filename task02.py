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