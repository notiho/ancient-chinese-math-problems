"""
今有上禾二秉，中禾三秉，下禾四秉，實皆不滿斗。上取中，中取下，下取上各一秉而實滿斗。問︰上、中、下禾實一秉各幾何？
術曰：如方程，各置所取，以正負術入之。正負術曰：同名相除，異名相益，正無入負之，負無入正之。其異名相除，同名相益，正無入正之，負無入負之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：上禾 a秉 實 b斗 ，中禾 c秉 實 d斗 ，下禾 e秉 實 f斗 。
"""

"""
This problem involves solving a system of equations using ancient Chinese mathematical techniques, specifically the "正負術" (positive-negative method) and "方程術" (method of equations). Below is the Python implementation of the procedure:


"""


from fractions import Fraction

# 上禾二秉，中禾三秉，下禾四秉
上禾秉數 = 2
中禾秉數 = 3
下禾秉數 = 4

# 實皆不滿斗
# 上取中，中取下，下取上各一秉而實滿斗
# This gives us the system of equations:
# 上禾 + 中禾 = 1
# 中禾 + 下禾 = 1
# 下禾 + 上禾 = 1

# 方程術解法 (Solving the system of equations)

# Step 1: Represent the equations in matrix form
# Let 上禾 = x, 中禾 = y, 下禾 = z
# The equations become:
# x + y = 1
# y + z = 1
# z + x = 1

# Step 2: Solve for x, y, z using substitution and elimination
# From the first equation: x = 1 - y
# Substitute x into the third equation: z + (1 - y) = 1 -> z = y
# Substitute z into the second equation: y + y = 1 -> y = 1/2
中禾實 = Fraction(1, 2)

# Solve for z using z = y
下禾實 = 中禾實

# Solve for x using x = 1 - y
上禾實 = 1 - 中禾實

# Step 3: Calculate the total斗 for each禾
# 上禾實, 中禾實, 下禾實 are the values for one秉
# Multiply by the respective秉數 to get the total斗
上禾斗 = 上禾實 * 上禾秉數
中禾斗 = 中禾實 * 中禾秉數
下禾斗 = 下禾實 * 下禾秉數

# Final results
a = 上禾秉數
b = 上禾斗
c = 中禾秉數
d = 中禾斗
e = 下禾秉數
f = 下禾斗

# Output the results
print(f"上禾 {a}秉 實 {b}斗")
print(f"中禾 {c}秉 實 {d}斗")
print(f"下禾 {e}秉 實 {f}斗")


"""


### Explanation of the Solution:
1. The problem is modeled as a system of three linear equations based on the relationships between the different types of禾 (grains).
2. Using substitution and elimination, the values for one秉 (bundle) of each type of禾 are calculated.
3. The total斗 (volume) for each type of禾 is then calculated by multiplying the value for one秉 by the number of秉 for that禾.
4. The results are presented as the total秉 and斗 for each type of禾.

### Final Answer:
- 上禾: `a = 2秉`, `b = 1斗`
- 中禾: `c = 3秉`, `d = 1.5斗`
- 下禾: `e = 4秉`, `f = 2斗`
"""


"""
Variable 'a' has wrong value. Expected: 1, Actual: 2
Variable 'b' has wrong value. Expected: 9/25, Actual: 1
Variable 'c' has wrong value. Expected: 1, Actual: 3
Variable 'd' has wrong value. Expected: 7/25, Actual: 3/2
Variable 'e' has wrong value. Expected: 1, Actual: 4
Variable 'f' has wrong value. Expected: 4/25, Actual: 2"""
