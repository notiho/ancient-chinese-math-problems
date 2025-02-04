"""
今有甲乙二人持錢不知其數。甲得乙半而錢五十，乙得甲太半而亦錢五十。問︰甲、乙持錢各幾何？
術曰：如方程，損益之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：甲持 a錢 ，乙持 b錢 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves two unknowns, \( a \) (the amount of money held by person 甲) and \( b \) (the amount of money held by person 乙). The problem states:

1. If 甲 gets half of 乙's money, 甲 will have 50.
2. If 乙 gets more than half of 甲's money, 乙 will also have 50.

We will solve this system of equations using Python.


"""


from fractions import Fraction

# Let a = money held by 甲
# Let b = money held by 乙

# Equation 1: a + b/2 = 50
# Equation 2: b + (3/2)*a = 50

# Solve the system of equations
# From Equation 1: b/2 = 50 - a
# Multiply through by 2: b = 2 * (50 - a)

# Substitute b into Equation 2:
# 2 * (50 - a) + (3/2)*a = 50
# Expand: 100 - 2*a + (3/2)*a = 50
# Combine terms: 100 - (4/2)*a + (3/2)*a = 50
# Simplify: 100 - (1/2)*a = 50
# Rearrange: (1/2)*a = 100 - 50
# Simplify: (1/2)*a = 50
# Multiply through by 2: a = 100

# Substitute a = 100 into b = 2 * (50 - a):
# b = 2 * (50 - 100)
# b = 2 * (-50)
# b = -100

a = Fraction(100)  # Money held by 甲
b = Fraction(-100)  # Money held by 乙

# The solution is:
# a = 100
# b = -100


"""


### Explanation:
- \( a \) represents the amount of money held by 甲.
- \( b \) represents the amount of money held by 乙.
- The solution satisfies both equations:
  - \( a + b/2 = 50 \)
  - \( b + (3/2)*a = 50 \)


"""


"""
Variable 'a' has wrong value. Expected: 75/2, Actual: 100
Variable 'b' has wrong value. Expected: 25, Actual: -100"""
