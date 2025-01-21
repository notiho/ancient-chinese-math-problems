"""
今有上禾三秉，益實六斗，當下禾十秉。下禾五秉，益實一斗，當上禾二秉。問︰上、下禾實一秉各幾何？
術曰：如方程，置上禾三秉正，下禾一十秉負，益實六斗負。次置上禾二秉負，下禾五秉正，益實一斗負。以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：上禾 a秉 實 b斗 ，下禾 c秉 實 d斗 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves solving a system of linear equations to determine the values of the unknowns. Let's compute the solution step by step.

### Problem setup:
1. Let the amount of grain per秉 (unit) for the "上禾" (upper grain) be `a`斗 (dou).
2. Let the amount of grain per秉 (unit) for the "下禾" (lower grain) be `b`斗 (dou).

From the problem, we have the following equations:
- \( 3a - 10b = -6 \)
- \( -2a + 5b = -1 \)

We will solve these equations using Python.

### Python Code:

"""


from fractions import Fraction

# Define the equations:
# 3a - 10b = -6
# -2a + 5b = -1

# Solve for a and b using substitution or elimination:
# Multiply the first equation by 2 and the second equation by 3 to align coefficients of 'a':
# 6a - 20b = -12
# -6a + 15b = -3

# Add the two equations to eliminate 'a':
# (-20b + 15b) = -12 - 3
b = Fraction(-15, -5)  # Simplify the result
b = Fraction(3)  # b = 3斗

# Substitute b = 3 into the first equation to solve for a:
# 3a - 10(3) = -6
# 3a - 30 = -6
# 3a = 24
a = Fraction(24, 3)  # Simplify the result
a = Fraction(8)  # a = 8斗

# Output the results:
a  # 上禾实一秉 (upper grain per unit)
b  # 下禾实一秉 (lower grain per unit)


"""


### Solution:
- \( a = 8 \)斗 (upper grain per unit)
- \( b = 3 \)斗 (lower grain per unit)

The Python code computes these values directly using the `Fraction` class to ensure exact arithmetic.
"""


"""
Variable 'a' has wrong value. Expected: 1, Actual: 8
Variable 'b' has wrong value. Expected: 8, Actual: 3
Missing variable in output: 'c'
Missing variable in output: 'd'"""
