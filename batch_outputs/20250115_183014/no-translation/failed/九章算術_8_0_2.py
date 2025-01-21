"""
今有上禾三秉，中禾二秉，下禾一秉，實三十九斗；上禾二秉，中禾三秉，下禾一秉，實三十四斗；上禾一秉，中禾二秉，下禾三秉，實二十六斗。問︰上、中、下禾實一秉各幾何？
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：上禾 a秉 ， b斗 ，中禾 c秉 ， d斗 ，下禾 e秉 ， f斗 。
"""

"""
To solve this problem, we will translate the ancient Chinese mathematical procedure into Python code step by step. The problem involves solving a system of linear equations using the described method. Here's the Python implementation:


"""


from fractions import Fraction

# Given equations:
# 3上禾 + 2中禾 + 1下禾 = 39斗
# 2上禾 + 3中禾 + 1下禾 = 34斗
# 1上禾 + 2中禾 + 3下禾 = 26斗

# Step 1: Represent the equations as a matrix
matrix = [
    [3, 2, 1, 39],  # First equation
    [2, 3, 1, 34],  # Second equation
    [1, 2, 3, 26]   # Third equation
]

# Step 2: Eliminate the first variable (上禾) from the second and third rows
for i in range(1, 3):
    factor = Fraction(matrix[i][0], matrix[0][0])
    for j in range(4):
        matrix[i][j] -= factor * matrix[0][j]

# Step 3: Eliminate the second variable (中禾) from the third row
factor = Fraction(matrix[2][1], matrix[1][1])
for j in range(1, 4):
    matrix[2][j] -= factor * matrix[1][j]

# Step 4: Solve for 下禾 (last variable)
下禾 = Fraction(matrix[2][3], matrix[2][2])

# Step 5: Solve for 中禾 (second variable)
中禾 = Fraction(matrix[1][3] - matrix[1][2] * 下禾, matrix[1][1])

# Step 6: Solve for 上禾 (first variable)
上禾 = Fraction(matrix[0][3] - matrix[0][2] * 下禾 - matrix[0][1] * 中禾, matrix[0][0])

# Results
a, b = 上禾.numerator, 上禾.denominator
c, d = 中禾.numerator, 中禾.denominator
e, f = 下禾.numerator, 下禾.denominator

print(f"上禾 {a}秉 ， {b}斗 ，中禾 {c}秉 ， {d}斗 ，下禾 {e}秉 ， {f}斗 。")


"""


### Explanation of the Code:
1. **Matrix Representation**: The system of equations is represented as a matrix where each row corresponds to an equation, and the last column represents the constants on the right-hand side of the equations.
2. **Gaussian Elimination**: The procedure described in the problem is essentially Gaussian elimination. We eliminate variables step by step to solve for the unknowns.
3. **Fractions**: The `Fraction` class is used to ensure exact arithmetic throughout the calculations, as described in the ancient method.
4. **Results**: The final results are presented as fractions, representing the exact values of the quantities for each type of grain.

This code will output the exact values for the quantities of 上禾, 中禾, and 下禾 per 秉 and 斗.
"""


"""
Variable 'a' has wrong value. Expected: 1, Actual: 37
Variable 'b' has wrong value. Expected: 37/4, Actual: 4
Variable 'c' has wrong value. Expected: 1, Actual: 17
Variable 'd' has wrong value. Expected: 17/4, Actual: 4
Variable 'e' has wrong value. Expected: 1, Actual: 11
Variable 'f' has wrong value. Expected: 11/4, Actual: 4"""
