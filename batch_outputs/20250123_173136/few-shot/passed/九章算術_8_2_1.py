"""
今有上禾二秉，中禾三秉，下禾四秉，實皆不滿斗。上取中，中取下，下取上各一秉而實滿斗。問︰上、中、下禾實一秉各幾何？
術曰：如方程，各置所取，以正負術入之。正負術曰：同名相除，異名相益，正無入負之，負無入正之。其異名相除，同名相益，正無入正之，負無入負之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：上禾一秉實 a斗 ，中禾一秉實 b斗 ，下禾一秉實 c斗 。
"""

"""
This problem involves solving a system of equations using ancient Chinese mathematical techniques, specifically the "正負術" (positive-negative method) and "方程術" (method of equations). Below is the Python implementation of the procedure:


"""


from fractions import Fraction

# 上禾二秉，中禾三秉，下禾四秉
上禾秉數 = 2
中禾秉數 = 3
下禾秉數 = 4

# 上取中，中取下，下取上各一秉而實滿斗
# Translate this into equations:
# Let 上禾一秉 = a, 中禾一秉 = b, 下禾一秉 = c
# The equations are:
# 2a + b = 1 (上禾取中禾一秉)
# 3b + c = 1 (中禾取下禾一秉)
# 4c + a = 1 (下禾取上禾一秉)

# Using the 方程術 to solve the system of equations:

# Step 1: Express the equations in matrix form:
# | 2  1  0 |   | a |   | 1 |
# | 0  3  1 | * | b | = | 1 |
# | 1  0  4 |   | c |   | 1 |

# Step 2: Solve using substitution and elimination:
# From the first equation: b = 1 - 2a
# Substitute b into the second equation: 3(1 - 2a) + c = 1
# Simplify: 3 - 6a + c = 1
# c = -2 + 6a
# Substitute c into the third equation: 4(-2 + 6a) + a = 1
# Simplify: -8 + 24a + a = 1
# 25a = 9
# a = 9 / 25

a = Fraction(9, 25)

# Step 3: Solve for b using b = 1 - 2a
b = 1 - 2 * a

# Step 4: Solve for c using c = -2 + 6a
c = -2 + 6 * a

# The results are:
# 上禾一秉實 a斗
# 中禾一秉實 b斗
# 下禾一秉實 c斗

print(f"上禾一秉實 {a}斗")
print(f"中禾一秉實 {b}斗")
print(f"下禾一秉實 {c}斗")


"""


### Explanation of the Results:
- The solution uses substitution and elimination to solve the system of equations derived from the problem.
- The results for `a`, `b`, and `c` represent the amount of grain in one秉 (bundle) for 上禾 (upper grain), 中禾 (middle grain), and 下禾 (lower grain), respectively.

### Final Answer:
- 上禾一秉實 `a` 斗
- 中禾一秉實 `b` 斗
- 下禾一秉實 `c` 斗
"""


"""
"""
