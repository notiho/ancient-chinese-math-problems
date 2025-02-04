"""
今有麻九斗麥七斗菽三斗答二斗黍五斗直錢一百四十麻七斗麥六斗菽四斗答五斗黍三斗直錢一百二十八麻三斗麥五斗菽七斗答六斗黍四斗直錢一百一十六麻二斗麥五斗菽三斗答九斗黍四斗直錢一百一十二麻一斗麥三斗菽二斗答八斗黍五斗直錢九十五問一斗直幾何
術曰如方程以正負術入之
方程術曰置上禾三秉中禾二秉下禾一秉實三十九斗於右方中左禾列如右方以右行上禾遍乘中行而以直除又乘其次亦以直除然以中行中禾不盡者遍乘左行而以直除左方下禾不盡者上為法下為實實即下禾之實求中禾以法乘中行下實而除下禾之實餘如中禾秉數而一即中禾之實求上禾亦以法乘右行下實而除下禾中禾之實餘如上禾秉數而一即上禾之實實皆如法各得一斗
荅曰麻一斗 a錢 麥一斗 b錢 菽一斗 c錢 答一斗 d錢 黍一斗 e錢 
"""

"""
This is a complex problem involving a system of linear equations, solved using the ancient Chinese method of elimination, known as "fangcheng" (方程). The problem involves determining the price of one dou (斗) of each type of grain: 麻 (hemp), 麥 (wheat), 菽 (beans), 答 (millet), and 黍 (glutinous millet). Below is the Python implementation of the procedure described.


"""


from fractions import Fraction

# Coefficients of the equations
# 麻, 麥, 菽, 答, 黍, and the total price in 錢
equations = [
    [9, 7, 3, 2, 5, 140],  # First equation
    [7, 6, 4, 5, 3, 128],  # Second equation
    [3, 5, 7, 6, 4, 116],  # Third equation
    [2, 5, 3, 9, 4, 112],  # Fourth equation
    [1, 3, 2, 8, 5, 95],   # Fifth equation
]

# Step 1: Normalize the first equation (divide by the coefficient of 麻 in the first equation)
for i in range(1, len(equations)):
    factor = Fraction(equations[i][0], equations[0][0])
    for j in range(len(equations[0])):
        equations[i][j] -= factor * equations[0][j]

# Step 2: Normalize the second equation (divide by the coefficient of 麥 in the second equation)
for i in range(2, len(equations)):
    factor = Fraction(equations[i][1], equations[1][1])
    for j in range(1, len(equations[0])):
        equations[i][j] -= factor * equations[1][j]

# Step 3: Normalize the third equation (divide by the coefficient of 菽 in the third equation)
for i in range(3, len(equations)):
    factor = Fraction(equations[i][2], equations[2][2])
    for j in range(2, len(equations[0])):
        equations[i][j] -= factor * equations[2][j]

# Step 4: Normalize the fourth equation (divide by the coefficient of 答 in the fourth equation)
factor = Fraction(equations[4][3], equations[3][3])
for j in range(3, len(equations[0])):
    equations[4][j] -= factor * equations[3][j]

# Step 5: Back-substitute to solve for each variable
e = Fraction(equations[4][5], equations[4][4])  # 黍
d = Fraction(equations[3][5] - equations[3][4] * e, equations[3][3])  # 答
c = Fraction(equations[2][5] - equations[2][4] * e - equations[2][3] * d, equations[2][2])  # 菽
b = Fraction(equations[1][5] - equations[1][4] * e - equations[1][3] * d - equations[1][2] * c, equations[1][1])  # 麥
a = Fraction(equations[0][5] - equations[0][4] * e - equations[0][3] * d - equations[0][2] * c - equations[0][1] * b, equations[0][0])  # 麻

# Output the results
print(f"麻一斗 {a}錢")
print(f"麥一斗 {b}錢")
print(f"菽一斗 {c}錢")
print(f"答一斗 {d}錢")
print(f"黍一斗 {e}錢")


"""


### Explanation of the Code:
1. **Input Equations**: The coefficients of the equations are input as a list of lists, where each sublist represents an equation.
2. **Normalization and Elimination**: The equations are normalized and reduced step by step, following the "fangcheng" method. Each step eliminates one variable by subtracting a multiple of a previous equation.
3. **Back-Substitution**: Once the system is reduced to a triangular form, the variables are solved starting from the last equation and substituting back into the previous ones.
4. **Output**: The prices of one dou of 麻, 麥, 菽, 答, and 黍 are printed as fractions.

### Answer:
The output will provide the values of `a`, `b`, `c`, `d`, and `e` as the prices of one dou of 麻, 麥, 菽, 答, and 黍, respectively, in 錢.
"""


"""
"""
