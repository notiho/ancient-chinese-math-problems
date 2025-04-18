"""
今有麻九斗麥七斗菽三斗答二斗黍五斗直錢一百四十麻七斗麥六斗菽四斗答五斗黍三斗直錢一百二十八麻三斗麥五斗菽七斗答六斗黍四斗直錢一百一十六麻二斗麥五斗菽三斗答九斗黍四斗直錢一百一十二麻一斗麥三斗菽二斗答八斗黍五斗直錢九十五問一斗直幾何
術曰如方程以正負術入之
方程術曰置上禾三秉中禾二秉下禾一秉實三十九斗於右方中左禾列如右方以右行上禾遍乘中行而以直除又乘其次亦以直除然以中行中禾不盡者遍乘左行而以直除左方下禾不盡者上為法下為實實即下禾之實求中禾以法乘中行下實而除下禾之實餘如中禾秉數而一即中禾之實求上禾亦以法乘右行下實而除下禾中禾之實餘如上禾秉數而一即上禾之實實皆如法各得一斗荅曰麻 a斗 b錢 麥 c斗 d錢 菽 e斗 f錢 答 g斗 h錢 黍 i斗 j錢 
"""

"""
This problem is a complex system of linear equations involving multiple variables. The solution involves solving for the value of one unit (1 dou) of each type of grain (麻, 麥, 菽, 答, 黍) in terms of dou and qian. The procedure described corresponds to solving the system using a method similar to Gaussian elimination, known in ancient Chinese mathematics as the "fangcheng" method.

Here is the Python implementation of the solution:


"""


from fractions import Fraction

# Coefficients of the equations
# 麻, 麥, 菽, 答, 黍, 錢
equations = [
    [9, 7, 3, 2, 5, 140],  # 麻9斗, 麥7斗, 菽3斗, 答2斗, 黍5斗, 直錢140
    [7, 6, 4, 5, 3, 128],  # 麻7斗, 麥6斗, 菽4斗, 答5斗, 黍3斗, 直錢128
    [3, 5, 7, 6, 4, 116],  # 麻3斗, 麥5斗, 菽7斗, 答6斗, 黍4斗, 直錢116
    [2, 5, 3, 9, 4, 112],  # 麻2斗, 麥5斗, 菽3斗, 答9斗, 黍4斗, 直錢112
    [1, 3, 2, 8, 5, 95],   # 麻1斗, 麥3斗, 菽2斗, 答8斗, 黍5斗, 直錢95
]

# Number of variables
n = 5

# Convert the equations into fractions for precise calculations
for eq in equations:
    for i in range(len(eq)):
        eq[i] = Fraction(eq[i])

# Perform Gaussian elimination
for i in range(n):
    # Make the diagonal element 1
    factor = equations[i][i]
    for j in range(n + 1):
        equations[i][j] /= factor

    # Eliminate the current variable from other rows
    for k in range(n):
        if k != i:
            factor = equations[k][i]
            for j in range(n + 1):
                equations[k][j] -= factor * equations[i][j]

# Extract the solutions
麻 = equations[0][n]
麥 = equations[1][n]
菽 = equations[2][n]
答 = equations[3][n]
黍 = equations[4][n]

# Convert the solutions into dou and qian
def convert_to_dou_and_qian(value):
    dou = int(value)
    qian = (value - dou) * 10
    return dou, int(qian)

a, b = convert_to_dou_and_qian(麻)
c, d = convert_to_dou_and_qian(麥)
e, f = convert_to_dou_and_qian(菽)
g, h = convert_to_dou_and_qian(答)
i, j = convert_to_dou_and_qian(黍)

# Output the results
print(f"麻 {a}斗 {b}錢")
print(f"麥 {c}斗 {d}錢")
print(f"菽 {e}斗 {f}錢")
print(f"答 {g}斗 {h}錢")
print(f"黍 {i}斗 {j}錢")


"""


### Explanation:
1. **Input Representation**: Each equation represents the cost of a combination of grains in terms of dou and qian.
2. **Gaussian Elimination**: The `fangcheng` method is implemented as Gaussian elimination to solve the system of linear equations.
3. **Fraction Arithmetic**: The `Fraction` class ensures precise calculations without floating-point errors.
4. **Conversion to Dou and Qian**: The results are converted into dou (integer part) and qian (fractional part multiplied by 10).

### Output:
The program will output the value of 1 dou of each type of grain in terms of dou and qian.
"""


"""
Variable 'a' has wrong value. Expected: 1, Actual: 7
Variable 'b' has wrong value. Expected: 7, Actual: 0
Variable 'c' has wrong value. Expected: 1, Actual: 4
Variable 'd' has wrong value. Expected: 4, Actual: 0
Variable 'e' has wrong value. Expected: 1, Actual: 3
Variable 'f' has wrong value. Expected: 3, Actual: 0
Variable 'g' has wrong value. Expected: 1, Actual: 5
Variable 'h' has wrong value. Expected: 5, Actual: 0
Variable 'i' has wrong value. Expected: 1, Actual: 6
Variable 'j' has wrong value. Expected: 6, Actual: 0"""
