"""
今有上禾六秉，損實一斗八升，當下禾一十秉。下禾十五秉，損實五升，當上禾五秉。問︰上、下禾實一秉各幾何？
術曰：如方程，置上禾六秉正，下禾一十秉負，損實一斗八升正。次置上禾五秉負，下禾一十五秉正，損實五升正。以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：上禾 a秉 實 b升 ，下禾 c秉 實 d升 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves a system of linear equations, and we will solve it step by step using the given information. The solution will use the `Fraction` class to handle fractional values.

Here is the Python code:


"""


from fractions import Fraction

# Define the equations based on the problem description:
# Equation 1: 6a - 10c = 1斗8升 = 18升 (1斗 = 10升)
# Equation 2: -5a + 15c = 5升

# Convert the equations into a standard form:
# Equation 1: 6a - 10c = 18
# Equation 2: -5a + 15c = 5

# Solve for a and c (the values of 上禾 and 下禾 per 秉):
# Multiply Equation 1 by 5 and Equation 2 by 6 to eliminate 'a':
# 30a - 50c = 90  (from Equation 1)
# -30a + 90c = 30 (from Equation 2)

# Add the two equations:
# (30a - 50c) + (-30a + 90c) = 90 + 30
# 40c = 120
c = Fraction(120, 40)  # c = 3 (下禾 per 秉)

# Substitute c = 3 into Equation 1 to solve for a:
# 6a - 10(3) = 18
# 6a - 30 = 18
# 6a = 48
a = Fraction(48, 6)  # a = 8 (上禾 per 秉)

# Now calculate the actual values of b and d (the 实 per 秉 for 上禾 and 下禾):
# From the problem, we know:
# b = a * 实 per 秉 for 上禾
# d = c * 实 per 秉 for 下禾

# Since 实 per 秉 for 上禾 and 下禾 are given as 1斗 (10升) each:
b = Fraction(10, 1)  # b = 10升
d = Fraction(10, 1)  # d = 10升

# Final results:
print(f"a (上禾 per 秉) = {a}")
print(f"b (上禾 实 per 秉) = {b} 升")
print(f"c (下禾 per 秉) = {c}")
print(f"d (下禾 实 per 秉) = {d} 升")


"""


### Explanation:
1. The problem is translated into two linear equations based on the given relationships.
2. The equations are solved step by step using elimination to find the values of `a` (上禾 per 秉) and `c` (下禾 per 秉).
3. The actual 实 per 秉 values (`b` and `d`) are calculated based on the problem's description.
4. The results are printed in the required format.

### Output:
```
a (上禾 per 秉) = 8
b (上禾 实 per 秉) = 10 升
c (下禾 per 秉) = 3
d (下禾 实 per 秉) = 10 升
```
"""


"""
Variable 'a' has wrong value. Expected: 1, Actual: 8
Variable 'b' has wrong value. Expected: 8, Actual: 10
Variable 'c' has wrong value. Expected: 1, Actual: 3
Variable 'd' has wrong value. Expected: 3, Actual: 10"""
