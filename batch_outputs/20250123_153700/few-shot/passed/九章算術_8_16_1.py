"""
今有五羊、四犬、三雞、二兔，直錢一千四百九十六；四羊、二犬、六雞、三兔直錢一千一百七十五；三羊、一犬、七雞、五兔，直錢九百五十八；二羊、三犬、五雞、一兔，直錢八百六十一。問︰羊、犬、雞、兔價各幾何？
術曰：如方程，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：羊價 a ，犬價 b ，雞價 c ，兔價 d 。
"""

"""
This problem is a classic system of linear equations, where the prices of sheep (羊), dogs (犬), chickens (雞), and rabbits (兔) are unknowns. The solution involves solving these equations using the method described in ancient Chinese mathematics, which is equivalent to Gaussian elimination in modern terms.

Here is the Python implementation of the problem:


"""


from fractions import Fraction

# Coefficients of the equations
# 5羊 + 4犬 + 3雞 + 2兔 = 1496
# 4羊 + 2犬 + 6雞 + 3兔 = 1175
# 3羊 + 1犬 + 7雞 + 5兔 = 958
# 2羊 + 3犬 + 5雞 + 1兔 = 861

# Matrix representation of the system
matrix = [
    [5, 4, 3, 2, 1496],
    [4, 2, 6, 3, 1175],
    [3, 1, 7, 5, 958],
    [2, 3, 5, 1, 861]
]

# Perform Gaussian elimination
for i in range(len(matrix)):
    # Normalize the current row
    divisor = matrix[i][i]
    for j in range(len(matrix[i])):
        matrix[i][j] = Fraction(matrix[i][j], divisor)
    
    # Eliminate the current variable from the rows below
    for k in range(i + 1, len(matrix)):
        multiplier = matrix[k][i]
        for j in range(len(matrix[k])):
            matrix[k][j] -= multiplier * matrix[i][j]

# Back substitution to solve for the variables
solutions = [0] * len(matrix)
for i in range(len(matrix) - 1, -1, -1):
    solutions[i] = matrix[i][-1]
    for j in range(i + 1, len(matrix)):
        solutions[i] -= matrix[i][j] * solutions[j]

# Assign the solutions to the respective variables
a = solutions[0]  # 羊價
b = solutions[1]  # 犬價
c = solutions[2]  # 雞價
d = solutions[3]  # 兔價

# Output the results
a, b, c, d


"""


### Explanation of the Code:
1. **Matrix Representation**: The system of equations is represented as a matrix where each row corresponds to an equation, and the last column is the constant term.
2. **Gaussian Elimination**: The process involves normalizing each row and eliminating variables from subsequent rows to create an upper triangular matrix.
3. **Back Substitution**: Once the matrix is in upper triangular form, the solutions are obtained by substituting values back into the equations.
4. **Fraction Class**: The `Fraction` class ensures that all calculations are performed exactly without floating-point errors.

### Final Answer:
The values of `a`, `b`, `c`, and `d` represent the prices of sheep, dogs, chickens, and rabbits, respectively, in terms of money (錢).
"""


"""
"""
