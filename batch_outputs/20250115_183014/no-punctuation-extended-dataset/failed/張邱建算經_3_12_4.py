"""
今有孟仲季兄弟三人各持絹不知疋數大兄謂二弟曰我得汝等絹各半得滿七十九疋中弟曰我得兄弟絹各半得滿六十八疋小弟曰我得二兄絹各半得滿五十七疋問兄弟本持絹各幾何
術曰大兄二中弟一小弟一合一百五十八疋大兄一中弟二小弟一合一百三十六疋大兄一中弟一小二合一百一十四疋如方程而求即得
方程術曰置上禾三秉中禾二秉下禾一秉實三十九斗於右方中左禾列如右方以右行上禾遍乘中行而以直除又乘其次亦以直除然以中行中禾不盡者遍乘左行而以直除左方下禾不盡者上為法下為實實即下禾之實求中禾以法乘中行下實而除下禾之實餘如中禾秉數而一即中禾之實求上禾亦以法乘右行下實而除下禾中禾之實餘如上禾秉數而一即上禾之實實皆如法各得一斗答曰孟 a疋 仲 b疋 季 c疋
"""

"""
Suppose there are three brothers, Meng, Zhong, and Ji, each holding an unknown number of bolts of silk.
The eldest brother (Meng) says to his two younger brothers: "If I take half of each of your silk, I will have 79 bolts in total."
The second brother (Zhong) says: "If I take half of each of your silk, I will have 68 bolts in total."
The youngest brother (Ji) says: "If I take half of each of your silk, I will have 57 bolts in total."
Question: How many bolts of silk does each brother originally hold?

The procedure says:
- Meng's silk multiplied by 2, plus Zhong's silk multiplied by 1, plus Ji's silk multiplied by 1, equals 158 bolts.
- Meng's silk multiplied by 1, plus Zhong's silk multiplied by 2, plus Ji's silk multiplied by 1, equals 136 bolts.
- Meng's silk multiplied by 1, plus Zhong's silk multiplied by 1, plus Ji's silk multiplied by 2, equals 114 bolts.
Using the method of simultaneous equations, solve for the unknowns.

Answer: Meng holds *a* bolts, Zhong holds *b* bolts, and Ji holds *c* bolts.
"""

# Define the coefficients and constants of the equations
# Equation 1: 2孟 + 1仲 + 1季 = 158
# Equation 2: 1孟 + 2仲 + 1季 = 136
# Equation 3: 1孟 + 1仲 + 2季 = 114

# Coefficients
A = [[2, 1, 1],  # Coefficients for Meng, Zhong, Ji in equation 1
     [1, 2, 1],  # Coefficients for Meng, Zhong, Ji in equation 2
     [1, 1, 2]]  # Coefficients for Meng, Zhong, Ji in equation 3

# Constants
B = [158, 136, 114]

# Step 1: Eliminate Meng's coefficient from equations 2 and 3
# Multiply equation 1 by 1 and subtract from equations 2 and 3
A[1][0] = A[1][0] - A[0][0]  # Meng's coefficient in equation 2
A[1][1] = A[1][1] - A[0][1]  # Zhong's coefficient in equation 2
A[1][2] = A[1][2] - A[0][2]  # Ji's coefficient in equation 2
B[1] = B[1] - B[0]           # Constant in equation 2

A[2][0] = A[2][0] - A[0][0]  # Meng's coefficient in equation 3
A[2][1] = A[2][1] - A[0][1]  # Zhong's coefficient in equation 3
A[2][2] = A[2][2] - A[0][2]  # Ji's coefficient in equation 3
B[2] = B[2] - B[0]           # Constant in equation 3

# Step 2: Eliminate Zhong's coefficient from equation 3
# Multiply equation 2 by 1 and subtract from equation 3
A[2][1] = A[2][1] - A[1][1]  # Zhong's coefficient in equation 3
A[2][2] = A[2][2] - A[1][2]  # Ji's coefficient in equation 3
B[2] = B[2] - B[1]           # Constant in equation 3

# Step 3: Solve for Ji
c = Fraction(B[2], A[2][2])

# Step 4: Solve for Zhong
b = Fraction(B[1] - A[1][2] * c, A[1][1])

# Step 5: Solve for Meng
a = Fraction(B[0] - A[0][1] * b - A[0][2] * c, A[0][0])

# Final answer
a疋 = a
b疋 = b
c疋 = c
"""
Variable 'a' has wrong value. Expected: 56, Actual: 101
Variable 'b' has wrong value. Expected: 34, Actual: -22
Variable 'c' has wrong value. Expected: 12, Actual: -22"""
