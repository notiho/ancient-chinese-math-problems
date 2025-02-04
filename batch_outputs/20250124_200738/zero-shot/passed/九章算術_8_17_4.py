"""
今有麻九斗、麥七斗、菽三斗、答二斗、黍五斗，直錢一百四十；麻七斗、麥六斗、菽四斗、答五斗、黍三斗，直錢一百二十八；麻三斗、麥五斗、菽七斗、答六斗、黍四斗，直錢一百一十六；麻二斗、麥五斗、菽三斗、答九斗、黍四斗，直錢一百一十二；麻一斗、麥三斗、菽二斗、答八斗、黍五斗，直錢九十五。問︰一斗直幾何？
術曰：如方程，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：麻一斗 a錢 ，麥一斗 b錢 ，菽一斗 c錢 ，答一斗 d錢 ，黍一斗 e錢 。
"""

"""
To solve this problem, we need to translate the given system of linear equations into Python code and solve for the unknowns `a`, `b`, `c`, `d`, and `e`. We will use the `Fraction` class to ensure precise arithmetic with fractions.

The system of equations is as follows:
```
9a + 7b + 3c + 2d + 5e = 140
7a + 6b + 4c + 5d + 3e = 128
3a + 5b + 7c + 6d + 4e = 116
2a + 5b + 3c + 9d + 4e = 112
1a + 3b + 2c + 8d + 5e = 95
```

Here is the Python code to solve for the unknowns:


"""

#----- content starts here -----

from fractions import Fraction

# Coefficients of the equations
# Equation 1: 9a + 7b + 3c + 2d + 5e = 140
# Equation 2: 7a + 6b + 4c + 5d + 3e = 128
# Equation 3: 3a + 5b + 7c + 6d + 4e = 116
# Equation 4: 2a + 5b + 3c + 9d + 4e = 112
# Equation 5: 1a + 3b + 2c + 8d + 5e = 95

# Define the augmented matrix
matrix = [
    [9, 7, 3, 2, 5, 140],
    [7, 6, 4, 5, 3, 128],
    [3, 5, 7, 6, 4, 116],
    [2, 5, 3, 9, 4, 112],
    [1, 3, 2, 8, 5, 95]
]

# Convert all elements to Fractions for precise arithmetic
matrix = [[Fraction(x) for x in row] for row in matrix]

# Perform Gaussian elimination
n = len(matrix)

# Forward elimination
for i in range(n):
    # Make the diagonal element 1
    diag = matrix[i][i]
    for j in range(i, n + 1):
        matrix[i][j] /= diag
    
    # Make the elements below the diagonal 0
    for k in range(i + 1, n):
        factor = matrix[k][i]
        for j in range(i, n + 1):
            matrix[k][j] -= factor * matrix[i][j]

# Back substitution
solution = [Fraction(0)] * n
for i in range(n - 1, -1, -1):
    solution[i] = matrix[i][n]
    for j in range(i + 1, n):
        solution[i] -= matrix[i][j] * solution[j]

# Assign the solutions to the variables
a, b, c, d, e = solution

# Output the results
a, b, c, d, e
#----- content ends here -----


"""


### Explanation:
1. **Matrix Representation**: The system of equations is represented as an augmented matrix, where the last column contains the constants on the right-hand side of the equations.
2. **Gaussian Elimination**:
   - Forward elimination is used to transform the matrix into an upper triangular form.
   - Back substitution is used to solve for the unknowns.
3. **Fraction Class**: All calculations are performed using the `Fraction` class to ensure precise results, especially since the coefficients and solutions might not be integers.
4. **Solution Assignment**: The solutions are assigned to the variables `a`, `b`, `c`, `d`, and `e`.

### Output:
The values of `a`, `b`, `c`, `d`, and `e` will be computed and stored in the respective variables.
"""


"""
"""
