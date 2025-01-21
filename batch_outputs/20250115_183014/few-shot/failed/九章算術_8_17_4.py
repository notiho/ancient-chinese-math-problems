"""
今有麻九斗、麥七斗、菽三斗、答二斗、黍五斗，直錢一百四十；麻七斗、麥六斗、菽四斗、答五斗、黍三斗，直錢一百二十八；麻三斗、麥五斗、菽七斗、答六斗、黍四斗，直錢一百一十六；麻二斗、麥五斗、菽三斗、答九斗、黍四斗，直錢一百一十二；麻一斗、麥三斗、菽二斗、答八斗、黍五斗，直錢九十五。問︰一斗直幾何？
術曰：如方程，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：麻 a斗 b錢 ，麥 c斗 d錢 ，菽 e斗 f錢 ，答 g斗 h錢 ，黍 i斗 j錢 。
"""

"""
The problem presented is a system of linear equations, which can be solved using the method described in ancient Chinese mathematics, specifically the "正負術" (positive and negative method) and "方程術" (method of simultaneous equations). Below is the Python implementation of the solution:


"""


from fractions import Fraction

# Coefficients of the equations
# 麻 (ma), 麥 (mai), 菽 (shu), 答 (da), 黍 (shu), and the total value in qian
equations = [
    [9, 7, 3, 2, 5, 140],
    [7, 6, 4, 5, 3, 128],
    [3, 5, 7, 6, 4, 116],
    [2, 5, 3, 9, 4, 112],
    [1, 3, 2, 8, 5, 95]
]

# Step 1: Convert the equations into a matrix form
matrix = [row[:-1] for row in equations]  # Coefficients of 麻, 麥, 菽, 答, 黍
values = [row[-1] for row in equations]  # Total values in qian

# Step 2: Perform Gaussian elimination to solve the system of equations
def gaussian_elimination(matrix, values):
    n = len(matrix)
    # Forward elimination
    for i in range(n):
        # Make the diagonal element 1
        diag = matrix[i][i]
        for j in range(i, n):
            matrix[i][j] = Fraction(matrix[i][j], diag)
        values[i] = Fraction(values[i], diag)
        
        # Eliminate the below rows
        for k in range(i + 1, n):
            factor = matrix[k][i]
            for j in range(i, n):
                matrix[k][j] -= factor * matrix[i][j]
            values[k] -= factor * values[i]
    
    # Back substitution
    solution = [0] * n
    for i in range(n - 1, -1, -1):
        solution[i] = values[i]
        for j in range(i + 1, n):
            solution[i] -= matrix[i][j] * solution[j]
    return solution

# Solve the system of equations
solution = gaussian_elimination(matrix, values)

# Extract the results
麻 = solution[0]
麥 = solution[1]
菽 = solution[2]
答 = solution[3]
黍 = solution[4]

# Convert the results to dou and qian
def convert_to_dou_and_qian(value):
    dou = int(value)
    qian = (value - dou) * 10
    return dou, qian

a, b = convert_to_dou_and_qian(麻)
c, d = convert_to_dou_and_qian(麥)
e, f = convert_to_dou_and_qian(菽)
g, h = convert_to_dou_and_qian(答)
i, j = convert_to_dou_and_qian(黍)

# Final answer
print(f"麻 {a}斗 {b}錢 ，麥 {c}斗 {d}錢 ，菽 {e}斗 {f}錢 ，答 {g}斗 {h}錢 ，黍 {i}斗 {j}錢 。")


"""


### Explanation of the Code:
1. **Input Data**: The coefficients of 麻, 麥, 菽, 答, 黍, and the total value in qian are stored in the `equations` list.
2. **Gaussian Elimination**: The `gaussian_elimination` function performs forward elimination to make the matrix upper triangular and then performs back substitution to find the solution.
3. **Fraction Handling**: The `Fraction` class is used to ensure exact arithmetic throughout the calculations.
4. **Conversion to Dou and Qian**: The results are converted into dou (integer part) and qian (fractional part multiplied by 10) for the final answer.

### Final Answer Format:
The solution will output the value of each type of grain (麻, 麥, 菽, 答, 黍) in terms of dou and qian.
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
