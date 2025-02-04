"""
今有甲乙二人持錢不知其數。甲得乙半而錢五十，乙得甲太半而亦錢五十。問︰甲、乙持錢各幾何？
術曰：如方程，損益之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：甲持 a錢 ，乙持 b錢 。
"""

"""
To solve the problem, we translate the ancient Chinese math problem into Python code. The problem involves two unknowns, \( a \) (the amount of money held by person 甲) and \( b \) (the amount of money held by person 乙). The conditions are:

1. If 甲 takes half of 乙's money, 甲 will have 50 units of money.
2. If 乙 takes more than half of 甲's money, 乙 will also have 50 units of money.

We will solve this system of equations using Python.


"""

#----- content starts here -----

from fractions import Fraction

# Let a be the amount of money held by 甲
# Let b be the amount of money held by 乙

# Equation 1: a + b/2 = 50
# Equation 2: b + (3/2)a = 50

# Solve for a and b
# From Equation 1: b = 2 * (50 - a)
# Substitute b into Equation 2: 2 * (50 - a) + (3/2)a = 50

# Simplify Equation 2:
# 100 - 2a + (3/2)a = 50
# Combine terms: -2a + (3/2)a = -50
# (-4/2)a + (3/2)a = -50
# (-4 + 3)/2 * a = -50
# (-1/2)a = -50
# a = 100

# Substitute a = 100 into Equation 1 to find b:
# b = 2 * (50 - 100)
# b = 2 * (-50)
# b = -100

a = Fraction(100)  # Amount of money held by 甲
b = Fraction(-100)  # Amount of money held by 乙

# The solution is:
# a = 100
# b = -100
#----- content ends here -----


"""


The solution is:
- \( a = 100 \) (甲持 100 錢)
- \( b = -100 \) (乙持 -100 錢)
"""


"""
Variable 'a' has wrong value. Expected: 75/2, Actual: 100
Variable 'b' has wrong value. Expected: 25, Actual: -100"""
