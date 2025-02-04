"""
今有麻九斗、麥七斗、菽三斗、答二斗、黍五斗，直錢一百四十；麻七斗、麥六斗、菽四斗、答五斗、黍三斗，直錢一百二十八；麻三斗、麥五斗、菽七斗、答六斗、黍四斗，直錢一百一十六；麻二斗、麥五斗、菽三斗、答九斗、黍四斗，直錢一百一十二；麻一斗、麥三斗、菽二斗、答八斗、黍五斗，直錢九十五。問︰一斗直幾何？
術曰：如方程，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：麻一斗 a錢 ，麥一斗 b錢 ，菽一斗 c錢 ，答一斗 d錢 ，黍一斗 e錢 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into a system of linear equations and solve for the unknowns \( a, b, c, d, e \). Here's the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Define the equations based on the problem statement
# Each equation corresponds to the total cost of the grains
# Equation 1: 9a + 7b + 3c + 2d + 5e = 140
# Equation 2: 7a + 6b + 4c + 5d + 3e = 128
# Equation 3: 3a + 5b + 7c + 6d + 4e = 116
# Equation 4: 2a + 5b + 3c + 9d + 4e = 112
# Equation 5: 1a + 3b + 2c + 8d + 5e = 95

# Solve the system of equations using substitution or elimination
# Representing the equations in matrix form:
# | 9  7  3  2  5 |   | a |   | 140 |
# | 7  6  4  5  3 | * | b | = | 128 |
# | 3  5  7  6  4 |   | c |   | 116 |
# | 2  5  3  9  4 |   | d |   | 112 |
# | 1  3  2  8  5 |   | e |   |  95 |

# Using Gaussian elimination to solve for a, b, c, d, e

# Step 1: Write the augmented matrix
matrix = [
    [9, 7, 3, 2, 5, 140],
    [7, 6, 4, 5, 3, 128],
    [3, 5, 7, 6, 4, 116],
    [2, 5, 3, 9, 4, 112],
    [1, 3, 2, 8, 5, 95]
]

# Step 2: Perform Gaussian elimination
# Convert to row echelon form
for i in range(len(matrix)):
    # Normalize the current row
    factor = matrix[i][i]
    for j in range(len(matrix[i])):
        matrix[i][j] = Fraction(matrix[i][j], factor)
    
    # Eliminate the current variable from the rows below
    for k in range(i + 1, len(matrix)):
        factor = matrix[k][i]
        for j in range(len(matrix[k])):
            matrix[k][j] -= factor * matrix[i][j]

# Step 3: Back substitution to solve for variables
variables = [0] * 5
for i in range(len(matrix) - 1, -1, -1):
    variables[i] = matrix[i][-1]
    for j in range(i + 1, len(matrix)):
        variables[i] -= matrix[i][j] * variables[j]

# Assign the solutions to the respective variables
a, b, c, d, e = variables

# Print the results
print(f"a = {a} 錢")
print(f"b = {b} 錢")
print(f"c = {c} 錢")
print(f"d = {d} 錢")
print(f"e = {e} 錢")
#----- content ends here -----


"""


This code uses Gaussian elimination to solve the system of linear equations and assigns the solutions to the variables \( a, b, c, d, e \). Each variable represents the cost of one斗 of the respective grain in 錢. The `Fraction` class ensures that the calculations are accurate and can handle non-integer results.
"""


"""
"""
