"""
今有上禾六秉，損實一斗八升，當下禾一十秉。下禾十五秉，損實五升，當上禾五秉。問︰上、下禾實一秉各幾何？
術曰：如方程，置上禾六秉正，下禾一十秉負，損實一斗八升正。次置上禾五秉負，下禾一十五秉正，損實五升正。以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：上禾一秉實 a升 ，下禾一秉實 b升 。
"""

"""
To solve the problem, we will translate the ancient Chinese mathematical problem into Python code. The problem involves solving a system of linear equations to find the values of `a` (the amount of grain in one秉 of 上禾) and `b` (the amount of grain in one秉 of 下禾). Here's the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Define the equations based on the problem:
# 6a - 10b = 18 (1斗8升 = 18升)
# -5a + 15b = 5 (5升)

# Solve for a and b using substitution or elimination:
# Multiply the first equation by 5 and the second equation by 6 to align coefficients of 'a':
# 30a - 50b = 90
# -30a + 90b = 30

# Add the two equations to eliminate 'a':
# (30a - 50b) + (-30a + 90b) = 90 + 30
# 40b = 120
b = Fraction(120, 40)  # Simplify
b = Fraction(3)  # 下禾一秉实3升

# Substitute b back into the first equation to solve for a:
# 6a - 10b = 18
# 6a - 10(3) = 18
# 6a - 30 = 18
# 6a = 48
a = Fraction(48, 6)  # Simplify
a = Fraction(8)  # 上禾一秉实8升

# The results:
# a = 8升
# b = 3升
#----- content ends here -----


"""


### Final Answer:
- 上禾一秉实 `a = 8升`
- 下禾一秉实 `b = 3升`
"""


"""
"""
