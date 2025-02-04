"""
今有大器五、小器一容三斛；大器一、小器五容二斛。問︰大、小器各容幾何？
術曰：假令大器五斗，小器亦五斗，盈一十斗。令之大器五斗五升，小器二斗五升，不足二斗。
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。
荅曰：大器容 a斛 ，小器容 b斛 。
"""

"""
To solve this problem, we need to determine the capacities of the large vessel (`a`) and the small vessel (`b`) in terms of "斛" (a unit of volume). The problem provides two equations based on the given conditions:

1. Five large vessels and one small vessel together hold 3斛.
2. One large vessel and five small vessels together hold 2斛.

We can represent these equations as:
- \( 5a + b = 3 \)
- \( a + 5b = 2 \)

We solve these equations simultaneously to find \( a \) and \( b \).

Here is the Python code to compute the values of \( a \) and \( b \):


"""

#----- content starts here -----

from fractions import Fraction

# Define the equations
# 5a + b = 3
# a + 5b = 2

# Solve for a and b
# Multiply the second equation by 5 to align coefficients of a
# 5a + b = 3
# 5a + 25b = 10

# Subtract the first equation from the modified second equation
# (5a + 25b) - (5a + b) = 10 - 3
# 24b = 7
b = Fraction(7, 24)

# Substitute b back into the first equation to solve for a
# 5a + b = 3
# 5a + (7/24) = 3
# 5a = 3 - (7/24)
# 5a = (72/24) - (7/24)
# 5a = 65/24
a = Fraction(65, 24)

# Results
a, b
#----- content ends here -----


"""


### Solution:
- Large vessel capacity (\( a \)): \( \frac{65}{24} \)斛
- Small vessel capacity (\( b \)): \( \frac{7}{24} \)斛
"""


"""
Variable 'a' has wrong value. Expected: 13/24, Actual: 65/24"""
