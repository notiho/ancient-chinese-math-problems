"""
今有甲乙丙三人持錢不知多少甲言我得乙大半得丙少半可滿一百乙言我得甲大半得丙半可滿一百丙言我得甲乙各大半可滿一百問甲乙丙持錢各幾何
術曰三甲二乙一丙錢三百四甲六乙三丙錢六百二甲二乙三丙錢三百如方程即得
方程術曰置上禾三秉中禾二秉下禾一秉實三十九斗於右方中左禾列如右方以右行上禾遍乘中行而以直除又乘其次亦以直除然以中行中禾不盡者遍乘左行而以直除左方下禾不盡者上為法下為實實即下禾之實求中禾以法乘中行下實而除下禾之實餘如中禾秉數而一即中禾之實求上禾亦以法乘右行下實而除下禾中禾之實餘如上禾秉數而一即上禾之實實皆如法各得一斗答曰甲 a 乙 b 丙 c
"""

"""
Suppose there are three people, Jia, Yi, and Bing, holding an unknown amount of money.
Jia says: If I take more than half of Yi's money and less than half of Bing's money, I can make 100.
Yi says: If I take more than half of Jia's money and half of Bing's money, I can make 100.
Bing says: If I take more than half of both Jia's and Yi's money, I can make 100.
Question: How much money do Jia, Yi, and Bing each hold?

The procedure says: 
- Three Jia, two Yi, and one Bing together hold 300.
- Four Jia, six Yi, and three Bing together hold 600.
- Two Jia, two Yi, and three Bing together hold 300.
Using the method of solving simultaneous equations, the solution is obtained.

The method for solving equations says:
- Place the coefficients of the first equation as the upper row, the second equation as the middle row, and the third equation as the lower row.
- Place the constants (right-hand side) of the equations on the right.
- Multiply the upper row by the middle row and divide by the diagonal coefficient, then proceed similarly for the lower row.
- Eliminate terms step by step to isolate variables and solve for each.

Answer: Jia holds *a*, Yi holds *b*, and Bing holds *c*.
"""

from fractions import Fraction

# Coefficients and constants from the equations:
# 3甲 + 2乙 + 1丙 = 300
# 4甲 + 6乙 + 3丙 = 600
# 2甲 + 2乙 + 3丙 = 300

# Initialize the coefficients and constants
上禾 = [3, 2, 1]  # Coefficients for Jia, Yi, Bing in the first equation
中禾 = [4, 6, 3]  # Coefficients for Jia, Yi, Bing in the second equation
下禾 = [2, 2, 3]  # Coefficients for Jia, Yi, Bing in the third equation
右方 = [300, 600, 300]  # Constants on the right-hand side

# Step 1: Eliminate Jia (甲) from the second and third equations
# Multiply the first equation by 4 (middle row's Jia coefficient) and subtract the second equation
中禾 = [4 * 上禾[i] - 中禾[i] for i in range(3)]
右方[1] = 4 * 右方[0] - 右方[1]

# Multiply the first equation by 2 (lower row's Jia coefficient) and subtract the third equation
下禾 = [2 * 上禾[i] - 下禾[i] for i in range(3)]
右方[2] = 2 * 右方[0] - 右方[2]

# Step 2: Eliminate Yi (乙) from the third equation
# Multiply the modified second equation by 2 (lower row's Yi coefficient) and subtract the third equation
下禾 = [2 * 中禾[i] - 下禾[i] for i in range(3)]
右方[2] = 2 * 右方[1] - 右方[2]

# Step 3: Solve for Bing (丙)
c = Fraction(右方[2], 下禾[2])  # 丙 = constant / coefficient of 丙 in the third equation

# Step 4: Solve for Yi (乙)
b = Fraction(右方[1] - 中禾[2] * c, 中禾[1])  # 乙 = (constant - coefficient of 丙 * 丙) / coefficient of 乙

# Step 5: Solve for Jia (甲)
a = Fraction(右方[0] - 上禾[1] * b - 上禾[2] * c, 上禾[0])  # 甲 = (constant - coefficient of 乙 * 乙 - coefficient of 丙 * 丙) / coefficient of 甲

# Final answer
a, b, c  # Jia, Yi, Bing
"""
Variable 'a' has wrong value. Expected: 60, Actual: -100
Variable 'b' has wrong value. Expected: 45, Actual: 150
Variable 'c' has wrong value. Expected: 30, Actual: 300"""
