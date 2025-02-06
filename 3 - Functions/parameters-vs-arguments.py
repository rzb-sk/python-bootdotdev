"""
    1. Parameters are the names used for inputs when "defining" a function.
    2. Arguments are the values of the inputs supplied when a function is "called".
    "Arguments" are the actual values that go into the function.
    "Parameters" are the names we use in the function definition o refer to those values.
"""

# a & b are parameters
def add(a, b):
    return a + b

# 5 & 6 are arguments
sum = add(5, 6)
print(sum)