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
Question: How much money do Jia, Yi, and Bing each hold?

The procedure says:
- Three Jia, two Yi, and one Bing together hold 300.
- Four Jia, six Yi, and three Bing together hold 600.
- Two Jia, two Yi, and three Bing together hold 300.
Using the method of solving simultaneous equations, we can find the solution.

The method for solving equations says:
- Place the coefficients of the first equation (3, 2, 1) as the top row, the second equation (4, 6, 3) as the middle row, and the third equation (2, 2, 3) as the bottom row.
- Place the constants (300, 600, 300) on the right-hand side.
- Solve the system by elimination:
  - Multiply rows and subtract to eliminate variables systematically.
  - Use the resulting equations to back-substitute and find the values of each variable.

Answer: Jia holds *a*, Yi holds *b*, and Bing holds *c*.
"""

# Coefficients and constants from the equations
# 3甲 + 2乙 + 1丙 = 300
# 4甲 + 6乙 + 3丙 = 600
# 2甲 + 2乙 + 3丙 = 300

# Define the coefficients and constants
甲1, 乙1, 丙1, 常數1 = 3, 2, 1, 300
甲2, 乙2, 丙2, 常數2 = 4, 6, 3, 600
甲3, 乙3, 丙3, 常數3 = 2, 2, 3, 300

# Eliminate 甲 from the second and third equations
# Multiply the first equation by 4 and subtract the second equation
倍1 = 4
倍2 = 3
新乙2 = 倍1 * 乙1 - 乙2
新丙2 = 倍1 * 丙1 - 丙2
新常數2 = 倍1 * 常數1 - 常數2

# Multiply the first equation by 2 and subtract the third equation
新乙3 = 倍2 *乙1-乙3
"""
Missing variable in output: 'a'
Missing variable in output: 'b'
Missing variable in output: 'c'"""
