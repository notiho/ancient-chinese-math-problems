"""
今有甲乙二人持錢不知其數。甲得乙半而錢五十，乙得甲太半而亦錢五十。問︰甲、乙持錢各幾何？
術曰：如方程，損益之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：甲持 a錢 ，乙持 b錢 。
"""

"""
To solve the problem, we will translate the ancient Chinese math problem into Python code. The problem describes a system of equations based on the relationships between the amounts of money held by two people, "甲" (a) and "乙" (b). Here's the solution:


"""


from fractions import Fraction

# Let a = money held by 甲
# Let b = money held by 乙

# Equation 1: 甲得乙半而錢五十
# a + b/2 = 50

# Equation 2: 乙得甲太半而亦錢五十
# b + (3/2)a = 50

# Solve the system of equations
# From Equation 1: a = 50 - b/2
# Substitute into Equation 2: b + (3/2)(50 - b/2) = 50

# Simplify Equation 2:
# b + 75 - (3/4)b = 50
# (1 - 3/4)b = 50 - 75
# (1/4)b = -25
# b = -25 * 4
b = Fraction(-25 * 4)

# Substitute b into Equation 1 to find a:
a = Fraction(50) - Fraction(b, 2)

# The solutions are:
# a = money held by 甲
# b = money held by 乙


"""


Now, the values of `a` and `b` are computed as fractions.
"""


"""
Variable 'a' has wrong value. Expected: 75/2, Actual: 100
Variable 'b' has wrong value. Expected: 25, Actual: -100"""
