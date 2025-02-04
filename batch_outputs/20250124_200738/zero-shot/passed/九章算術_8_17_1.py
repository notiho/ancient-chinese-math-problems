"""
今有麻九斗、麥七斗、菽三斗、答二斗、黍五斗，直錢一百四十；麻七斗、麥六斗、菽四斗、答五斗、黍三斗，直錢一百二十八；麻三斗、麥五斗、菽七斗、答六斗、黍四斗，直錢一百一十六；麻二斗、麥五斗、菽三斗、答九斗、黍四斗，直錢一百一十二；麻一斗、麥三斗、菽二斗、答八斗、黍五斗，直錢九十五。問︰一斗直幾何？
術曰：如方程，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：麻一斗 a錢 ，麥一斗 b錢 ，菽一斗 c錢 ，答一斗 d錢 ，黍一斗 e錢 。
"""

"""
To solve this problem, we need to translate the ancient Chinese system of equations into Python code and compute the values of the unknowns \( a \), \( b \), \( c \), \( d \), and \( e \). We'll use the `Fraction` class to ensure precise calculations.

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Coefficients of the equations
# Each equation corresponds to the price of a combination of grains
# 麻 (a), 麥 (b), 菽 (c), 答 (d), 黍 (e)
equations = [
    [9, 7, 3, 2, 5, 140],  # 9a + 7b + 3c + 2d + 5e = 140
    [7, 6, 4, 5, 3, 128],  # 7a + 6b + 4c + 5d + 3e = 128
    [3, 5, 7, 6, 4, 116],  # 3a + 5b + 7c + 6d + 4e = 116
    [2, 5, 3, 9, 4, 112],  # 2a + 5b + 3c + 9d + 4e = 112
    [1, 3, 2, 8, 5, 95]    # 1a + 3b + 2c + 8d + 5e = 95
]

# Solve the system of linear equations using substitution or elimination
# Represent the equations as a matrix
matrix = [
    [Fraction(eq[i]) for i in range(5)] + [Fraction(eq[5])]
    for eq in equations
]

# Perform Gaussian elimination
for i in range(5):
    # Normalize the pivot row
    pivot = matrix[i][i]
    for j in range(i, 6):
        matrix[i][j] /= pivot
    
    # Eliminate the current variable from the rows below
    for k in range(i + 1, 5):
        factor = matrix[k][i]
        for j in range(i, 6):
            matrix[k][j] -= factor * matrix[i][j]

# Back substitution to find the solution
solution = [0] * 5
for i in range(4, -1, -1):
    solution[i] = matrix[i][5]
    for j in range(i + 1, 5):
        solution[i] -= matrix[i][j] * solution[j]

# Assign the solutions to the respective variables
a, b, c, d, e = solution

# Output the results
a, b, c, d, e
#----- content ends here -----


"""


### Explanation of the Code:
1. **Equations Setup**: The coefficients of the equations are extracted from the problem statement and stored in a list of lists.
2. **Matrix Representation**: Each equation is represented as a row in a matrix, with the last element being the constant term (the total price in this case).
3. **Gaussian Elimination**: The system of equations is solved using Gaussian elimination:
   - Normalize the pivot row.
   - Eliminate the variable from the rows below.
4. **Back Substitution**: Once the matrix is in row-echelon form, back substitution is used to compute the values of the unknowns.
5. **Assign Variables**: The solutions are assigned to the variables \( a \), \( b \), \( c \), \( d \), and \( e \).

### Solution:
The variables \( a \), \( b \), \( c \), \( d \), and \( e \) represent the price of one unit of 麻 (a), 麥 (b), 菽 (c), 答 (d), and 黍 (e), respectively. The computed values will be in terms of fractions for exactness.
"""


"""
"""
