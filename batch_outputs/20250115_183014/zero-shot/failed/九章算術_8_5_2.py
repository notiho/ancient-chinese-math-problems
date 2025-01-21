"""
今有上禾三秉，益實六斗，當下禾十秉。下禾五秉，益實一斗，當上禾二秉。問︰上、下禾實一秉各幾何？
術曰：如方程，置上禾三秉正，下禾一十秉負，益實六斗負。次置上禾二秉負，下禾五秉正，益實一斗負。以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：上禾 a秉 實 b斗 ，下禾 c秉 實 d斗 。
"""

"""
To solve this problem, we will translate the ancient Chinese mathematical problem into Python code. The problem involves solving a system of linear equations to find the values of the unknowns. Here's the Python implementation:


"""


from fractions import Fraction

# Define the equations based on the problem:
# Equation 1: 3a - 10c = -6
# Equation 2: -2a + 5c = -1

# Solve for 'a' (the amount of grain per秉 for 上禾) and 'c' (the amount of grain per秉 for 下禾):
# Multiply Equation 1 by 5 and Equation 2 by 10 to eliminate 'c':
# 15a - 50c = -30
# -20a + 50c = -10

# Add the two equations:
# (15a - 20a) + (-50c + 50c) = -30 + -10
# -5a = -40
a = Fraction(-40, -5)  # Simplify
a = Fraction(8)  # 上禾實 per秉 (斗)

# Substitute 'a' into Equation 1 to solve for 'c':
# 3a - 10c = -6
# 3(8) - 10c = -6
# 24 - 10c = -6
# -10c = -6 - 24
# -10c = -30
c = Fraction(-30, -10)  # Simplify
c = Fraction(3)  # 下禾實 per秉 (斗)

# Output the results:
b = a  # 上禾實 per秉 (斗)
d = c  # 下禾實 per秉 (斗)

# The results:
# 上禾 a秉 實 b斗
# 下禾 c秉 實 d斗


"""


After running this code, the values of the unknowns are:
- `a = 8` (上禾實 per秉 in 斗)
- `b = 8` (上禾實 per秉 in 斗)
- `c = 3` (下禾實 per秉 in 斗)
- `d = 3` (下禾實 per秉 in 斗)
"""


"""
Variable 'a' has wrong value. Expected: 1, Actual: 8
Variable 'c' has wrong value. Expected: 1, Actual: 3"""
