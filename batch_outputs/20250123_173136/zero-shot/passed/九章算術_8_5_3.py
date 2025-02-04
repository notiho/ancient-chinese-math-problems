"""
今有上禾三秉，益實六斗，當下禾十秉。下禾五秉，益實一斗，當上禾二秉。問︰上、下禾實一秉各幾何？
術曰：如方程，置上禾三秉正，下禾一十秉負，益實六斗負。次置上禾二秉負，下禾五秉正，益實一斗負。以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：上禾一秉實 a斗 ，下禾一秉實 b斗 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves solving a system of linear equations to find the values of `a` (the amount of grain per unit for "上禾") and `b` (the amount of grain per unit for "下禾"). Here's the Python code:


"""


from fractions import Fraction

# Define the equations based on the problem:
# 3a - 10b = -6
# -2a + 5b = -1

# Solve the system of equations using substitution or elimination.
# Multiply the first equation by 2 and the second equation by 3 to align coefficients of `a`:
# 6a - 20b = -12
# -6a + 15b = -3

# Add the two equations to eliminate `a`:
# (-20b + 15b) = (-12 - 3)
# -5b = -15
b = Fraction(-15, -5)  # Solve for b
b = Fraction(3)  # Simplify

# Substitute b = 3 into the first equation to solve for a:
# 3a - 10b = -6
# 3a - 10(3) = -6
# 3a - 30 = -6
# 3a = 24
a = Fraction(24, 3)  # Solve for a
a = Fraction(8)  # Simplify

# The results:
# a = 8斗 (amount of grain per unit for "上禾")
# b = 3斗 (amount of grain per unit for "下禾")


"""


The values of the unknowns are:
- `a = 8` (斗)
- `b = 3` (斗)
"""


"""
"""
