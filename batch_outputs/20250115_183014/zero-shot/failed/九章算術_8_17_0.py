"""
今有麻九斗、麥七斗、菽三斗、答二斗、黍五斗，直錢一百四十；麻七斗、麥六斗、菽四斗、答五斗、黍三斗，直錢一百二十八；麻三斗、麥五斗、菽七斗、答六斗、黍四斗，直錢一百一十六；麻二斗、麥五斗、菽三斗、答九斗、黍四斗，直錢一百一十二；麻一斗、麥三斗、菽二斗、答八斗、黍五斗，直錢九十五。問︰一斗直幾何？
術曰：如方程，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：麻 a斗 b錢 ，麥 c斗 d錢 ，菽 e斗 f錢 ，答 g斗 h錢 ，黍 i斗 j錢 。
"""

"""
To solve this problem, we need to translate the ancient Chinese mathematical system into a modern Python program. The problem involves solving a system of linear equations to determine the price per unit (斗) of 麻 (a), 麥 (c), 菽 (e), 答 (g), and 黍 (i). Here's the Python code to compute the solution:


"""


from fractions import Fraction

# Coefficients of the equations
# Each row corresponds to the coefficients of 麻, 麥, 菽, 答, 黍, and the total price
equations = [
    [9, 7, 3, 2, 5, 140],
    [7, 6, 4, 5, 3, 128],
    [3, 5, 7, 6, 4, 116],
    [2, 5, 3, 9, 4, 112],
    [1, 3, 2, 8, 5, 95]
]

# Using Gaussian elimination to solve the system of equations
# Convert the equations into a matrix
matrix = [[Fraction(num) for num in row] for row in equations]

# Forward elimination
for i in range(len(matrix)):
    # Make the diagonal element 1
    diag = matrix[i][i]
    for j in range(len(matrix[i])):
        matrix[i][j] /= diag
    
    # Make the elements below the diagonal 0
    for k in range(i + 1, len(matrix)):
        factor = matrix[k][i]
        for j in range(len(matrix[k])):
            matrix[k][j] -= factor * matrix[i][j]

# Back substitution
solution = [0] * len(matrix)
for i in range(len(matrix) - 1, -1, -1):
    solution[i] = matrix[i][-1]
    for j in range(i + 1, len(matrix)):
        solution[i] -= matrix[i][j] * solution[j]

# Assign the solutions to the variables
a = solution[0]  # 麻 price per 斗
c = solution[1]  # 麥 price per 斗
e = solution[2]  # 菽 price per 斗
g = solution[3]  # 答 price per 斗
i = solution[4]  # 黍 price per 斗

# Print the results
print(f"麻 a斗 {a}錢")
print(f"麥 c斗 {c}錢")
print(f"菽 e斗 {e}錢")
print(f"答 g斗 {g}錢")
print(f"黍 i斗 {i}錢")


"""


### Explanation:
1. **Input Representation**: The coefficients of the equations are stored in a list of lists, where each sublist represents one equation.
2. **Gaussian Elimination**: The system of equations is solved using Gaussian elimination, which involves forward elimination to create an upper triangular matrix and back substitution to find the solutions.
3. **Fractions**: The `Fraction` class is used to ensure that all calculations are exact and to handle non-integer results.
4. **Variable Assignment**: The solutions are assigned to variables `a`, `c`, `e`, `g`, and `i`, corresponding to the prices per 斗 of 麻, 麥, 菽, 答, and 黍, respectively.

This code will compute the exact prices per 斗 for each type of grain.
"""


"""
Variable 'a' has wrong value. Expected: 1, Actual: 7
Missing variable in output: 'b'
Variable 'c' has wrong value. Expected: 1, Actual: 4
Missing variable in output: 'd'
Variable 'e' has wrong value. Expected: 1, Actual: 3
Missing variable in output: 'f'
Variable 'g' has wrong value. Expected: 1, Actual: 5
Missing variable in output: 'h'
Variable 'i' has wrong value. Expected: 1, Actual: 6
Variable 'j' has wrong value. Expected: 6, Actual: 4"""
