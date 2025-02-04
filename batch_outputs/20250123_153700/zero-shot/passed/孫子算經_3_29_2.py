"""
今有雉、兔同籠，上有三十五頭，下有九十四足。問：雉、兔各幾何？
術曰：上置三十五頭，下置九十四足。半其足，得四十七，以少減多，再命之，上三除下三，上五除下五，下有一除上一，下有二除上二，即得。
答曰：雉 a ，兔 b 。
"""

"""
This is a classic Chinese math problem known as the "chicken and rabbit problem." Let's translate it into Python code to compute the values of the unknowns `a` (number of chickens) and `b` (number of rabbits). Chickens have 2 legs, and rabbits have 4 legs.


"""


from fractions import Fraction

# Total number of heads (chickens + rabbits)
heads = 35

# Total number of legs
legs = 94

# Using the system of equations:
# a + b = heads
# 2a + 4b = legs

# Simplify the second equation by dividing through by 2:
# a + b = heads
# a + 2b = legs / 2

# Subtract the first equation from the second:
# (a + 2b) - (a + b) = (legs / 2) - heads
# b = (legs / 2) - heads

b = Fraction(legs, 2) - heads

# Solve for a using the first equation:
# a + b = heads
# a = heads - b
a = heads - b

# Results
a, b


"""


This code will compute the values of `a` (number of chickens) and `b` (number of rabbits) using the given constraints. The solution is represented as fractions to handle any non-integer results.
"""


"""
"""
