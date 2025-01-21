"""
今有孟仲季兄弟三人各持絹不知疋數大兄謂二弟曰我得汝等絹各半得滿七十九疋中弟曰我得兄弟絹各半得滿六十八疋小弟曰我得二兄絹各半得滿五十七疋問兄弟本持絹各幾何
術曰大兄二中弟一小弟一合一百五十八疋大兄一中弟二小弟一合一百三十六疋大兄一中弟一小二合一百一十四疋如方程而求即得
方程術曰置上禾三秉中禾二秉下禾一秉實三十九斗於右方中左禾列如右方以右行上禾遍乘中行而以直除又乘其次亦以直除然以中行中禾不盡者遍乘左行而以直除左方下禾不盡者上為法下為實實即下禾之實求中禾以法乘中行下實而除下禾之實餘如中禾秉數而一即中禾之實求上禾亦以法乘右行下實而除下禾中禾之實餘如上禾秉數而一即上禾之實實皆如法各得一斗答曰孟 a疋 仲 b疋 季 c疋
"""

"""
Suppose there are three brothers, Meng, Zhong, and Ji, each holding an unknown number of bolts of silk.
The eldest brother (Meng) says to his two younger brothers: "If I take half of each of your silk bolts, I will have 79 bolts in total."
The second brother (Zhong) says: "If I take half of each of your silk bolts, I will have 68 bolts in total."
The youngest brother (Ji) says: "If I take half of each of your silk bolts, I will have 57 bolts in total."
Question: How many bolts of silk does each brother originally hold?

The procedure says:
- Meng's silk bolts are 2, Zhong's are 1, and Ji's are 1, summing to 158 bolts.
- Meng's are 1, Zhong's are 2, and Ji's are 1, summing to 136 bolts.
- Meng's are 1, Zhong's are 1, and Ji's are 2, summing to 114 bolts.
Using the method of simultaneous equations, solve to find the answer.

The answer says: Meng has *a* bolts, Zhong has *b* bolts, and Ji has *c* bolts.
"""

# Define the equations based on the problem description:
# Meng's equation: Meng + 1/2 * Zhong + 1/2 * Ji = 79
# Zhong's equation: 1/2 * Meng + Zhong + 1/2 * Ji = 68
# Ji's equation: 1/2 * Meng + 1/2 * Zhong + Ji = 57

# Using the method of simultaneous equations (方程術):

# Coefficients for Meng, Zhong, and Ji
coefficients = [
    [1, Fraction(1, 2), Fraction(1, 2)],  # Meng's equation
    [Fraction(1, 2), 1, Fraction(1, 2)],  # Zhong's equation
    [Fraction(1, 2), Fraction(1, 2), 1]   # Ji's equation
]

# Constants on the right-hand side
constants = [79, 68, 57]

# Step 1: Eliminate Meng's coefficient from Zhong's and Ji's equations
factor1 = coefficients[1][0] / coefficients[0][0]
for i in range(3):
    coefficients[1][i] -= factor1 * coefficients[0][i]
constants[1] -= factor1 * constants[0]

factor2 = coefficients[2][0] / coefficients[0][0]
for i in range(3):
    coefficients[2][i] -= factor2 * coefficients[0][i]
constants[2] -= factor2 * constants[0]

# Step 2: Eliminate Zhong's coefficient from Ji's equation
factor3 = coefficients[2][1] / coefficients[1][1]
for i in range(3):
    coefficients[2][i] -= factor3 * coefficients[1][i]
constants[2] -= factor3 * constants[1]

# Step 3: Solve for Ji
c = constants[2] / coefficients[2][2]

# Step 4: Solve for Zhong
b = (constants[1] - coefficients[1][2] * c) / coefficients[1][1]

# Step 5: Solve for Meng
a = (constants[0] - coefficients[0][1] * b - coefficients[0][2] * c) / coefficients[0][0]

# Final answer
a = Fraction(a)
b = Fraction(b)
c = Fraction(c)

# Answer
a疋 = a
b疋 = b
c疋 = c
"""
"""
