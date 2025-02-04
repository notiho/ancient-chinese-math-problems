"""
今有麻九斗麥七斗菽三斗答二斗黍五斗直錢一百四十麻七斗麥六斗菽四斗答五斗黍三斗直錢一百二十八麻三斗麥五斗菽七斗答六斗黍四斗直錢一百一十六麻二斗麥五斗菽三斗答九斗黍四斗直錢一百一十二麻一斗麥三斗菽二斗答八斗黍五斗直錢九十五問一斗直幾何
術曰如方程以正負術入之
方程術曰置上禾三秉中禾二秉下禾一秉實三十九斗於右方中左禾列如右方以右行上禾遍乘中行而以直除又乘其次亦以直除然以中行中禾不盡者遍乘左行而以直除左方下禾不盡者上為法下為實實即下禾之實求中禾以法乘中行下實而除下禾之實餘如中禾秉數而一即中禾之實求上禾亦以法乘右行下實而除下禾中禾之實餘如上禾秉數而一即上禾之實實皆如法各得一斗
荅曰麻一斗 a錢 麥一斗 b錢 菽一斗 c錢 答一斗 d錢 黍一斗 e錢 
"""

"""
This is a complex problem involving solving a system of linear equations. The problem essentially asks for the price of one dou of each type of grain (麻, 麥, 菽, 答, 黍). The solution requires encoding the ancient Chinese method of solving simultaneous equations, known as the "fangcheng" method.

Let's proceed step by step:

### Problem Setup
We are given the following equations based on the problem statement:

1. \( 9麻 + 7麥 + 3菽 + 2答 + 5黍 = 140 \)
2. \( 7麻 + 6麥 + 4菽 + 5答 + 3黍 = 128 \)
3. \( 3麻 + 5麥 + 7菽 + 6答 + 4黍 = 116 \)
4. \( 2麻 + 5麥 + 3菽 + 9答 + 4黍 = 112 \)
5. \( 1麻 + 3麥 + 2菽 + 8答 + 5黍 = 95 \)

We need to solve for \( 麻, 麥, 菽, 答, 黍 \), which represent the price of one dou of each grain.

---

### Fangcheng Method
The "fangcheng" method is an ancient Chinese algorithm for solving systems of linear equations. It involves systematically eliminating variables by multiplying rows and subtracting them, similar to Gaussian elimination.

---

### Implementation in Python


"""


from fractions import Fraction

# Coefficients of the equations
matrix = [
    [9, 7, 3, 2, 5, 140],  # Equation 1
    [7, 6, 4, 5, 3, 128],  # Equation 2
    [3, 5, 7, 6, 4, 116],  # Equation 3
    [2, 5, 3, 9, 4, 112],  # Equation 4
    [1, 3, 2, 8, 5, 95]    # Equation 5
]

# Step 1: Normalize the first row
for i in range(len(matrix[0]) - 1):
    matrix[0][i] = Fraction(matrix[0][i], matrix[0][0])
matrix[0][-1] = Fraction(matrix[0][-1], matrix[0][0])

# Step 2: Eliminate the first variable from all other rows
for i in range(1, len(matrix)):
    factor = matrix[i][0]
    for j in range(len(matrix[0])):
        matrix[i][j] -= factor * matrix[0][j]

# Step 3: Normalize the second row
for i in range(1, len(matrix[0]) - 1):
    matrix[1][i] = Fraction(matrix[1][i], matrix[1][1])
matrix[1][-1] = Fraction(matrix[1][-1], matrix[1][1])

# Step 4: Eliminate the second variable from all other rows
for i in range(len(matrix)):
    if i != 1:
        factor = matrix[i][1]
        for j in range(1, len(matrix[0])):
            matrix[i][j] -= factor * matrix[1][j]

# Step 5: Normalize the third row
for i in range(2, len(matrix[0]) - 1):
    matrix[2][i] = Fraction(matrix[2][i], matrix[2][2])
matrix[2][-1] = Fraction(matrix[2][-1], matrix[2][2])

# Step 6: Eliminate the third variable from all other rows
for i in range(len(matrix)):
    if i != 2:
        factor = matrix[i][2]
        for j in range(2, len(matrix[0])):
            matrix[i][j] -= factor * matrix[2][j]

# Step 7: Normalize the fourth row
for i in range(3, len(matrix[0]) - 1):
    matrix[3][i] = Fraction(matrix[3][i], matrix[3][3])
matrix[3][-1] = Fraction(matrix[3][-1], matrix[3][3])

# Step 8: Eliminate the fourth variable from all other rows
for i in range(len(matrix)):
    if i != 3:
        factor = matrix[i][3]
        for j in range(3, len(matrix[0])):
            matrix[i][j] -= factor * matrix[3][j]

# Step 9: Normalize the fifth row
for i in range(4, len(matrix[0]) - 1):
    matrix[4][i] = Fraction(matrix[4][i], matrix[4][4])
matrix[4][-1] = Fraction(matrix[4][-1], matrix[4][4])

# Step 10: Eliminate the fifth variable from all other rows
for i in range(len(matrix)):
    if i != 4:
        factor = matrix[i][4]
        for j in range(4, len(matrix[0])):
            matrix[i][j] -= factor * matrix[4][j]

# Extract the results
a = matrix[0][-1]  # 麻
b = matrix[1][-1]  # 麥
c = matrix[2][-1]  # 菽
d = matrix[3][-1]  # 答
e = matrix[4][-1]  # 黍

# Output the results
a, b, c, d, e


"""


---

### Explanation of the Code
1. **Matrix Representation**: Each equation is represented as a row in the matrix, with the last column being the constant term.
2. **Normalization**: Each row is normalized by dividing through by the coefficient of the leading variable.
3. **Elimination**: Variables are systematically eliminated from other rows by subtracting appropriate multiples of the normalized row.
4. **Back Substitution**: After all variables are eliminated, the solution is read directly from the last column of the matrix.

---

### Final Answer
The values of \( a, b, c, d, e \) represent the price of one dou of 麻, 麥, 菽, 答, and 黍 respectively.
"""


"""
Variable 'a' has wrong value. Expected: 7, Actual: 31397809912728649141
Variable 'b' has wrong value. Expected: 4, Actual: -4375002499293458921
Variable 'c' has wrong value. Expected: 3, Actual: -256410403765178263
Variable 'd' has wrong value. Expected: 5, Actual: -1780548826195710
Variable 'e' has wrong value. Expected: 6, Actual: -21745302069"""
