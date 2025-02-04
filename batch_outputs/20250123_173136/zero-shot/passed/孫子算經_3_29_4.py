"""
今有雉、兔同籠，上有三十五頭，下有九十四足。問：雉、兔各幾何？
術曰：上置三十五頭，下置九十四足。半其足，得四十七，以少減多，再命之，上三除下三，上五除下五，下有一除上一，下有二除上二，即得。
答曰：雉 a ，兔 b 。
"""

"""
To solve this problem, we need to determine the number of pheasants ("雉") and rabbits ("兔") in a cage, given that there are 35 heads and 94 feet in total. Pheasants have 2 feet each, and rabbits have 4 feet each.

Here is the Python code to compute the solution:


"""


from fractions import Fraction

# Total number of heads and feet
heads = 35
feet = 94

# Let a = number of pheasants (雉)
# Let b = number of rabbits (兔)

# Using the system of equations:
# a + b = heads
# 2a + 4b = feet

# Solve for b in terms of a using the first equation:
# b = heads - a

# Substitute b into the second equation:
# 2a + 4(heads - a) = feet
# 2a + 4heads - 4a = feet
# -2a + 4heads = feet
# 2a = 4heads - feet
# a = (4heads - feet) / 2

a = Fraction(4 * heads - feet, 2)

# Solve for b using b = heads - a
b = heads - a

# Results
a, b


"""


The variables `a` and `b` will hold the number of pheasants and rabbits, respectively.
"""


"""
"""
