"""
今有上禾六秉，損實一斗八升，當下禾一十秉。下禾十五秉，損實五升，當上禾五秉。問︰上、下禾實一秉各幾何？
術曰：如方程，置上禾六秉正，下禾一十秉負，損實一斗八升正。次置上禾五秉負，下禾一十五秉正，損實五升正。以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：上禾 a秉 實 b升 ，下禾 c秉 實 d升 。
"""

"""
To solve this problem, we will translate the ancient Chinese mathematical problem into Python code. The problem involves solving a system of linear equations to find the values of the unknowns.

Here is the Python code:


"""


from fractions import Fraction

# Define the equations based on the problem:
# Equation 1: 6a - 10c = 1斗8升 = 18升
# Equation 2: -5a + 15c = 5升

# Convert units to "升" for consistency:
# 1斗 = 10升
eq1_constant = 18  # 1斗8升 = 18升
eq2_constant = 5   # 5升

# Coefficients of the equations:
# Equation 1: 6a - 10c = 18
# Equation 2: -5a + 15c = 5
coeff_a1, coeff_c1 = 6, -10
coeff_a2, coeff_c2 = -5, 15

# Solve for 'a' (上禾實一秉) and 'c' (下禾實一秉):
# Use the elimination method to solve the system of equations.
# Multiply the first equation by 5 and the second equation by 6 to align coefficients of 'a':
multiplier1 = 5
multiplier2 = 6

new_coeff_a1 = coeff_a1 * multiplier1
new_coeff_c1 = coeff_c1 * multiplier1
new_constant1 = eq1_constant * multiplier1

new_coeff_a2 = coeff_a2 * multiplier2
new_coeff_c2 = coeff_c2 * multiplier2
new_constant2 = eq2_constant * multiplier2

# Subtract the second equation from the first to eliminate 'a':
final_coeff_c = new_coeff_c1 - new_coeff_c2
final_constant = new_constant1 - new_constant2

# Solve for 'c':
c = Fraction(final_constant, final_coeff_c)

# Substitute 'c' back into one of the original equations to solve for 'a':
a = Fraction(eq1_constant - coeff_c1 * c, coeff_a1)

# Convert results to "斗" and "升" for the final answer:
# 'a' and 'c' are in terms of "升". Convert to "斗" and "升".
a斗 = a // 10  # Integer division for "斗"
a升 = a % 10   # Remainder for "升"

c斗 = c // 10  # Integer division for "斗"
c升 = c % 10   # Remainder for "升"

# Assign the results to variables:
b = a升  # 上禾實一秉 in 升
d = c升  # 下禾實一秉 in 升

# Final results:
a = a斗  # 上禾實一秉 in 斗
c = c斗  # 下禾實一秉 in 斗

# The results are:
# a: 上禾實一秉 in 斗
# b: 上禾實一秉 in 升
# c: 下禾實一秉 in 斗
# d: 下禾實一秉 in 升


"""


This code solves the problem step by step, using the elimination method to find the values of `a` (上禾實一秉) and `c` (下禾實一秉). The results are expressed in terms of "斗" and "升" as required.
"""


"""
Variable 'a' has wrong value. Expected: 1, Actual: 0
Variable 'b' has wrong value. Expected: 8, Actual: 16/7
Variable 'c' has wrong value. Expected: 1, Actual: -1
Variable 'd' has wrong value. Expected: 3, Actual: 67/7"""
