"""
今有上禾七秉損實一斗益之下禾二秉而實一十斗下禾八秉益實一斗與上禾二秉而實一十斗問上下禾實一秉各幾何
術曰如方程損之曰益益之曰損損實一斗者其實過一十斗也益實一斗者其實不滿一十斗也
方程術曰置上禾三秉中禾二秉下禾一秉實三十九斗於右方中左禾列如右方以右行上禾遍乘中行而以直除又乘其次亦以直除然以中行中禾不盡者遍乘左行而以直除左方下禾不盡者上為法下為實實即下禾之實求中禾以法乘中行下實而除下禾之實餘如中禾秉數而一即中禾之實求上禾亦以法乘右行下實而除下禾中禾之實餘如上禾秉數而一即上禾之實實皆如法各得一斗荅曰上禾 a秉 實 b斗 下禾 c秉 實 d斗 
"""

"""
This is a complex problem involving a system of equations and proportional reasoning. Let's break it down step by step and encode the solution in Python.

### Problem Breakdown:
We are tasked with finding the yield (實) per秉 (unit of crop) for both 上禾 (upper crop) and 下禾 (lower crop). The problem provides relationships between the crops and their yields, which can be solved using a system of equations.

### Procedure:
1. **Interpret the relationships:**
   - 損實一斗益之下禾二秉而實一十斗: If the yield of 上禾 is reduced by 1 dou and added to 下禾 for 2 units, the total yield is 10 dou.
   - 下禾八秉益實一斗與上禾二秉而實一十斗: If the yield of 下禾 is increased by 1 dou and added to 上禾 for 2 units, the total yield is 10 dou.

2. **Set up equations:**
   Let `x` be the yield per秉 of 上禾 and `y` be the yield per秉 of 下禾. The equations are:
   - \( 7x - 1 + 2y = 10 \)
   - \( 8y + 1 + 2x = 10 \)

3. **Solve for `x` and `y`:**
   Use algebraic manipulation to solve the system of equations.

4. **Output the results:**
   Calculate the yield per秉 for both 上禾 and 下禾.

### Python Code:

"""


from fractions import Fraction

# Define the equations based on the problem description
# Equation 1: 7x - 1 + 2y = 10
# Equation 2: 8y + 1 + 2x = 10

# Solve for x (yield per秉 of 上禾) and y (yield per秉 of 下禾)
# Rearrange Equation 1: 7x + 2y = 11
# Rearrange Equation 2: 2x + 8y = 9

# Coefficients for the system of equations
a1, b1, c1 = 7, 2, 11  # 7x + 2y = 11
a2, b2, c2 = 2, 8, 9   # 2x + 8y = 9

# Solve using substitution or elimination
# Multiply Equation 1 by 8 and Equation 2 by 2 to align coefficients of y
eq1_mult = [a1 * 8, b1 * 8, c1 * 8]  # 56x + 16y = 88
eq2_mult = [a2 * 2, b2 * 2, c2 * 2]  # 4x + 16y = 18

# Subtract the modified equations to eliminate y
# (56x + 16y) - (4x + 16y) = 88 - 18
x_coeff = eq1_mult[0] - eq2_mult[0]  # 56x - 4x = 52x
y_coeff = eq1_mult[1] - eq2_mult[1]  # 16y - 16y = 0
const = eq1_mult[2] - eq2_mult[2]    # 88 - 18 = 70

# Solve for x
x = Fraction(const, x_coeff)  # x = 70 / 52 = 35 / 26

# Substitute x back into one of the original equations to solve for y
# Using 7x + 2y = 11
y = Fraction(c1 - a1 * x, b1)  # y = (11 - 7x) / 2

# Results
a = 7  # 上禾秉數
b = x  # 上禾實 per秉
c = 8  # 下禾秉數
d = y  # 下禾實 per秉

print(f"上禾 {a}秉 實 {b}斗")
print(f"下禾 {c}秉 實 {d}斗")


"""


### Explanation of the Code:
1. The equations are derived from the problem description.
2. The system of equations is solved using elimination to find `x` (yield per秉 of 上禾).
3. The value of `x` is substituted back into one of the original equations to find `y` (yield per秉 of 下禾).
4. The results are printed in the required format.

### Answer:
The yield per秉 for 上禾 and 下禾 is calculated as fractions (or decimals, if preferred).
"""


"""
Variable 'a' has wrong value. Expected: 1, Actual: 7
Variable 'c' has wrong value. Expected: 1, Actual: 8"""
