"""
今有上禾三秉，中禾二秉，下禾一秉，實三十九斗；上禾二秉，中禾三秉，下禾一秉，實三十四斗；上禾一秉，中禾二秉，下禾三秉，實二十六斗。問︰上、中、下禾實一秉各幾何？
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：上禾 a秉 ， b斗 ，中禾 c秉 ， d斗 ，下禾 e秉 ， f斗 。
"""

"""
To solve this problem, we will translate the ancient Chinese mathematical procedure into Python code step by step. This involves solving a system of linear equations using the described method. Here's the Python implementation:


"""


from fractions import Fraction

# Given equations:
# 3上禾 + 2中禾 + 1下禾 = 39斗
# 2上禾 + 3中禾 + 1下禾 = 34斗
# 1上禾 + 2中禾 + 3下禾 = 26斗

# Step 1: Represent the equations in matrix form
# Coefficients of the equations
matrix = [
    [3, 2, 1, 39],  # 3上禾 + 2中禾 + 1下禾 = 39
    [2, 3, 1, 34],  # 2上禾 + 3中禾 + 1下禾 = 34
    [1, 2, 3, 26]   # 1上禾 + 2中禾 + 3下禾 = 26
]

# Step 2: Perform Gaussian elimination to solve for 上禾, 中禾, 下禾

# Normalize the first row
factor = matrix[0][0]
for i in range(4):
    matrix[0][i] = Fraction(matrix[0][i], factor)

# Eliminate the first variable from the second and third rows
for row in range(1, 3):
    factor = matrix[row][0]
    for col in range(4):
        matrix[row][col] -= factor * matrix[0][col]

# Normalize the second row
factor = matrix[1][1]
for i in range(1, 4):
    matrix[1][i] = Fraction(matrix[1][i], factor)

# Eliminate the second variable from the third row
factor = matrix[2][1]
for col in range(1, 4):
    matrix[2][col] -= factor * matrix[1][col]

# Normalize the third row
factor = matrix[2][2]
for i in range(2, 4):
    matrix[2][i] = Fraction(matrix[2][i], factor)

# Back substitution to find the values of 上禾, 中禾, 下禾
下禾 = matrix[2][3]
中禾 = matrix[1][3] - matrix[1][2] * 下禾
上禾 = matrix[0][3] - matrix[0][2] * 下禾 - matrix[0][1] * 中禾

# Results
a, b = 1, 上禾  # 上禾 1秉, b斗
c, d = 1, 中禾  # 中禾 1秉, d斗
e, f = 1, 下禾  # 下禾 1秉, f斗

# Output the results
print(f"上禾 {a}秉, {b}斗")
print(f"中禾 {c}秉, {d}斗")
print(f"下禾 {e}秉, {f}斗")


"""


### Explanation of the Code:
1. **Matrix Representation**: The problem is represented as a system of linear equations in matrix form.
2. **Gaussian Elimination**: The procedure described in the problem is essentially Gaussian elimination, where we eliminate variables step by step to solve for the unknowns.
3. **Fraction Handling**: The `Fraction` class is used to ensure exact arithmetic, as ancient Chinese mathematics often dealt with fractions.

### Output:
The solution will provide the number of "斗" (volume) for each type of "禾" (grain) per "秉" (bundle).
"""


"""
"""
