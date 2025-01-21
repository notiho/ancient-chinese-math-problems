"""
今有甲乙丙三人持錢不知多少甲言我得乙大半得丙少半可滿一百乙言我得甲大半得丙半可滿一百丙言我得甲乙各大半可滿一百問甲乙丙持錢各幾何
術曰三甲二乙一丙錢三百四甲六乙三丙錢六百二甲二乙三丙錢三百如方程即得
方程術曰置上禾三秉中禾二秉下禾一秉實三十九斗於右方中左禾列如右方以右行上禾遍乘中行而以直除又乘其次亦以直除然以中行中禾不盡者遍乘左行而以直除左方下禾不盡者上為法下為實實即下禾之實求中禾以法乘中行下實而除下禾之實餘如中禾秉數而一即中禾之實求上禾亦以法乘右行下實而除下禾中禾之實餘如上禾秉數而一即上禾之實實皆如法各得一斗答曰甲 a 乙 b 丙 c
"""

"""
Suppose there are three people, Jia, Yi, and Bing, holding an unknown amount of money.
Jia says: If I take more than half of Yi's money and less than half of Bing's money, I can reach 100.
Yi says: If I take more than half of Jia's money and half of Bing's money, I can reach 100.
Bing says: If I take more than half of both Jia's and Yi's money, I can reach 100.
Question: How much money does each of Jia, Yi, and Bing hold?

The procedure says:
- Three Jia, two Yi, and one Bing together make 300.
- Four Jia, six Yi, and three Bing together make 600.
- Two Jia, two Yi, and three Bing together make 300.
Using the method of solving simultaneous equations, the solution is obtained.

The method of solving equations says:
- Place the coefficients of the first equation (3, 2, 1) and the constant (300) on the right side.
- Place the coefficients of the second equation (4, 6, 3) and the constant (600) in the middle.
- Place the coefficients of the third equation (2, 2, 3) and the constant (300) on the left.
- Solve step by step using elimination and substitution to find the values of Jia, Yi, and Bing.

Answer: Jia holds *a*, Yi holds *b*, and Bing holds *c*.
"""

# Coefficients and constants from the equations:
# 3甲 + 2乙 + 1丙 = 300
# 4甲 + 6乙 + 3丙 = 600
# 2甲 + 2乙 + 3丙 = 300

# Step 1: Eliminate one variable (丙) using the first two equations.
# Multiply the first equation by 3 and the second equation by 1 to align 丙 coefficients.
eq1 = [3, 2, 1, 300]  # 3甲 + 2乙 + 1丙 = 300
eq2 = [4, 6, 3, 600]  # 4甲 + 6乙 + 3丙 = 600
eq3 = [2, 2, 3, 300]  # 2甲 + 2乙 + 3丙 = 300

# Align 丙 coefficients by multiplying eq1 by 3:
eq1_scaled = [3 * i for i in eq1]  # 9甲 + 6乙 + 3丙 = 900
# Subtract eq2 from eq1_scaled to eliminate 丙:
eq4 = [eq1_scaled[i] - eq2[i] for i in range(4)]  # 5甲 + 0乙 + 0丙 = 300
# Simplify eq4:
eq4 = [5, 0, 0, 300]  # 5甲 = 300

# Step 2: Solve for 甲 (Jia's money).
甲 = eq4[3] / eq4[0]  # 甲 = 300 / 5
甲 = 60

# Step 3: Substitute 甲 into the first equation to solve for 乙 and 丙.
# Substitute 甲 = 60 into eq1: 3甲 + 2乙 + 1丙 = 300
eq1_sub = [3 * 甲, 2, 1, 300]  # 180 + 2乙 + 1丙 = 300
# Simplify eq1_sub:
eq1_sub[3] -= eq1_sub[0]  # 2乙 + 1丙 = 120
eq1_sub = [0, 2, 1, 120]  # 2乙 + 1丙 = 120

# Step 4: Substitute 甲 into the third equation to solve for 乙 and 丙.
# Substitute 甲 = 60 into eq3: 2甲 + 2乙 + 3丙 = 300
eq3_sub = [2 * 甲, 2, 3, 300]  # 120 + 2乙 + 3丙 = 300
# Simplify eq3_sub:
eq3_sub[3] -= eq3_sub[0]  # 2乙 + 3丙 = 180
eq3_sub = [0, 2, 3, 180]  # 2乙 + 3丙 = 180

# Step 5: Solve the system of two equations (from eq1_sub and eq3_sub) for 乙 and 丙.
# From eq1_sub: 2乙 + 1丙 = 120
# From eq3_sub: 2乙 + 3丙 = 180
# Subtract eq1_sub from eq3_sub to eliminate 乙:
eq5 = [eq3_sub[i] - eq1_sub[i] for i in range(4)]  # 0乙 + 2丙 = 60
# Simplify eq5:
丙 = eq5[3] / eq5[2]  # 丙 = 60 / 2
丙 = 30

# Substitute 丙 = 30 into eq1_sub to solve for 乙:
# 2乙 + 1丙 = 120
eq1_sub[3] -= eq1_sub[2] * 丙  # 2乙 = 120 - 30
乙 = eq1_sub[3] / eq1_sub[1]  # 乙 = 90 / 2
乙 = 45

# Final answer:
a = 甲  # Jia's money
b = 乙  # Yi's money
c = 丙  # Bing's money
"""
"""
