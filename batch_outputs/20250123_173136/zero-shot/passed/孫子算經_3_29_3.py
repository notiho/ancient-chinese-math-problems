"""
今有雉、兔同籠，上有三十五頭，下有九十四足。問：雉、兔各幾何？
術曰：上置三十五頭，下置九十四足。半其足，得四十七，以少減多，再命之，上三除下三，上五除下五，下有一除上一，下有二除上二，即得。
答曰：雉 a ，兔 b 。
"""

"""
This is a classic ancient Chinese math problem known as the "chicken and rabbit problem." Let's translate it into Python code to compute the values of the unknowns `a` (number of chickens) and `b` (number of rabbits). Chickens have 2 legs, and rabbits have 4 legs. The total number of heads is 35, and the total number of legs is 94.


"""


from fractions import Fraction

# Total heads
heads = 35

# Total legs
legs = 94

# Solve for the number of chickens (a) and rabbits (b)
# Let a = number of chickens, b = number of rabbits
# We know:
# a + b = heads
# 2a + 4b = legs

# Simplify the second equation by dividing through by 2:
# a + 2b = legs / 2

# Subtract the first equation from the simplified second equation:
# (a + 2b) - (a + b) = (legs / 2) - heads
# b = (legs / 2) - heads

b = Fraction(legs, 2) - heads

# Substitute b back into the first equation to solve for a:
# a + b = heads
a = heads - b

# The solution
a, b


"""


This code will compute the number of chickens (`a`) and rabbits (`b`) using the given constraints. The result will be stored in the variables `a` and `b`.
"""


"""
"""
