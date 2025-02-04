"""
今有上禾七秉損實一斗益之下禾二秉而實一十斗下禾八秉益實一斗與上禾二秉而實一十斗問上下禾實一秉各幾何
術曰如方程損之曰益益之曰損損實一斗者其實過一十斗也益實一斗者其實不滿一十斗也
方程術曰置上禾三秉中禾二秉下禾一秉實三十九斗於右方中左禾列如右方以右行上禾遍乘中行而以直除又乘其次亦以直除然以中行中禾不盡者遍乘左行而以直除左方下禾不盡者上為法下為實實即下禾之實求中禾以法乘中行下實而除下禾之實餘如中禾秉數而一即中禾之實求上禾亦以法乘右行下實而除下禾中禾之實餘如上禾秉數而一即上禾之實實皆如法各得一斗
荅曰上禾一秉實 a斗 下禾一秉實 b斗 
"""

"""
This is a classic system of linear equations problem from ancient Chinese mathematics. The problem involves determining the yield per unit (秉) of two types of crops, "上禾" (upper crop) and "下禾" (lower crop), based on the given relationships between their quantities and total yields. Below is the translation of the procedure into Python code:


"""


from fractions import Fraction

# Problem setup
# 上禾七秉損實一斗益之下禾二秉而實一十斗
# 下禾八秉益實一斗與上禾二秉而實一十斗
# Let x = yield of one unit of 上禾 (upper crop)
# Let y = yield of one unit of 下禾 (lower crop)

# Equation 1: 7x - 1 + 2y = 10
# Equation 2: 8y + 1 + 2x = 10

# Rewrite the equations:
# 7x + 2y = 11  (Equation 1)
# 2x + 8y = 9   (Equation 2)

# Solve using the 方程術 (method of elimination)

# Step 1: Multiply Equation 1 by 8 and Equation 2 by 2 to align coefficients of y
eq1 = [7 * 8, 2 * 8, 11 * 8]  # 56x + 16y = 88
eq2 = [2 * 2, 8 * 2, 9 * 2]   # 4x + 16y = 18

# Step 2: Subtract Equation 2 from Equation 1 to eliminate y
# (56x + 16y) - (4x + 16y) = 88 - 18
x_coefficient = eq1[0] - eq2[0]  # 56 - 4 = 52
constant = eq1[2] - eq2[2]       # 88 - 18 = 70
# 52x = 70
x = Fraction(constant, x_coefficient)  # x = 70 / 52 = 35 / 26

# Step 3: Substitute x into one of the original equations to solve for y
# Use Equation 1: 7x + 2y = 11
x_value = x
y_coefficient = 2
constant = 11 - 7 * x_value  # 11 - 7 * (35 / 26)
y = Fraction(constant, y_coefficient)  # y = (11 - 245 / 26) / 2 = (286 / 26 - 245 / 26) / 2 = 41 / 26 / 2 = 41 / 52

# Final results
a = x  # Yield of one unit of 上禾
b = y  # Yield of one unit of 下禾

print(f"上禾一秉實 {a}斗")
print(f"下禾一秉實 {b}斗")


"""


### Explanation of the Code:
1. The problem is translated into two linear equations based on the relationships provided.
2. The elimination method is used to solve the system of equations step by step, following the ancient Chinese 方程術 (method of elimination).
3. The results are expressed as fractions (`Fraction`) to maintain precision, as was done in ancient Chinese mathematics.

### Answer:
- 上禾一秉實 \( a = \frac{35}{26} \) 斗
- 下禾一秉實 \( b = \frac{41}{52} \) 斗
"""


"""
"""
