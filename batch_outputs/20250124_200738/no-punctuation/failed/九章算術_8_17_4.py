"""
今有麻九斗麥七斗菽三斗答二斗黍五斗直錢一百四十麻七斗麥六斗菽四斗答五斗黍三斗直錢一百二十八麻三斗麥五斗菽七斗答六斗黍四斗直錢一百一十六麻二斗麥五斗菽三斗答九斗黍四斗直錢一百一十二麻一斗麥三斗菽二斗答八斗黍五斗直錢九十五問一斗直幾何
術曰如方程以正負術入之
方程術曰置上禾三秉中禾二秉下禾一秉實三十九斗於右方中左禾列如右方以右行上禾遍乘中行而以直除又乘其次亦以直除然以中行中禾不盡者遍乘左行而以直除左方下禾不盡者上為法下為實實即下禾之實求中禾以法乘中行下實而除下禾之實餘如中禾秉數而一即中禾之實求上禾亦以法乘右行下實而除下禾中禾之實餘如上禾秉數而一即上禾之實實皆如法各得一斗
荅曰麻一斗 a錢 麥一斗 b錢 菽一斗 c錢 答一斗 d錢 黍一斗 e錢 
"""

"""
This is a complex system of linear equations problem based on ancient Chinese mathematics. The problem involves determining the price per dou (斗) for each type of grain: 麻 (hemp), 麥 (wheat), 菽 (beans), 答 (rice), and 黍 (millet). The solution will follow the "方程術" (method of solving simultaneous equations) as described.

The equations are derived from the problem statement:

1. \( 9麻 + 7麥 + 3菽 + 2答 + 5黍 = 140錢 \)
2. \( 7麻 + 6麥 + 4菽 + 5答 + 3黍 = 128錢 \)
3. \( 3麻 + 5麥 + 7菽 + 6答 + 4黍 = 116錢 \)
4. \( 2麻 + 5麥 + 3菽 + 9答 + 4黍 = 112錢 \)
5. \( 1麻 + 3麥 + 2菽 + 8答 + 5黍 = 95錢 \)

We will solve this system step by step using the described procedure.


"""

#----- content starts here -----

from fractions import Fraction

# Coefficients of the equations
# 麻, 麥, 菽, 答, 黍
equations = [
    [9, 7, 3, 2, 5, 140],
    [7, 6, 4, 5, 3, 128],
    [3, 5, 7, 6, 4, 116],
    [2, 5, 3, 9, 4, 112],
    [1, 3, 2, 8, 5, 95]
]

# Step 1: Normalize the first equation (divide by the coefficient of 麻 in the first equation)
for i in range(6):
    equations[0][i] = Fraction(equations[0][i], 9)

# Step 2: Eliminate 麻 from the other equations
for i in range(1, 5):
    factor = equations[i][0]
    for j in range(6):
        equations[i][j] -= factor * equations[0][j]

# Step 3: Normalize the second equation (divide by the coefficient of 麥 in the second equation)
for i in range(1, 6):
    equations[1][i] = Fraction(equations[1][i], equations[1][1])

# Step 4: Eliminate 麥 from the other equations
for i in [0, 2, 3, 4]:
    factor = equations[i][1]
    for j in range(1, 6):
        equations[i][j] -= factor * equations[1][j]

# Step 5: Normalize the third equation (divide by the coefficient of 菽 in the third equation)
for i in range(2, 6):
    equations[2][i] = Fraction(equations[2][i], equations[2][2])

# Step 6: Eliminate 菽 from the other equations
for i in [0, 1, 3, 4]:
    factor = equations[i][2]
    for j in range(2, 6):
        equations[i][j] -= factor * equations[2][j]

# Step 7: Normalize the fourth equation (divide by the coefficient of 答 in the fourth equation)
for i in range(3, 6):
    equations[3][i] = Fraction(equations[3][i], equations[3][3])

# Step 8: Eliminate 答 from the other equations
for i in [0, 1, 2, 4]:
    factor = equations[i][3]
    for j in range(3, 6):
        equations[i][j] -= factor * equations[3][j]

# Step 9: Normalize the fifth equation (divide by the coefficient of 黍 in the fifth equation)
for i in range(4, 6):
    equations[4][i] = Fraction(equations[4][i], equations[4][4])

# Step 10: Back-substitute to solve for each variable
e = equations[4][5]
d = equations[3][5] - equations[3][4] * e
c = equations[2][5] - equations[2][4] * e - equations[2][3] * d
b = equations[1][5] - equations[1][4] * e - equations[1][3] * d - equations[1][2] * c
a = equations[0][5] - equations[0][4] * e - equations[0][3] * d - equations[0][2] * c - equations[0][1] * b

# Results
a = float(a)
b = float(b)
c = float(c)
d = float(d)
e = float(e)

print(f"麻一斗 {a}錢")
print(f"麥一斗 {b}錢")
print(f"菽一斗 {c}錢")
print(f"答一斗 {d}錢")
print(f"黍一斗 {e}錢")
#----- content ends here -----


"""
 

This Python code follows the described ancient Chinese method of solving simultaneous equations step by step. The final result will give the price per dou for 麻, 麥, 菽, 答, and 黍.
"""


"""
Variable 'a' has wrong value. Expected: 7, Actual: -94753.08204105467
Variable 'b' has wrong value. Expected: 4, Actual: 151256.21053750566
Variable 'c' has wrong value. Expected: 3, Actual: -59923.12792373432
Variable 'd' has wrong value. Expected: 5, Actual: -14738.512823873907
Variable 'e' has wrong value. Expected: 6, Actual: 674.1348051806315"""
