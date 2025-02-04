"""
今有孟仲季兄弟三人各持絹不知疋數大兄謂二弟曰我得汝等絹各半得滿七十九疋中弟曰我得兄弟絹各半得滿六十八疋小弟曰我得二兄絹各半得滿五十七疋問兄弟本持絹各幾何
術曰大兄二中弟一小弟一合一百五十八疋大兄一中弟二小弟一合一百三十六疋大兄一中弟一小二合一百一十四疋如方程而求即得
方程術曰置上禾三秉中禾二秉下禾一秉實三十九斗於右方中左禾列如右方以右行上禾遍乘中行而以直除又乘其次亦以直除然以中行中禾不盡者遍乘左行而以直除左方下禾不盡者上為法下為實實即下禾之實求中禾以法乘中行下實而除下禾之實餘如中禾秉數而一即中禾之實求上禾亦以法乘右行下實而除下禾中禾之實餘如上禾秉數而一即上禾之實實皆如法各得一斗
答曰孟 a疋 仲 b疋 季 c疋
"""

"""
This problem involves solving a system of linear equations to determine how many bolts of silk each of the three brothers (Meng, Zhong, and Ji) originally held.

### Problem Breakdown:
1. The eldest brother (Meng) says: "If I take half of each of your silk bolts, I will have 79 bolts."
2. The middle brother (Zhong) says: "If I take half of each of your silk bolts, I will have 68 bolts."
3. The youngest brother (Ji) says: "If I take half of each of your silk bolts, I will have 57 bolts."

We need to determine how many bolts of silk each brother originally had.

### Procedure:
The problem can be solved using the "fangcheng" (linear equations) method. The equations derived from the problem are:

1. \( M + \frac{1}{2}Z + \frac{1}{2}J = 79 \)
2. \( \frac{1}{2}M + Z + \frac{1}{2}J = 68 \)
3. \( \frac{1}{2}M + \frac{1}{2}Z + J = 57 \)

We will solve this system of equations step by step using the method described.

---


"""

#----- content starts here -----

from fractions import Fraction

# Define the coefficients and constants for the equations
# Equation 1: M + 1/2 Z + 1/2 J = 79
# Equation 2: 1/2 M + Z + 1/2 J = 68
# Equation 3: 1/2 M + 1/2 Z + J = 57

# Coefficients for Meng (M), Zhong (Z), and Ji (J)
coefficients = [
    [1, Fraction(1, 2), Fraction(1, 2)],  # Coefficients for Equation 1
    [Fraction(1, 2), 1, Fraction(1, 2)],  # Coefficients for Equation 2
    [Fraction(1, 2), Fraction(1, 2), 1]   # Coefficients for Equation 3
]

# Constants on the right-hand side of the equations
constants = [79, 68, 57]

# Step 1: Eliminate Meng (M) from the second and third equations
# Multiply the first equation by 1/2 and subtract from the second equation
coefficients[1] = [
    coefficients[1][i] - Fraction(1, 2) * coefficients[0][i] for i in range(3)
]
constants[1] -= Fraction(1, 2) * constants[0]

# Multiply the first equation by 1/2 and subtract from the third equation
coefficients[2] = [
    coefficients[2][i] - Fraction(1, 2) * coefficients[0][i] for i in range(3)
]
constants[2] -= Fraction(1, 2) * constants[0]

# Step 2: Eliminate Zhong (Z) from the third equation
# Multiply the second equation by 1/2 and subtract from the third equation
coefficients[2] = [
    coefficients[2][i] - Fraction(1, 2) * coefficients[1][i] for i in range(3)
]
constants[2] -= Fraction(1, 2) * constants[1]

# Step 3: Solve for Ji (J)
J = constants[2] / coefficients[2][2]

# Step 4: Solve for Zhong (Z)
Z = (constants[1] - coefficients[1][2] * J) / coefficients[1][1]

# Step 5: Solve for Meng (M)
M = (constants[0] - coefficients[0][1] * Z - coefficients[0][2] * J) / coefficients[0][0]

# Final results
a = M  # Meng's bolts of silk
b = Z  # Zhong's bolts of silk
c = J  # Ji's bolts of silk

# Output the results
a, b, c
#----- content ends here -----


"""


### Explanation of the Code:
1. **Step 1:** Eliminate \( M \) from the second and third equations by subtracting appropriate multiples of the first equation.
2. **Step 2:** Eliminate \( Z \) from the third equation by subtracting an appropriate multiple of the second equation.
3. **Step 3:** Solve for \( J \) from the simplified third equation.
4. **Step 4:** Back-substitute \( J \) into the second equation to solve for \( Z \).
5. **Step 5:** Back-substitute \( Z \) and \( J \) into the first equation to solve for \( M \).

### Answer:
The results will give:
- \( a \): Meng's bolts of silk.
- \( b \): Zhong's bolts of silk.
- \( c \): Ji's bolts of silk.
"""


"""
Variable 'a' has wrong value. Expected: 56, Actual: 874/15
Variable 'b' has wrong value. Expected: 34, Actual: 544/15
Variable 'c' has wrong value. Expected: 12, Actual: 26/5"""
