"""
今有上禾二秉，中禾三秉，下禾四秉，實皆不滿斗。上取中，中取下，下取上各一秉而實滿斗。問︰上、中、下禾實一秉各幾何？
術曰：如方程，各置所取，以正負術入之。正負術曰：同名相除，異名相益，正無入負之，負無入正之。其異名相除，同名相益，正無入正之，負無入負之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：上禾一秉實 a斗 ，中禾一秉實 b斗 ，下禾一秉實 c斗 。
"""

"""
To solve this problem, we will translate the ancient Chinese mathematical procedure into Python code step by step. The procedure involves solving a system of linear equations using elimination methods similar to Gaussian elimination. Here's the Python implementation:


"""


from fractions import Fraction

# Given data
# Upward, middle, and downward grains
上禾秉數 = 2
中禾秉數 = 3
下禾秉數 = 4

# Total grains after redistribution
總實 = 39

# Step 1: Set up the equations based on the problem description
# Let a, b, c represent the actual grain per秉 for 上禾, 中禾, 下禾 respectively.
# The equations are:
# 2a + b = 39  (上禾 equation)
# b + 3c = 39  (中禾 equation)
# c + 4a = 39  (下禾 equation)

# Step 2: Solve the system of equations using elimination
# From the first equation: b = 39 - 2a
# Substitute b into the second equation: (39 - 2a) + 3c = 39
# Simplify: -2a + 3c = 0
# From the third equation: c + 4a = 39
# Solve for c: c = 39 - 4a

# Substitute c into -2a + 3c = 0:
# -2a + 3(39 - 4a) = 0
# -2a + 117 - 12a = 0
# -14a + 117 = 0
# a = 117 / 14

a = Fraction(117, 14)

# Solve for c using c = 39 - 4a
c = 39 - 4 * a

# Solve for b using b = 39 - 2a
b = 39 - 2 * a

# Results
print(f"上禾一秉實 a斗 = {a}")
print(f"中禾一秉實 b斗 = {b}")
print(f"下禾一秉實 c斗 = {c}")


"""


### Explanation of the Code:
1. **Setting up the equations**: The problem is translated into three linear equations based on the description of the redistribution of grains.
2. **Elimination method**: The equations are solved step by step by substituting variables and simplifying.
3. **Using `Fraction`**: This ensures that all calculations are exact and fractions are preserved, as required by the problem.

### Output:
The solution will provide the exact values of `a`, `b`, and `c` (the grain per秉 for 上禾, 中禾, and 下禾 respectively) in terms of斗.
"""


"""
Variable 'a' has wrong value. Expected: 9/25, Actual: 117/14
Variable 'b' has wrong value. Expected: 7/25, Actual: 156/7
Variable 'c' has wrong value. Expected: 4/25, Actual: 39/7"""
