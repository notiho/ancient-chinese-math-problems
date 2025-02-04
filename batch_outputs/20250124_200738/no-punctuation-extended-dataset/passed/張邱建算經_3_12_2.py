"""
今有孟仲季兄弟三人各持絹不知疋數大兄謂二弟曰我得汝等絹各半得滿七十九疋中弟曰我得兄弟絹各半得滿六十八疋小弟曰我得二兄絹各半得滿五十七疋問兄弟本持絹各幾何
術曰大兄二中弟一小弟一合一百五十八疋大兄一中弟二小弟一合一百三十六疋大兄一中弟一小二合一百一十四疋如方程而求即得
方程術曰置上禾三秉中禾二秉下禾一秉實三十九斗於右方中左禾列如右方以右行上禾遍乘中行而以直除又乘其次亦以直除然以中行中禾不盡者遍乘左行而以直除左方下禾不盡者上為法下為實實即下禾之實求中禾以法乘中行下實而除下禾之實餘如中禾秉數而一即中禾之實求上禾亦以法乘右行下實而除下禾中禾之實餘如上禾秉數而一即上禾之實實皆如法各得一斗
答曰孟 a疋 仲 b疋 季 c疋
"""

#----- content starts here -----
"""
Suppose there are three brothers: Meng, Zhong, and Ji. Each holds an unknown number of bolts of silk.
The eldest brother (Meng) says to the other two: "If I take half of each of your silk bolts, I will have a total of 79 bolts."
The second brother (Zhong) says: "If I take half of each of your silk bolts, I will have a total of 68 bolts."
The youngest brother (Ji) says: "If I take half of each of your silk bolts, I will have a total of 57 bolts."
Question: How many bolts of silk does each brother originally hold?

The procedure says: 
- Meng's silk multiplied by 2, plus Zhong's silk multiplied by 1, plus Ji's silk multiplied by 1, equals 158 bolts.
- Meng's silk multiplied by 1, plus Zhong's silk multiplied by 2, plus Ji's silk multiplied by 1, equals 136 bolts.
- Meng's silk multiplied by 1, plus Zhong's silk multiplied by 1, plus Ji's silk multiplied by 2, equals 114 bolts.
Solve this system of equations using the method of simultaneous equations.

Answer: Meng has *a* bolts, Zhong has *b* bolts, Ji has *c* bolts.
"""

# Define the coefficients and constants for the system of equations
# Equation 1: 2孟 + 1仲 + 1季 = 158
# Equation 2: 1孟 + 2仲 + 1季 = 136
# Equation 3: 1孟 + 1仲 + 2季 = 114

# Coefficients
A = [[2, 1, 1],  # Coefficients for equation 1
     [1, 2, 1],  # Coefficients for equation 2
     [1, 1, 2]]  # Coefficients for equation 3

# Constants
B = [158, 136, 114]

# Solve using substitution/elimination (manual implementation of Gaussian elimination)

# Step 1: Normalize the first row
factor = A[0][0]
A[0] = [x / factor for x in A[0]]
B[0] = B[0] / factor

# Step 2: Eliminate the first variable from the second and third rows
factor = A[1][0]
A[1] = [A[1][i] - factor * A[0][i] for i in range(3)]
B[1] = B[1] - factor * B[0]

factor = A[2][0]
A[2] = [A[2][i] - factor * A[0][i] for i in range(3)]
B[2] = B[2] - factor * B[0]

# Step 3: Normalize the second row
factor = A[1][1]
A[1] = [x / factor for x in A[1]]
B[1] = B[1] / factor

# Step 4: Eliminate the second variable from the third row
factor = A[2][1]
A[2] = [A[2][i] - factor * A[1][i] for i in range(3)]
B[2] = B[2] - factor * B[1]

# Step 5: Solve for the third variable
c = B[2] / A[2][2]

# Step 6: Back-substitute to solve for the second variable
b = B[1] - A[1][2] * c

# Step 7: Back-substitute to solve for the first variable
a = B[0] - A[0][1] * b - A[0][2] * c

# Final answer
a = Fraction(a)
b = Fraction(b)
c = Fraction(c)#----- content ends here -----

"""
"""
