"""
今有甲乙丙三人持錢不知多少甲言我得乙大半得丙少半可滿一百乙言我得甲大半得丙半可滿一百丙言我得甲乙各大半可滿一百問甲乙丙持錢各幾何
術曰三甲二乙一丙錢三百四甲六乙三丙錢六百二甲二乙三丙錢三百如方程即得
方程術曰置上禾三秉中禾二秉下禾一秉實三十九斗於右方中左禾列如右方以右行上禾遍乘中行而以直除又乘其次亦以直除然以中行中禾不盡者遍乘左行而以直除左方下禾不盡者上為法下為實實即下禾之實求中禾以法乘中行下實而除下禾之實餘如中禾秉數而一即中禾之實求上禾亦以法乘右行下實而除下禾中禾之實餘如上禾秉數而一即上禾之實實皆如法各得一斗答曰甲 a 乙 b 丙 c
"""

"""
Suppose there are three people, Jia, Yi, and Bing, holding an unknown amount of money.
Jia says: If I take more than half of Yi's money and less than half of Bing's money, I can reach 100.
Yi says: If I take more than half of Jia's money and half of Bing's money, I can reach 100.
Bing says: If I take more than half of Jia's money and more than half of Yi's money, I can reach 100.
Question: How much money does each of Jia, Yi, and Bing hold?

The procedure says: 
1. Represent the relationships as equations:
   - 3 Jia + 2 Yi + 1 Bing = 300
   - 4 Jia + 6 Yi + 3 Bing = 600
   - 2 Jia + 2 Yi + 3 Bing = 300
2. Solve the equations using the method of elimination (方程術).

The elimination method says:
- Place the coefficients of the unknowns (禾) in rows, with the results (實) on the right-hand side.
- Use the top row to eliminate the coefficients in the rows below by multiplying and subtracting.
- Continue until the coefficients of one unknown remain in the bottom row.
- Solve for the unknown in the bottom row, then back-substitute to solve for the others.

Answer: Jia holds *a*, Yi holds *b*, and Bing holds *c*.
"""

from fractions import Fraction

# Coefficients of the equations
# 3 Jia + 2 Yi + 1 Bing = 300
# 4 Jia + 6 Yi + 3 Bing = 600
# 2 Jia + 2 Yi + 3 Bing = 300

# Initialize the augmented matrix
matrix = [
    [3, 2, 1, 300],
    [4, 6, 3, 600],
    [2, 2, 3, 300]
]

# Step 1: Eliminate the first variable (Jia) from the second and third rows
factor1 = Fraction(matrix[1][0], matrix[0][0])
matrix[1] = [matrix[1][i] - factor1 * matrix[0][i] for i in range(4)]

factor2 = Fraction(matrix[2][0], matrix[0][0])
matrix[2] = [matrix[2][i] - factor2 * matrix[0][i] for i in range(4)]

# Step 2: Eliminate the second variable (Yi) from the third row
factor3 = Fraction(matrix[2][1], matrix[1][1])
matrix[2] = [matrix[2][i] - factor3 * matrix[1][i] for i in range(4)]

# Step 3: Solve for Bing (c) in the third row
c = Fraction(matrix[2][3], matrix[2][2])

# Step 4: Back-substitute to solve for Yi (b) in the second row
b = Fraction(matrix[1][3] - matrix[1][2] * c, matrix[1][1])

# Step 5: Back-substitute to solve for Jia (a) in the first row
a = Fraction(matrix[0][3] - matrix[0][1] * b - matrix[0][2] * c, matrix[0][0])

# Final answer
a, b, c
"""
"""
