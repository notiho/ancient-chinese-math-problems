"""
今有五羊、四犬、三雞、二兔，直錢一千四百九十六；四羊、二犬、六雞、三兔直錢一千一百七十五；三羊、一犬、七雞、五兔，直錢九百五十八；二羊、三犬、五雞、一兔，直錢八百六十一。問︰羊、犬、雞、兔價各幾何？
術曰：如方程，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：羊價 a ，犬價 b ，雞價 c ，兔價 d 。
"""

"""
This problem involves solving a system of linear equations, which is described in the ancient Chinese mathematical text using the "正負術" (positive and negative method, equivalent to Gaussian elimination). Below is the Python implementation of the procedure:


"""


from fractions import Fraction

# Coefficients of the equations
# 5羊 + 4犬 + 3雞 + 2兔 = 1496
# 4羊 + 2犬 + 6雞 + 3兔 = 1175
# 3羊 + 1犬 + 7雞 + 5兔 = 958
# 2羊 + 3犬 + 5雞 + 1兔 = 861

# Representing the equations as a matrix
matrix = [
    [5, 4, 3, 2, 1496],
    [4, 2, 6, 3, 1175],
    [3, 1, 7, 5, 958],
    [2, 3, 5, 1, 861]
]

# Gaussian elimination process
def gaussian_elimination(matrix):
    n = len(matrix)

    # Forward elimination
    for i in range(n):
        # Normalize the pivot row
        pivot = matrix[i][i]
        for j in range(i, n + 1):
            matrix[i][j] = Fraction(matrix[i][j], pivot)

        # Eliminate the current variable from the rows below
        for k in range(i + 1, n):
            factor = matrix[k][i]
            for j in range(i, n + 1):
                matrix[k][j] -= factor * matrix[i][j]

    # Back substitution
    solution = [0] * n
    for i in range(n - 1, -1, -1):
        solution[i] = matrix[i][n]
        for j in range(i + 1, n):
            solution[i] -= matrix[i][j] * solution[j]

    return solution

# Solve the system of equations
solution = gaussian_elimination(matrix)

# Extract the values for 羊, 犬, 雞, 兔
a, b, c, d = solution

# Output the results
a, b, c, d


"""


### Explanation of the Code:
1. **Matrix Representation**: The system of equations is represented as an augmented matrix, where the last column contains the constants on the right-hand side of the equations.
2. **Gaussian Elimination**: The process involves forward elimination to make the matrix upper triangular, followed by back substitution to solve for the variables.
3. **Fraction Handling**: The `Fraction` class is used to ensure exact arithmetic, as required by the ancient procedure.

### Results:
- `a`: Price of a sheep (羊價)
- `b`: Price of a dog (犬價)
- `c`: Price of a chicken (雞價)
- `d`: Price of a rabbit (兔價)
"""


"""
"""
