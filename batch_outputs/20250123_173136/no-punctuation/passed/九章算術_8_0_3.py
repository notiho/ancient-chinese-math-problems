"""
今有上禾三秉中禾二秉下禾一秉實三十九斗上禾二秉中禾三秉下禾一秉實三十四斗上禾一秉中禾二秉下禾三秉實二十六斗問上中下禾實一秉各幾何
方程術曰置上禾三秉中禾二秉下禾一秉實三十九斗於右方中左禾列如右方以右行上禾遍乘中行而以直除又乘其次亦以直除然以中行中禾不盡者遍乘左行而以直除左方下禾不盡者上為法下為實實即下禾之實求中禾以法乘中行下實而除下禾之實餘如中禾秉數而一即中禾之實求上禾亦以法乘右行下實而除下禾中禾之實餘如上禾秉數而一即上禾之實實皆如法各得一斗
荅曰上禾一秉 a斗 中禾一秉 b斗 下禾一秉 c斗 
"""

"""
Suppose there are three bundles of upper-grade grain, two bundles of middle-grade grain, and one bundle of lower-grade grain, with a total of 39 dou.
There are two bundles of upper-grade grain, three bundles of middle-grade grain, and one bundle of lower-grade grain, with a total of 34 dou.
There is one bundle of upper-grade grain, two bundles of middle-grade grain, and three bundles of lower-grade grain, with a total of 26 dou.
Question: how much does one bundle of upper-grade, middle-grade, and lower-grade grain yield respectively?

The procedure for solving systems of equations says:
1. Place the first equation: 3 bundles of upper-grade grain, 2 bundles of middle-grade grain, 1 bundle of lower-grade grain, totaling 39 dou, on the right side.
2. Arrange the second equation: 2 bundles of upper-grade grain, 3 bundles of middle-grade grain, 1 bundle of lower-grade grain, totaling 34 dou, below the first.
3. Arrange the third equation: 1 bundle of upper-grade grain, 2 bundles of middle-grade grain, 3 bundles of lower-grade grain, totaling 26 dou, below the second.
4. Use elimination to solve for the unknowns:
   - Multiply rows and subtract to eliminate variables systematically.
   - Solve for the remaining variables using substitution and back-substitution.

Answer: one bundle of upper-grade grain yields *a* dou, one bundle of middle-grade grain yields *b* dou, and one bundle of lower-grade grain yields *c* dou.
"""

# Initial equations:
# 3上 + 2中 + 1下 = 39
# 2上 + 3中 + 1下 = 34
# 1上 + 2中 + 3下 = 26

# Step 1: Represent the coefficients and constants
coefficients = [
    [3, 2, 1],  # Coefficients for the first equation
    [2, 3, 1],  # Coefficients for the second equation
    [1, 2, 3],  # Coefficients for the third equation
]
constants = [39, 34, 26]  # Constants on the right-hand side

# Step 2: Elimination to solve for variables
# Eliminate the first variable (上禾) from the second and third equations
factor1 = Fraction(coefficients[1][0], coefficients[0][0])
factor2 = Fraction(coefficients[2][0], coefficients[0][0])

for i in range(3):
    coefficients[1][i] -= factor1 * coefficients[0][i]
    coefficients[2][i] -= factor2 * coefficients[0][i]

constants[1] -= factor1 * constants[0]
constants[2] -= factor2 * constants[0]

# Eliminate the second variable (中禾) from the third equation
factor3 = Fraction(coefficients[2][1], coefficients[1][1])

for i in range(3):
    coefficients[2][i] -= factor3 * coefficients[1][i]

constants[2] -= factor3 * constants[1]

# Step 3: Back-substitution to solve for variables
# Solve for 下禾
c = Fraction(constants[2], coefficients[2][2])

# Solve for 中禾
b = Fraction(constants[1] - coefficients[1][2] * c, coefficients[1][1])

# Solve for 上禾
a = Fraction(constants[0] - coefficients[0][1] * b - coefficients[0][2] * c, coefficients[0][0])

# Final results
a, b, c  # a is for 上禾, b is for 中禾, c is for 下禾
"""
"""
