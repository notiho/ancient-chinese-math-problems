"""
今有麻九斗麥七斗菽三斗答二斗黍五斗直錢一百四十麻七斗麥六斗菽四斗答五斗黍三斗直錢一百二十八麻三斗麥五斗菽七斗答六斗黍四斗直錢一百一十六麻二斗麥五斗菽三斗答九斗黍四斗直錢一百一十二麻一斗麥三斗菽二斗答八斗黍五斗直錢九十五問一斗直幾何
術曰如方程以正負術入之
方程術曰置上禾三秉中禾二秉下禾一秉實三十九斗於右方中左禾列如右方以右行上禾遍乘中行而以直除又乘其次亦以直除然以中行中禾不盡者遍乘左行而以直除左方下禾不盡者上為法下為實實即下禾之實求中禾以法乘中行下實而除下禾之實餘如中禾秉數而一即中禾之實求上禾亦以法乘右行下實而除下禾中禾之實餘如上禾秉數而一即上禾之實實皆如法各得一斗荅曰麻 a斗 b錢 麥 c斗 d錢 菽 e斗 f錢 答 g斗 h錢 黍 i斗 j錢 
"""

"""
This problem involves solving a system of linear equations using ancient Chinese mathematical methods, specifically the "fangcheng" (方程) method. However, due to the complexity of the problem and the limitations of this medium, I will provide a simplified Python implementation of the solution using fractions to ensure precision.

The problem involves determining the price per dou (斗) of 麻 (hemp), 麥 (wheat), 菽 (beans), 答 (response), and 黍 (millet) based on the given data.


"""


from fractions import Fraction

# Coefficients of the equations
# Each row represents [麻, 麥, 菽, 答, 黍, total price]
equations = [
    [9, 7, 3, 2, 5, 140],
    [7, 6, 4, 5, 3, 128],
    [3, 5, 7, 6, 4, 116],
    [2, 5, 3, 9, 4, 112],
    [1, 3, 2, 8, 5, 95]
]

# Initialize variables for 麻, 麥, 菽, 答, 黍
麻, 麥, 菽, 答, 黍 = 0, 0, 0, 0, 0

# Solve the system of equations using substitution or elimination
# Step 1: Convert the equations into a matrix form and perform Gaussian elimination
def gaussian_elimination(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    for i in range(rows):
        # Make the diagonal element 1
        diag_element = matrix[i][i]
        for j in range(cols):
            matrix[i][j] = Fraction(matrix[i][j], diag_element)

        # Eliminate the current column in all other rows
        for k in range(rows):
            if k != i:
                factor = matrix[k][i]
                for j in range(cols):
                    matrix[k][j] -= factor * matrix[i][j]

    return matrix

# Perform Gaussian elimination
result = gaussian_elimination(equations)

# Extract the solutions
麻 = result[0][-1]
麥 = result[1][-1]
菽 = result[2][-1]
答 = result[3][-1]
黍 = result[4][-1]

# Convert the results to dou and qian (1 dou = 10 qian)
def convert_to_dou_and_qian(value):
    dou = value // 1
    qian = (value - dou) * 10
    return dou, qian

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


This implementation uses Gaussian elimination to solve the system of linear equations. The results are then converted into dou (斗) and qian (錢) for each commodity. Note that this is a simplified approach and does not strictly follow the ancient Chinese "fangcheng" method, but it achieves the same result.
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
