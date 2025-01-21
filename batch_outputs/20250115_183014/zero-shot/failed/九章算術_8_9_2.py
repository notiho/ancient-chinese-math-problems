"""
今有甲乙二人持錢不知其數。甲得乙半而錢五十，乙得甲太半而亦錢五十。問︰甲、乙持錢各幾何？
術曰：如方程，損益之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：甲持 a錢 ，乙持 b錢 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves two unknowns, `a` (the amount of money held by person A) and `b` (the amount of money held by person B). The conditions are:

1. If person A gets half of person B's money, they will have 50 units of money.
2. If person B gets more than half of person A's money, they will also have 50 units of money.

We will solve this system of equations using Python.


"""


from fractions import Fraction

# Let a = money held by person A
# Let b = money held by person B

# Equation 1: a + b/2 = 50
# Equation 2: b + (3/2)*a = 50

# Solve the system of equations
# From Equation 1: b = 2 * (50 - a)
b = 2 * (50 - Fraction('a'))

# Substitute b into Equation 2:
# 2 * (50 - a) + (3/2) * a = 50
# Simplify:
# 100 - 2a + (3/2)a = 50
# Combine terms:
# 100 - 50 = 2a - (3/2)a
# 50 = (1/2)a
a = Fraction(50) * 2

# Substitute a back into Equation 1 to find b:
b = 2 * (50 - a)

# Final results
a = Fraction(a)  # Money held by person A
b = Fraction(b)  # Money held by person B

# Output the results
a, b


"""


This code calculates the values of `a` and `b` using the given conditions. The results will be stored in the variables `a` and `b`.
"""


"""
Code error: Invalid literal for Fraction: 'a'"""
