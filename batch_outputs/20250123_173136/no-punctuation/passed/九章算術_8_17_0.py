"""
今有麻九斗麥七斗菽三斗答二斗黍五斗直錢一百四十麻七斗麥六斗菽四斗答五斗黍三斗直錢一百二十八麻三斗麥五斗菽七斗答六斗黍四斗直錢一百一十六麻二斗麥五斗菽三斗答九斗黍四斗直錢一百一十二麻一斗麥三斗菽二斗答八斗黍五斗直錢九十五問一斗直幾何
術曰如方程以正負術入之
方程術曰置上禾三秉中禾二秉下禾一秉實三十九斗於右方中左禾列如右方以右行上禾遍乘中行而以直除又乘其次亦以直除然以中行中禾不盡者遍乘左行而以直除左方下禾不盡者上為法下為實實即下禾之實求中禾以法乘中行下實而除下禾之實餘如中禾秉數而一即中禾之實求上禾亦以法乘右行下實而除下禾中禾之實餘如上禾秉數而一即上禾之實實皆如法各得一斗
荅曰麻一斗 a錢 麥一斗 b錢 菽一斗 c錢 答一斗 d錢 黍一斗 e錢 
"""

"""
This problem involves solving a system of linear equations to determine the price per dou (斗) of each type of grain. The procedure described corresponds to solving the equations using a method similar to Gaussian elimination. Below is the Python implementation of the procedure:


"""


from fractions import Fraction

# Coefficients of the equations
# 麻 (ma), 麥 (mai), 菽 (shu), 答 (da), 黍 (shu2), and the total price
equations = [
    [9, 7, 3, 2, 5, 140],  # 麻9斗, 麥7斗, 菽3斗, 答2斗, 黍5斗, 直錢140
    [7, 6, 4, 5, 3, 128],  # 麻7斗, 麥6斗, 菽4斗, 答5斗, 黍3斗, 直錢128
    [3, 5, 7, 6, 4, 116],  # 麻3斗, 麥5斗, 菽7斗, 答6斗, 黍4斗, 直錢116
    [2, 5, 3, 9, 4, 112],  # 麻2斗, 麥5斗, 菽3斗, 答9斗, 黍4斗, 直錢112
    [1, 3, 2, 8, 5, 95]    # 麻1斗, 麥3斗, 菽2斗, 答8斗, 黍5斗, 直錢95
]

# Number of variables
n = len(equations)

# Convert all coefficients to fractions for exact arithmetic
for i in range(n):
    equations[i] = [Fraction(x) for x in equations[i]]

# Gaussian elimination
for i in range(n):
    # Make the diagonal element 1 by dividing the entire row
    diag = equations[i][i]
    for j in range(n + 1):
        equations[i][j] /= diag

    # Eliminate the current variable from all other rows
    for k in range(n):
        if k != i:
            factor = equations[k][i]
            for j in range(n + 1):
                equations[k][j] -= factor * equations[i][j]

# Extract the solutions
a = equations[0][-1]  # 麻一斗
b = equations[1][-1]  # 麥一斗
c = equations[2][-1]  # 菽一斗
d = equations[3][-1]  # 答一斗
e = equations[4][-1]  # 黍一斗

# Output the results
a, b, c, d, e


"""


### Explanation of the Code:
1. **Input the equations**: Each equation represents the relationship between the quantities of 麻 (ma), 麥 (mai), 菽 (shu), 答 (da), 黍 (shu2), and their total price.
2. **Convert to fractions**: All coefficients are converted to fractions to ensure exact arithmetic.
3. **Gaussian elimination**:
   - Normalize each row by dividing by the diagonal element.
   - Eliminate the current variable from all other rows.
4. **Extract solutions**: After elimination, the last column of each row contains the solution for the corresponding variable.
5. **Output the results**: The prices per dou for 麻, 麥, 菽, 答, and 黍 are stored in `a`, `b`, `c`, `d`, and `e`, respectively.

### Answer:
The prices per dou are:
- 麻 (ma): `a` 錢
- 麥 (mai): `b` 錢
- 菽 (shu): `c` 錢
- 答 (da): `d` 錢
- 黍 (shu2): `e` 錢
"""


"""
"""
