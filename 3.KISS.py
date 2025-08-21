# KISS -> Keep It Simple, Stupid

# The KISS Principle stands for “Keep It Simple, Stupid”.
# It emphasizes writing code that is simple, clear, and easy to understand, instead of making it unnecessarily complex.

# The principle says: Simple solutions are often the best ones.
# Overengineering leads to bugs, harder debugging, and low readability.
# Instead of writing fancy or overcomplicated code, focus on clarity and maintainability.
# In Python, this often means avoiding unnecessary conditions, loops, or features when a straightforward solution works.

# Complex version (violates the KISS Principle)
def sum_complex(numbers):
    total = 0
    for i in range(len(numbers)):
        total = total + numbers[i]
    return total

# Simple Version (follows KISS Principle)


def sum_simple(numbers):
    return sum(numbers)


nums = [10, 20, 30, 40]

print("Complex Sum:", sum_complex(nums))
print("Simple Sum:", sum_simple(nums))
