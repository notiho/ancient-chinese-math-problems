"""
今有二馬、一牛價過一萬，如半馬之價。一馬、二牛價不滿一萬，如半牛之價。問︰牛、馬價各幾何？
術曰：如方程，損益之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：馬價 a錢 ，牛價 b錢 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves two equations:

1. \( 2a + b = 10000 + \frac{a}{2} \)
2. \( a + 2b = 10000 + \frac{b}{2} \)

Where:
- \( a \) is the price of a horse in "錢".
- \( b \) is the price of a cow in "錢".

We will solve for \( a \) and \( b \) using Python.


"""

#----- content starts here -----

from fractions import Fraction

# Define the equations
# Equation 1: 2a + b = 10000 + a / 2
# Equation 2: a + 2b = 10000 + b / 2

# Solve for a and b
# Rearrange Equation 1: 2a + b - a / 2 = 10000
# Multiply through by 2 to eliminate the fraction: 4a + 2b - a = 20000
# Simplify: 3a + 2b = 20000

# Rearrange Equation 2: a + 2b - b / 2 = 10000
# Multiply through by 2 to eliminate the fraction: 2a + 4b - b = 20000
# Simplify: 2a + 3b = 20000

# Now we have a system of linear equations:
# 1. 3a + 2b = 20000
# 2. 2a + 3b = 20000

# Solve using substitution or elimination
# Multiply the first equation by 2 and the second equation by 3 to align coefficients of a:
# 1. 6a + 4b = 40000
# 2. 6a + 9b = 60000

# Subtract the first equation from the second:
# (6a + 9b) - (6a + 4b) = 60000 - 40000
# 5b = 20000
b = Fraction(20000, 5)  # b = 4000

# Substitute b = 4000 into the first equation:
# 3a + 2b = 20000
# 3a + 2(4000) = 20000
# 3a + 8000 = 20000
# 3a = 12000
a = Fraction(12000, 3)  # a = 4000

# The solutions are:
# a = 4000 (price of a horse in 錢)
# b = 4000 (price of a cow in 錢)
#----- content ends here -----


"""


Now the variables `a` and `b` hold the prices of a horse and a cow, respectively, in "錢".
"""


"""
Variable 'a' has wrong value. Expected: 60000/11, Actual: 4000
Variable 'b' has wrong value. Expected: 20000/11, Actual: 4000"""
