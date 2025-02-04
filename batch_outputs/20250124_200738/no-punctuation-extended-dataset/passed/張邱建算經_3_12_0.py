"""
今有孟仲季兄弟三人各持絹不知疋數大兄謂二弟曰我得汝等絹各半得滿七十九疋中弟曰我得兄弟絹各半得滿六十八疋小弟曰我得二兄絹各半得滿五十七疋問兄弟本持絹各幾何
術曰大兄二中弟一小弟一合一百五十八疋大兄一中弟二小弟一合一百三十六疋大兄一中弟一小二合一百一十四疋如方程而求即得
方程術曰置上禾三秉中禾二秉下禾一秉實三十九斗於右方中左禾列如右方以右行上禾遍乘中行而以直除又乘其次亦以直除然以中行中禾不盡者遍乘左行而以直除左方下禾不盡者上為法下為實實即下禾之實求中禾以法乘中行下實而除下禾之實餘如中禾秉數而一即中禾之實求上禾亦以法乘右行下實而除下禾中禾之實餘如上禾秉數而一即上禾之實實皆如法各得一斗
答曰孟 a疋 仲 b疋 季 c疋
"""

#----- content starts here -----
"""
Suppose there are three brothers: Meng, Zhong, and Ji. Each holds an unknown number of bolts of silk.
The eldest brother (Meng) says to his two younger brothers: "If I take half of each of your silk, I will have 79 bolts in total."
The second brother (Zhong) says: "If I take half of each of your silk, I will have 68 bolts in total."
The youngest brother (Ji) says: "If I take half of each of your silk, I will have 57 bolts in total."
Question: How many bolts of silk does each brother originally hold?

The procedure says:
- Meng's silk multiplied by 2, plus Zhong's silk multiplied by 1, plus Ji's silk multiplied by 1, equals 158 bolts.
- Meng's silk multiplied by 1, plus Zhong's silk multiplied by 2, plus Ji's silk multiplied by 1, equals 136 bolts.
- Meng's silk multiplied by 1, plus Zhong's silk multiplied by 1, plus Ji's silk multiplied by 2, equals 114 bolts.
Solve this system of equations using the method of simultaneous equations.

The answer says: Meng has *a* bolts, Zhong has *b* bolts, and Ji has *c* bolts.
"""

# Define the equations based on the problem:
# 2M + Z + J = 158
# M + 2Z + J = 136
# M + Z + 2J = 114

# Step 1: Eliminate one variable (e.g., Meng's silk, M) using the first two equations.
# Multiply the second equation by 2 and subtract the first equation:
# 2(M + 2Z + J) - (2M + Z + J) = 2(136) - 158
# 2M + 4Z + 2J - 2M - Z - J = 272 - 158
# 3Z + J = 114

# Step 2: Eliminate the same variable (M) using the first and third equations.
# Multiply the third equation by 2 and subtract the first equation:
# 2(M + Z + 2J) - (2M + Z + J) = 2(114) - 158
# 2M + 2Z + 4J - 2M - Z - J = 228 - 158
# Z + 3J = 70

# Step 3: Solve the resulting system of two equations with two variables:
# 3Z + J = 114
# Z + 3J = 70

# Multiply the second equation by 3 and subtract the first equation:
# 3(Z + 3J) - (3Z + J) = 3(70) - 114
# 3Z + 9J - 3Z - J = 210 - 114
# 8J = 96
J = Fraction(96, 8)

# Substitute J back into the first equation:
# 3Z + J = 114
# 3Z + 12 = 114
# 3Z = 102
Z = Fraction(102, 3)

# Substitute Z and J into the first original equation to solve for M:
# 2M + Z + J = 158
# 2M + 34 + 12 = 158
# 2M = 158 - 46
# 2M = 112
M = Fraction(112, 2)

# Final results:
a = M  # Meng's silk
b = Z  # Zhong's silk
c = J  # Ji's silk#----- content ends here -----

"""
"""
