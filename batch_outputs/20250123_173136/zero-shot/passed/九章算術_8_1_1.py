"""
今有上禾七秉，損實一斗，益之下禾二秉，而實一十斗。下禾八秉，益實一斗與上禾二秉，而實一十斗。問︰上、下禾實一秉各幾何？
術曰：如方程。損之曰益，益之曰損。損實一斗者，其實過一十斗也。益實一斗者，其實不滿一十斗也。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：上禾一秉實 a斗 ，下禾一秉實 b斗 。
"""

"""
To solve the problem, we will translate the ancient Chinese math problem into Python code and compute the values of the unknowns `a` and `b`. Here's the solution:


"""


from fractions import Fraction

# Define the equations based on the problem description:
# Let a = the amount of grain (in dou) per秉 of 上禾 (upper grain)
# Let b = the amount of grain (in dou) per秉 of 下禾 (lower grain)

# Equation 1: 7a - 1 + 2b = 10
# Equation 2: 8b + 1 + 2a = 10

# Solve the system of equations:
# From Equation 1: 7a - 1 + 2b = 10
# Simplify: 7a + 2b = 11

# From Equation 2: 8b + 1 + 2a = 10
# Simplify: 2a + 8b = 9

# Solve for a and b using substitution or elimination:
# Multiply the first equation by 4 to align coefficients of b:
# 28a + 8b = 44
# 2a + 8b = 9

# Subtract the second equation from the first:
# (28a + 8b) - (2a + 8b) = 44 - 9
# 26a = 35
a = Fraction(35, 26)

# Substitute a into the first equation to solve for b:
# 7a + 2b = 11
# 7(Fraction(35, 26)) + 2b = 11
# Fraction(245, 26) + 2b = 11
# 2b = 11 - Fraction(245, 26)
# 2b = Fraction(286, 26) - Fraction(245, 26)
# 2b = Fraction(41, 26)
b = Fraction(41, 52)

# The solution:
# a = Fraction(35, 26) dou
# b = Fraction(41, 52) dou


"""


The values of `a` and `b` are:
- `a = 35/26` dou (amount of grain per秉 of 上禾)
- `b = 41/52` dou (amount of grain per秉 of 下禾)
"""


"""
"""
