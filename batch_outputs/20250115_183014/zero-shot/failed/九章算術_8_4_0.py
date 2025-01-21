"""
今有上禾六秉，損實一斗八升，當下禾一十秉。下禾十五秉，損實五升，當上禾五秉。問︰上、下禾實一秉各幾何？
術曰：如方程，置上禾六秉正，下禾一十秉負，損實一斗八升正。次置上禾五秉負，下禾一十五秉正，損實五升正。以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：上禾 a秉 實 b升 ，下禾 c秉 實 d升 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves solving a system of linear equations to find the values of the unknowns. Here's the Python code:


"""


from fractions import Fraction

# Define the equations based on the problem:
# Equation 1: 6a - 10c = 1斗8升 = 18升
# Equation 2: -5a + 15c = 5升

# Convert units to consistent terms (升):
# 1斗 = 10升
eq1_constant = 18  # 1斗8升 = 18升
eq2_constant = 5   # 5升

# Solve the system of equations:
# Multiply equation 1 by 5 and equation 2 by 6 to eliminate 'a':
# 30a - 50c = 90
# -30a + 90c = 30

# Add the two equations:
# 40c = 120
c = Fraction(120, 40)  # c = 3

# Substitute c = 3 into equation 1 to solve for a:
# 6a - 10(3) = 18
# 6a - 30 = 18
# 6a = 48
a = Fraction(48, 6)  # a = 8

# Now calculate the actual values for the "實" (amount per 秉):
# For 上禾 (a 秉), 实 = b 升
# For 下禾 (c 秉), 实 = d 升

# From the problem, we know:
# Total 实 for 上禾 = 6a = 6 * 8 = 48升
# Total 实 for 下禾 = 10c = 10 * 3 = 30升

# 实 per 秉 for 上禾:
b = Fraction(48, 6)  # b = 8升

# 实 per 秉 for 下禾:
d = Fraction(30, 10)  # d = 3升

# Final results:
a = 8  # 上禾 秉数
b = 8  # 上禾 实 per 秉 (升)
c = 3  # 下禾 秉数
d = 3  # 下禾 实 per 秉 (升)


"""


### Explanation:
1. The problem is translated into two linear equations based on the given relationships.
2. The units are converted to a consistent unit (升).
3. The system of equations is solved using substitution and elimination.
4. The results are stored in variables `a`, `b`, `c`, and `d` as required.

### Results:
- `a = 8` (上禾 秉数)
- `b = 8` (上禾 实 per 秉 in 升)
- `c = 3` (下禾 秉数)
- `d = 3` (下禾 实 per 秉 in 升)
"""


"""
Variable 'a' has wrong value. Expected: 1, Actual: 8
Variable 'c' has wrong value. Expected: 1, Actual: 3"""
