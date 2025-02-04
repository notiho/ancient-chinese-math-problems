"""
今有五羊四犬三雞二兔直錢一千四百九十六四羊二犬六雞三兔直錢一千一百七十五三羊一犬七雞五兔直錢九百五十八二羊三犬五雞一兔直錢八百六十一問羊犬雞兔價各幾何
術曰如方程以正負術入之
方程術曰置上禾三秉中禾二秉下禾一秉實三十九斗於右方中左禾列如右方以右行上禾遍乘中行而以直除又乘其次亦以直除然以中行中禾不盡者遍乘左行而以直除左方下禾不盡者上為法下為實實即下禾之實求中禾以法乘中行下實而除下禾之實餘如中禾秉數而一即中禾之實求上禾亦以法乘右行下實而除下禾中禾之實餘如上禾秉數而一即上禾之實實皆如法各得一斗
荅曰羊價 a 犬價 b 雞價 c 兔價 d 
"""

"""
This problem involves solving a system of linear equations to determine the prices of sheep, dogs, chickens, and rabbits. The ancient Chinese method described here corresponds to a systematic elimination process similar to Gaussian elimination. Below is the Python implementation of the procedure:


"""

#----- content starts here -----

from fractions import Fraction

# Define the coefficients of the equations
# 5羊 + 4犬 + 3雞 + 2兔 = 1496
# 4羊 + 2犬 + 6雞 + 3兔 = 1175
# 3羊 + 1犬 + 7雞 + 5兔 = 958
# 2羊 + 3犬 + 5雞 + 1兔 = 861

coefficients = [
    [5, 4, 3, 2, 1496],
    [4, 2, 6, 3, 1175],
    [3, 1, 7, 5, 958],
    [2, 3, 5, 1, 861]
]

# Perform Gaussian elimination
# Step 1: Normalize the first row
for i in range(1, 4):
    factor = Fraction(coefficients[i][0], coefficients[0][0])
    for j in range(5):
        coefficients[i][j] -= factor * coefficients[0][j]

# Step 2: Normalize the second row
for i in range(2, 4):
    factor = Fraction(coefficients[i][1], coefficients[1][1])
    for j in range(1, 5):
        coefficients[i][j] -= factor * coefficients[1][j]

# Step 3: Normalize the third row
factor = Fraction(coefficients[3][2], coefficients[2][2])
for j in range(2, 5):
    coefficients[3][j] -= factor * coefficients[2][j]

# Back substitution to find the values
d = Fraction(coefficients[3][4], coefficients[3][3])
c = Fraction(coefficients[2][4] - coefficients[2][3] * d, coefficients[2][2])
b = Fraction(coefficients[1][4] - coefficients[1][2] * c - coefficients[1][3] * d, coefficients[1][1])
a = Fraction(coefficients[0][4] - coefficients[0][1] * b - coefficients[0][2] * c - coefficients[0][3] * d, coefficients[0][0])

# The results
a, b, c, d
#----- content ends here -----


"""


### Explanation of the Code:
1. **Input the equations**: The coefficients of the equations are stored in a 2D list, where each row represents an equation, and the last column represents the constant term on the right-hand side.

2. **Gaussian elimination**:
   - Normalize each row by eliminating the coefficients of the variables step by step.
   - Subtract multiples of the rows to make the coefficients below the pivot (diagonal element) zero.

3. **Back substitution**:
   - Solve for the variables starting from the last row and substituting back into the previous rows.

4. **Output**:
   - The values of `a`, `b`, `c`, and `d` represent the prices of sheep, dogs, chickens, and rabbits, respectively.

This implementation follows the ancient Chinese procedure of systematically eliminating variables to solve the system of equations.
"""


"""
"""
