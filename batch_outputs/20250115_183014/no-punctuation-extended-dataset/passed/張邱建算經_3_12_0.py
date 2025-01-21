"""
今有孟仲季兄弟三人各持絹不知疋數大兄謂二弟曰我得汝等絹各半得滿七十九疋中弟曰我得兄弟絹各半得滿六十八疋小弟曰我得二兄絹各半得滿五十七疋問兄弟本持絹各幾何
術曰大兄二中弟一小弟一合一百五十八疋大兄一中弟二小弟一合一百三十六疋大兄一中弟一小二合一百一十四疋如方程而求即得
方程術曰置上禾三秉中禾二秉下禾一秉實三十九斗於右方中左禾列如右方以右行上禾遍乘中行而以直除又乘其次亦以直除然以中行中禾不盡者遍乘左行而以直除左方下禾不盡者上為法下為實實即下禾之實求中禾以法乘中行下實而除下禾之實餘如中禾秉數而一即中禾之實求上禾亦以法乘右行下實而除下禾中禾之實餘如上禾秉數而一即上禾之實實皆如法各得一斗答曰孟 a疋 仲 b疋 季 c疋
"""

"""
Suppose there are three brothers: Meng (the eldest), Zhong (the middle), and Ji (the youngest). Each holds an unknown number of bolts of silk.
The eldest brother says to the other two: "If I take half of each of your silk, I will have 79 bolts in total."
The middle brother says: "If I take half of each of your silk, I will have 68 bolts in total."
The youngest brother says: "If I take half of each of your silk, I will have 57 bolts in total."
Question: How many bolts of silk does each brother originally hold?

The procedure says:
- The eldest brother's equation: Meng + 1/2 * Zhong + 1/2 * Ji = 79
- The middle brother's equation: 1/2 * Meng + Zhong + 1/2 * Ji = 68
- The youngest brother's equation: 1/2 * Meng + 1/2 * Zhong + Ji = 57

Using the method of simultaneous equations (方程術), solve for Meng, Zhong, and Ji.

Answer: Meng holds *a* bolts, Zhong holds *b* bolts, and Ji holds *c* bolts.
"""

from fractions import Fraction

# Define the equations based on the problem
# Meng + 1/2 * Zhong + 1/2 * Ji = 79
# 1/2 * Meng + Zhong + 1/2 * Ji = 68
# 1/2 * Meng + 1/2 * Zhong + Ji = 57

# Represent the coefficients of the equations
# Coefficients for Meng, Zhong, Ji, and the constant term
eq1 = [1, Fraction(1, 2), Fraction(1, 2), 79]
eq2 = [Fraction(1, 2), 1, Fraction(1, 2), 68]
eq3 = [Fraction(1, 2), Fraction(1, 2), 1, 57]

# Eliminate Meng from eq2 and eq3 using eq1
factor1 = eq2[0] / eq1[0]
factor2 = eq3[0] / eq1[0]

for i in range(4):
    eq2[i] -= factor1 * eq1[i]
    eq3[i] -= factor2 * eq1[i]

# Eliminate Zhong from eq3 using eq2
factor3 = eq3[1] / eq2[1]

for i in range(4):
    eq3[i] -= factor3 * eq2[i]

# Solve for Ji
c = eq3[3] / eq3[2]

# Solve for Zhong using eq2
b = (eq2[3] - eq2[2] * c) / eq2[1]

# Solve for Meng using eq1
a = (eq1[3] - eq1[1] * b - eq1[2] * c) / eq1[0]

# Results
a, b, c  # Meng, Zhong, Ji
"""
"""
