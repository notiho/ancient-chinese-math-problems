"""
今有甲乙丙三人持錢不知多少甲言我得乙大半得丙少半可滿一百乙言我得甲大半得丙半可滿一百丙言我得甲乙各大半可滿一百問甲乙丙持錢各幾何
術曰三甲二乙一丙錢三百四甲六乙三丙錢六百二甲二乙三丙錢三百如方程即得
方程術曰置上禾三秉中禾二秉下禾一秉實三十九斗於右方中左禾列如右方以右行上禾遍乘中行而以直除又乘其次亦以直除然以中行中禾不盡者遍乘左行而以直除左方下禾不盡者上為法下為實實即下禾之實求中禾以法乘中行下實而除下禾之實餘如中禾秉數而一即中禾之實求上禾亦以法乘右行下實而除下禾中禾之實餘如上禾秉數而一即上禾之實實皆如法各得一斗
答曰甲 a 乙 b 丙 c
"""

"""
Suppose there are three people, Jia, Yi, and Bing, holding an unknown amount of money.
Jia says: If I take more than half of Yi's money and less than half of Bing's money, I will have 100.
Yi says: If I take more than half of Jia's money and half of Bing's money, I will have 100.
Bing says: If I take more than half of Jia's money and more than half of Yi's money, I will have 100.
Question: How much money do Jia, Yi, and Bing each hold?

The procedure says: 
- The equations are:
  3 Jia + 2 Yi + 1 Bing = 300
  4 Jia + 6 Yi + 3 Bing = 600
  2 Jia + 2 Yi + 3 Bing = 300
- Solve these equations using the method of elimination.

The answer says: Jia has *a*, Yi has *b*, and Bing has *c*.
"""

from fractions import Fraction

# Coefficients and constants from the equations:
# 3甲 + 2乙 + 1丙 = 300
# 4甲 + 6乙 + 3丙 = 600
# 2甲 + 2乙 + 3丙 = 300

# Define the coefficients and constants
A1, B1, C1, D1 = 3, 2, 1, 300
A2, B2, C2, D2 = 4, 6, 3, 600
A3, B3, C3, D3 = 2, 2, 3, 300

# Step 1: Eliminate Jia (甲) from the second and third equations
# Multiply the first equation by 4 and subtract the second equation
E2_A = A1 * 4 - A2
E2_B = B1 * 4 - B2
E2_C = C1 * 4 - C2
E2_D = D1 * 4 - D2

# Multiply the first equation by 2 and subtract the third equation
E3_A = A1 * 2 - A3
E3_B = B1 * 2 - B3
E3_C = C1 * 2 - C3
E3_D = D1 * 2 - D3

# Step 2: Eliminate Yi (乙) from the resulting equations
# Multiply the second resulting equation by E3_B and subtract the third resulting equation multiplied by E2_B
E4_B = E2_B * E3_B - E3_B * E2_B
E4_C = E2_C * E3_B - E3_C * E2_B
E4_D = E2_D * E3_B - E3_D * E2_B

# Step 3: Solve for Bing (丙)
C = Fraction(E4_D, E4_C)

# Step 4: Back-substitute to solve for Yi (乙)
B = Fraction(E2_D - E2_C * C, E2_B)

# Step 5: Back-substitute to solve for Jia (甲)
A = Fraction(D1 - B1 * B - C1 * C, A1)

# Assign the results
a = A
b = B
c = C
"""
Variable 'a' has wrong value. Expected: 60, Actual: -100
Variable 'b' has wrong value. Expected: 45, Actual: 225
Variable 'c' has wrong value. Expected: 30, Actual: 150"""
