"""
今有上禾二秉，中禾三秉，下禾四秉，實皆不滿斗。上取中，中取下，下取上各一秉而實滿斗。問︰上、中、下禾實一秉各幾何？
術曰：如方程，各置所取，以正負術入之。正負術曰：同名相除，異名相益，正無入負之，負無入正之。其異名相除，同名相益，正無入正之，負無入負之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：上禾 a秉 實 b斗 ，中禾 c秉 實 d斗 ，下禾 e秉 實 f斗 。
"""

"""
This problem involves solving a system of linear equations using ancient Chinese mathematical methods, which resemble Gaussian elimination. Let's translate the procedure into Python code step by step.


"""


from fractions import Fraction

# Given data
上禾秉數 = 2
中禾秉數 = 3
下禾秉數 = 4
總實 = 39  # Total斗

# Step 1: Set up the equations
# Let 上禾實 = a, 中禾實 = b, 下禾實 = c
# The equations are:
# 2a + b = 39 (from 上禾)
# a + 3b + c = 39 (from 中禾)
# b + 4c = 39 (from 下禾)

# Step 2: Solve the system of equations using elimination
# Rewrite the equations:
# Equation 1: 2a + b = 39
# Equation 2: a + 3b + c = 39
# Equation 3: b + 4c = 39

# Eliminate `a` from Equation 2 using Equation 1
# Multiply Equation 1 by 1/2: a = (39 - b) / 2
# Substitute into Equation 2:
# (39 - b) / 2 + 3b + c = 39
# Multiply through by 2 to clear the fraction:
# 39 - b + 6b + 2c = 78
# Simplify:
# 5b + 2c = 39  (New Equation 4)

# Eliminate `b` from Equation 4 using Equation 3
# Solve Equation 3 for b: b = 39 - 4c
# Substitute into Equation 4:
# 5(39 - 4c) + 2c = 39
# Expand:
# 195 - 20c + 2c = 39
# Simplify:
# -18c = -156
# Solve for c:
下禾實 = Fraction(-156, -18)

# Substitute c back into Equation 3 to find b
中禾實 = Fraction(39 - 4 * 下禾實)

# Substitute b and c back into Equation 1 to find a
上禾實 = Fraction(39 - 中禾實)

# Results
a = 上禾秉數
b = 上禾實
c = 中禾秉數
d = 中禾實
e = 下禾秉數
f = 下禾實

# Output
print(f"上禾 {a}秉 實 {b}斗")
print(f"中禾 {c}秉 實 {d}斗")
print(f"下禾 {e}秉 實 {f}斗")


"""


### Explanation:
1. The equations are derived from the problem statement.
2. The elimination process follows the ancient Chinese method described in the procedure.
3. Fractions are used to ensure precise calculations.
4. The final results are printed in the required format.

This code solves the problem step by step and adheres to the ancient procedure.
"""


"""
Variable 'a' has wrong value. Expected: 1, Actual: 2
Variable 'b' has wrong value. Expected: 9/25, Actual: 104/3
Variable 'c' has wrong value. Expected: 1, Actual: 3
Variable 'd' has wrong value. Expected: 7/25, Actual: 13/3
Variable 'e' has wrong value. Expected: 1, Actual: 4
Variable 'f' has wrong value. Expected: 4/25, Actual: 26/3"""
