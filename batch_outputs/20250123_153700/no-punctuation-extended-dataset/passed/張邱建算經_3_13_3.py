"""
今有甲乙丙三人持錢不知多少甲言我得乙大半得丙少半可滿一百乙言我得甲大半得丙半可滿一百丙言我得甲乙各大半可滿一百問甲乙丙持錢各幾何
術曰三甲二乙一丙錢三百四甲六乙三丙錢六百二甲二乙三丙錢三百如方程即得
方程術曰置上禾三秉中禾二秉下禾一秉實三十九斗於右方中左禾列如右方以右行上禾遍乘中行而以直除又乘其次亦以直除然以中行中禾不盡者遍乘左行而以直除左方下禾不盡者上為法下為實實即下禾之實求中禾以法乘中行下實而除下禾之實餘如中禾秉數而一即中禾之實求上禾亦以法乘右行下實而除下禾中禾之實餘如上禾秉數而一即上禾之實實皆如法各得一斗
答曰甲 a 乙 b 丙 c
"""

"""
Suppose there are three people, Jia, Yi, and Bing, holding an unknown amount of money.

Jia says: If I take more than half of Yi's money and less than half of Bing's money, I can reach 100.
Yi says: If I take more than half of Jia's money and half of Bing's money, I can reach 100.
Bing says: If I take more than half of Jia's money and more than half of Yi's money, I can reach 100.

Question: How much money does each of Jia, Yi, and Bing hold?

The procedure says: 
- Represent the relationships as equations:
  3 Jia + 2 Yi + 1 Bing = 300
  4 Jia + 6 Yi + 3 Bing = 600
  2 Jia + 2 Yi + 3 Bing = 300
- Solve the equations using the method of elimination.

The answer says: Jia holds *a*, Yi holds *b*, and Bing holds *c*.
"""

# 方程術
# Equations:
# 3甲 + 2乙 + 1丙 = 300
# 4甲 + 6乙 + 3丙 = 600
# 2甲 + 2乙 + 3丙 = 300

# Step 1: Eliminate 丙 from the first two equations
# Multiply the first equation by 3 and the second equation by 1
eq1 = [3 * 3, 3 * 2, 3 * 1, 3 * 300]  # 9甲 + 6乙 + 3丙 = 900
eq2 = [1 * 4, 1 * 6, 1 * 3, 1 * 600]  # 4甲 + 6乙 + 3丙 = 600

# Subtract eq2 from eq1
eq3 = [eq1[0] - eq2[0], eq1[1] - eq2[1], eq1[2] - eq2[2], eq1[3] - eq2[3]]  # 5甲 + 0乙 + 0丙 = 300
# Simplify eq3
甲 = Fraction(eq3[3], eq3[0])  # 甲 = 60

# Step 2: Substitute 甲 into the first equation to find 乙
# 3甲 + 2乙 + 1丙 = 300
# Substitute 甲 = 60
eq4 = [3 * 甲, 2, 1, 300]  # 180 + 2乙 + 1丙 = 300
eq4 = [0, eq4[1], eq4[2], eq4[3] - eq4[0]]  # 2乙 + 1丙 = 120

# Step 3: Eliminate 丙 from eq4 and the third equation
# eq4: 2乙 + 1丙 = 120
# Third equation: 2甲 + 2乙 + 3丙 = 300
# Substitute 甲 = 60 into the third equation
eq5 = [2 * 甲, 2, 3, 300]  # 120 + 2乙 + 3丙 = 300
eq5 = [0, eq5[1], eq5[2], eq5[3] - eq5[0]]  # 2乙 + 3丙 = 180

# Subtract eq4 from eq5
eq6 = [eq5[0] - eq4[0], eq5[1] - eq4[1], eq5[2] - eq4[2], eq5[3] - eq4[3]]  # 0乙 + 2丙 = 60
# Simplify eq6
丙 = Fraction(eq6[3], eq6[2])  # 丙 = 30

# Step 4: Substitute 丙 into eq4 to find 乙
# 2乙 + 1丙 = 120
# Substitute 丙 = 30
eq7 = [2, 1 * 丙, 120]  # 2乙 + 30 = 120
eq7 = [eq7[0], 0, eq7[2] - eq7[1]]  # 2乙 = 90
# Simplify eq7
乙 = Fraction(eq7[2], eq7[0])  # 乙 = 45

# Final answer
a = 甲  # 甲 = 60
b = 乙  # 乙 = 45
c = 丙  # 丙 = 30
"""
"""
