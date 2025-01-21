"""
今有孟仲季兄弟三人各持絹不知疋數大兄謂二弟曰我得汝等絹各半得滿七十九疋中弟曰我得兄弟絹各半得滿六十八疋小弟曰我得二兄絹各半得滿五十七疋問兄弟本持絹各幾何
術曰大兄二中弟一小弟一合一百五十八疋大兄一中弟二小弟一合一百三十六疋大兄一中弟一小二合一百一十四疋如方程而求即得
方程術曰置上禾三秉中禾二秉下禾一秉實三十九斗於右方中左禾列如右方以右行上禾遍乘中行而以直除又乘其次亦以直除然以中行中禾不盡者遍乘左行而以直除左方下禾不盡者上為法下為實實即下禾之實求中禾以法乘中行下實而除下禾之實餘如中禾秉數而一即中禾之實求上禾亦以法乘右行下實而除下禾中禾之實餘如上禾秉數而一即上禾之實實皆如法各得一斗答曰孟 a疋 仲 b疋 季 c疋
"""

"""
Suppose there are three brothers: Meng (the eldest), Zhong (the middle), and Ji (the youngest). Each holds an unknown number of bolts of silk.
The eldest brother says to his two younger brothers: "If I take half of each of your silk bolts, I will have a total of 79 bolts."
The middle brother says: "If I take half of each of your silk bolts, I will have a total of 68 bolts."
The youngest brother says: "If I take half of each of your silk bolts, I will have a total of 57 bolts."
Question: How many bolts of silk does each brother originally hold?

The procedure says:
- The eldest brother's equation: 2 * Meng + 1 * Zhong + 1 * Ji = 158 bolts.
- The middle brother's equation: 1 * Meng + 2 * Zhong + 1 * Ji = 136 bolts.
- The youngest brother's equation: 1 * Meng + 1 * Zhong + 2 * Ji = 114 bolts.
Solve these equations using the method of simultaneous equations.

The method of simultaneous equations says:
- Place the coefficients of Meng, Zhong, and Ji in rows, with the totals on the right-hand side.
- Use elimination and substitution to solve for each variable.

Answer: Meng holds *a* bolts, Zhong holds *b* bolts, and Ji holds *c* bolts.
"""

# Coefficients and totals from the equations:
# 2 * Meng + 1 * Zhong + 1 * Ji = 158
# 1 * Meng + 2 * Zhong + 1 * Ji = 136
# 1 * Meng + 1 * Zhong + 2 * Ji = 114

# Step 1: Define the coefficients and totals
A1, B1, C1, Total1 = 2, 1, 1, 158  # Equation 1
A2, B2, C2, Total2 = 1, 2, 1, 136  # Equation 2
A3, B3, C3, Total3 = 1, 1, 2, 114  # Equation 3

# Step 2: Eliminate Meng (A1, A2, A3) to reduce to two equations
# Multiply Equation 2 by 2 and subtract Equation 1
E2_Multiplied = (2 * A2, 2 * B2, 2 * C2, 2 * Total2)
Reduced2 = (E2_Multiplied[0] - A1, E2_Multiplied[1] - B1, E2_Multiplied[2] - C1, E2_Multiplied[3] - Total1)

# Multiply Equation 3 by 2 and subtract Equation 1
E3_Multiplied = (2 * A3, 2 * B3, 2 * C3, 2 * Total3)
Reduced3 = (E3_Multiplied[0] - A1, E3_Multiplied[1] - B1, E3_Multiplied[2] - C1, E3_Multiplied[3] - Total1)

# Step 3: Eliminate Zhong (B1, B2, B3) to solve for Ji
# Multiply Reduced3 by Reduced2's B coefficient and subtract Reduced2
Factor = Reduced3[1]  # Coefficient of Zhong in Reduced3
Reduced3_Scaled = (Reduced3[0] * Reduced2[1], Reduced3[1] * Reduced2[1], Reduced3[2] * Reduced2[1], Reduced3[3] * Reduced2[1])
Reduced2_Scaled = (Reduced2[0] * Factor, Reduced2[1] * Factor, Reduced2[2] * Factor, Reduced2[3] * Factor)
Final_Reduced = (Reduced3_Scaled[0] - Reduced2_Scaled[0], Reduced3_Scaled[1] - Reduced2_Scaled[1], Reduced3_Scaled[2] - Reduced2_Scaled[2], Reduced3_Scaled[3] - Reduced2_Scaled[3])

# Solve for Ji
c = Fraction(Final_Reduced[3], Final_Reduced[2])

# Step 4: Back-substitute to solve for Zhong
b = Fraction(Reduced2[3] - Reduced2[2] * c, Reduced2[1])

# Step 5: Back-substitute to solve for Meng
a = Fraction(Total1 - B1 * b - C1 * c, A1)

# Final answer
a, b, c  # Meng, Zhong, Ji
"""
"""
