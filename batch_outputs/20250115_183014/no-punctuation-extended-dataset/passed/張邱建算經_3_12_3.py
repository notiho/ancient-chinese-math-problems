"""
今有孟仲季兄弟三人各持絹不知疋數大兄謂二弟曰我得汝等絹各半得滿七十九疋中弟曰我得兄弟絹各半得滿六十八疋小弟曰我得二兄絹各半得滿五十七疋問兄弟本持絹各幾何
術曰大兄二中弟一小弟一合一百五十八疋大兄一中弟二小弟一合一百三十六疋大兄一中弟一小二合一百一十四疋如方程而求即得
方程術曰置上禾三秉中禾二秉下禾一秉實三十九斗於右方中左禾列如右方以右行上禾遍乘中行而以直除又乘其次亦以直除然以中行中禾不盡者遍乘左行而以直除左方下禾不盡者上為法下為實實即下禾之實求中禾以法乘中行下實而除下禾之實餘如中禾秉數而一即中禾之實求上禾亦以法乘右行下實而除下禾中禾之實餘如上禾秉數而一即上禾之實實皆如法各得一斗答曰孟 a疋 仲 b疋 季 c疋
"""

"""
Suppose there are three brothers: Meng, Zhong, and Ji. Each holds an unknown number of bolts of silk.
The eldest brother (Meng) says to his two younger brothers: "If I take half of each of your silk bolts, I will have a total of 79 bolts."
The second brother (Zhong) says: "If I take half of the silk bolts from my elder and younger brothers, I will have a total of 68 bolts."
The youngest brother (Ji) says: "If I take half of the silk bolts from my two elder brothers, I will have a total of 57 bolts."
Question: How many bolts of silk does each brother originally hold?

The procedure says: 
1. The eldest brother (Meng) has 2, the second brother (Zhong) has 1, and the youngest brother (Ji) has 1, together making 158 bolts.
2. The eldest brother (Meng) has 1, the second brother (Zhong) has 2, and the youngest brother (Ji) has 1, together making 136 bolts.
3. The eldest brother (Meng) has 1, the second brother (Zhong) has 1, and the youngest brother (Ji) has 2, together making 114 bolts.
Use the method of simultaneous equations to solve.

Answer: Meng has *a* bolts, Zhong has *b* bolts, and Ji has *c* bolts.
"""

# Define the equations based on the problem description:
# Let Meng = x, Zhong = y, Ji = z
# Equation 1: x + (1/2)y + (1/2)z = 79
# Equation 2: (1/2)x + y + (1/2)z = 68
# Equation 3: (1/2)x + (1/2)y + z = 57

# Multiply through by 2 to eliminate fractions:
# 2x + y + z = 158  (Equation 1)
# x + 2y + z = 136  (Equation 2)
# x + y + 2z = 114  (Equation 3)

# Step 1: Solve the system of equations using substitution/elimination.

# Coefficients of the equations:
# 2x + y + z = 158
# x + 2y + z = 136
# x + y + 2z = 114

# Eliminate x from Equation 1 and Equation 2:
# Multiply Equation 2 by 2 and subtract Equation 1:
# 2(x + 2y + z) - (2x + y + z) = 2(136) - 158
# 2x + 4y + 2z - 2x - y - z = 272 - 158
# 3y + z = 114  (New Equation A)

# Eliminate x from Equation 1 and Equation 3:
# Multiply Equation 3 by 2 and subtract Equation 1:
# 2(x + y + 2z) - (2x + y + z) = 2(114) - 158
# 2x + 2y + 4z - 2x - y - z = 228 - 158
# y + 3z = 70  (New Equation B)

# Step 2: Solve the two-variable system (New Equation A and New Equation B):
# 3y + z = 114  (Equation A)
# y + 3z = 70   (Equation B)

# Multiply Equation B by 3 and subtract Equation A:
# 3(y + 3z) - (3y + z) = 3(70) - 114
# 3y + 9z - 3y - z = 210 - 114
# 8z = 96
z = 96 // 8

# Substitute z = 12 into Equation B:
# y + 3(12) = 70
# y + 36 = 70
y = 70 - 36

# Substitute y = 34 and z = 12 into Equation 1:
# 2x + 34 + 12 = 158
# 2x + 46 = 158
# 2x = 158 - 46
# 2x = 112
x = 112 // 2

# Final results:
a = x  # Meng's bolts
b = y  # Zhong's bolts
c = z  # Ji's bolts
"""
"""
