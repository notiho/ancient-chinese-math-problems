"""
今有上禾二秉，中禾三秉，下禾四秉，實皆不滿斗。上取中，中取下，下取上各一秉而實滿斗。問︰上、中、下禾實一秉各幾何？
術曰：如方程，各置所取，以正負術入之。正負術曰：同名相除，異名相益，正無入負之，負無入正之。其異名相除，同名相益，正無入正之，負無入負之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：上禾 a(=1)秉 實 b(=9/25)斗 ，中禾 c(=1)秉 實 d(=7/25)斗 ，下禾 e(=1)秉 實 f(=4/25)斗 。
"""

"""
This problem involves solving a system of equations using ancient Chinese methods, specifically the "正負術" (positive and negative method) and "方程術" (method of equations). Below is the Python implementation of the solution:


"""


from fractions import Fraction

# 上禾、 中禾、 下禾秉數
上禾秉數 = 2
中禾秉數 = 3
下禾秉數 = 4

# 每秉實滿斗的條件
# 上禾取中禾1秉，中禾取下禾1秉，下禾取上禾1秉，實滿1斗
# 方程式如下：
# 2a + b = 1
# 3b + c = 1
# 4c + a = 1

# Step 1: Solve for a, b, c using substitution/elimination
# From the first equation: b = 1 - 2a
# Substitute b into the second equation: 3(1 - 2a) + c = 1
# Simplify: 3 - 6a + c = 1 -> c = 6a - 2
# Substitute c into the third equation: 4(6a - 2) + a = 1
# Simplify: 24a - 8 + a = 1 -> 25a = 9 -> a = 9/25
a = Fraction(9, 25)

# Step 2: Solve for b
# b = 1 - 2a
b = 1 - 2 * a

# Step 3: Solve for c
# c = 6a - 2
c = 6 * a - 2

# Step 4: Verify the solution satisfies all equations
assert 2 * a + b == 1
assert 3 * b + c == 1
assert 4 * c + a == 1

# Output the results
上禾實 = a  # 9/25斗
中禾實 = b  # 7/25斗
下禾實 = c  # 4/25斗

# Each秉數 is 1
上禾秉 = 1
中禾秉 = 1
下禾秉 = 1

# Final results
print(f"上禾 {上禾秉} 秉 實 {上禾實} 斗")
print(f"中禾 {中禾秉} 秉 實 {中禾實} 斗")
print(f"下禾 {下禾秉} 秉 實 {下禾實} 斗")


"""


### Explanation of the Solution:
1. **Equations Setup**:
   - The problem provides three equations based on the relationships between the different types of grain bundles (上禾, 中禾, 下禾).
   - These equations are solved using substitution and elimination.

2. **Step-by-Step Solution**:
   - Solve for one variable in terms of the others.
   - Substitute into the remaining equations to isolate and solve for each variable.

3. **Verification**:
   - After solving, verify that the solution satisfies all the original equations.

### Final Answer:
- 上禾: 1 秉, 實 9/25 斗
- 中禾: 1 秉, 實 7/25 斗
- 下禾: 1 秉, 實 4/25 斗
"""


"""
Variable 'a' has wrong value. Expected: 1, Actual: 9/25
Variable 'b' has wrong value. Expected: 9/25, Actual: 7/25
Variable 'c' has wrong value. Expected: 1, Actual: 4/25
Missing variable in output: 'd'
Missing variable in output: 'e'
Missing variable in output: 'f'"""
