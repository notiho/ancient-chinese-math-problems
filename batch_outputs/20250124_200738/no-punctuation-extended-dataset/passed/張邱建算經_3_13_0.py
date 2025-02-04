"""
今有甲乙丙三人持錢不知多少甲言我得乙大半得丙少半可滿一百乙言我得甲大半得丙半可滿一百丙言我得甲乙各大半可滿一百問甲乙丙持錢各幾何
術曰三甲二乙一丙錢三百四甲六乙三丙錢六百二甲二乙三丙錢三百如方程即得
方程術曰置上禾三秉中禾二秉下禾一秉實三十九斗於右方中左禾列如右方以右行上禾遍乘中行而以直除又乘其次亦以直除然以中行中禾不盡者遍乘左行而以直除左方下禾不盡者上為法下為實實即下禾之實求中禾以法乘中行下實而除下禾之實餘如中禾秉數而一即中禾之實求上禾亦以法乘右行下實而除下禾中禾之實餘如上禾秉數而一即上禾之實實皆如法各得一斗
答曰甲 a 乙 b 丙 c
"""

#----- content starts here -----
"""
Suppose there are three people, Jia, Yi, and Bing, holding an unknown amount of money.

Jia says: If I take more than half of Yi's money and less than half of Bing's money, I can make 100.
Yi says: If I take more than half of Jia's money and half of Bing's money, I can make 100.
Bing says: If I take more than half of both Jia's and Yi's money, I can make 100.

Question: How much money does each of Jia, Yi, and Bing hold?

The procedure says: 
1. Represent the relationships as equations:
   - 3 Jia + 2 Yi + 1 Bing = 300
   - 4 Jia + 6 Yi + 3 Bing = 600
   - 2 Jia + 2 Yi + 3 Bing = 300
2. Solve the equations using the method of elimination:
   - Place the coefficients of Jia, Yi, and Bing in rows.
   - Use elimination to simplify and solve for each variable.

Answer: Jia holds *a*, Yi holds *b*, and Bing holds *c*.
"""

from fractions import Fraction

# Coefficients of the equations
# 3甲 + 2乙 + 1丙 = 300
# 4甲 + 6乙 + 3丙 = 600
# 2甲 + 2乙 + 3丙 = 300

# Define the equations
eq1 = [3, 2, 1, 300]  # 3甲 + 2乙 + 1丙 = 300
eq2 = [4, 6, 3, 600]  # 4甲 + 6乙 + 3丙 = 600
eq3 = [2, 2, 3, 300]  # 2甲 + 2乙 + 3丙 = 300

# Step 1: Eliminate 甲 from eq2 and eq3 using eq1
factor1 = Fraction(eq2[0], eq1[0])  # Factor to eliminate 甲 from eq2
factor2 = Fraction(eq3[0], eq1[0])  # Factor to eliminate 甲 from eq3

# Subtract (factor * eq1) from eq2 and eq3
eq2 = [eq2[i] - factor1 * eq1[i] for i in range(4)]
eq3 = [eq3[i] - factor2 * eq1[i] for i in range(4)]

# Step 2: Eliminate 乙 from eq3 using the modified eq2
factor3 = Fraction(eq3[1], eq2[1])  # Factor to eliminate 乙 from eq3
eq3 = [eq3[i] - factor3 * eq2[i] for i in range(4)]

# Step 3: Solve for 丙 (eq3 now only contains 丙)
c = Fraction(eq3[3], eq3[2])

# Step 4: Solve for 乙 using the modified eq2
b = Fraction(eq2[3] - eq2[2] * c, eq2[1])

# Step 5: Solve for 甲 using eq1
a = Fraction(eq1[3] - eq1[1] * b - eq1[2] * c, eq1[0])

# Final answer
a, b, c  # Jia, Yi, Bing#----- content ends here -----

"""
"""
