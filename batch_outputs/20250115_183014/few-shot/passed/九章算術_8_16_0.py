"""
今有五羊、四犬、三雞、二兔，直錢一千四百九十六；四羊、二犬、六雞、三兔直錢一千一百七十五；三羊、一犬、七雞、五兔，直錢九百五十八；二羊、三犬、五雞、一兔，直錢八百六十一。問︰羊、犬、雞、兔價各幾何？
術曰：如方程，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：羊價 a ，犬價 b ，雞價 c ，兔價 d 。
"""

"""
This problem involves solving a system of linear equations using the ancient Chinese method of elimination, which is similar to Gaussian elimination. Let's translate the problem into Python code step by step.

### Problem Setup:
We are given four equations:
1. \( 5x + 4y + 3z + 2w = 1496 \)
2. \( 4x + 2y + 6z + 3w = 1175 \)
3. \( 3x + y + 7z + 5w = 958 \)
4. \( 2x + 3y + 5z + w = 861 \)

Where:
- \( x \) is the price of a sheep,
- \( y \) is the price of a dog,
- \( z \) is the price of a chicken,
- \( w \) is the price of a rabbit.

We need to solve for \( x, y, z, w \).

### Procedure:
The ancient Chinese elimination method (方程術) involves systematically eliminating variables by multiplying rows and subtracting them, similar to Gaussian elimination.

### Python Code:


"""


from fractions import Fraction

# Coefficients of the equations
matrix = [
    [5, 4, 3, 2, 1496],  # 5x + 4y + 3z + 2w = 1496
    [4, 2, 6, 3, 1175],  # 4x + 2y + 6z + 3w = 1175
    [3, 1, 7, 5, 958],   # 3x + y + 7z + 5w = 958
    [2, 3, 5, 1, 861]    # 2x + 3y + 5z + w = 861
]

# Step 1: Eliminate the first variable (x) from rows 2, 3, and 4
for i in range(1, 4):
    factor = Fraction(matrix[i][0], matrix[0][0])
    for j in range(5):
        matrix[i][j] -= factor * matrix[0][j]

# Step 2: Eliminate the second variable (y) from rows 3 and 4
for i in range(2, 4):
    factor = Fraction(matrix[i][1], matrix[1][1])
    for j in range(5):
        matrix[i][j] -= factor * matrix[1][j]

# Step 3: Eliminate the third variable (z) from row 4
factor = Fraction(matrix[3][2], matrix[2][2])
for j in range(5):
    matrix[3][j] -= factor * matrix[2][j]

# Step 4: Back-substitution to solve for w, z, y, x
w = Fraction(matrix[3][4], matrix[3][3])
z = Fraction(matrix[2][4] - matrix[2][3] * w, matrix[2][2])
y = Fraction(matrix[1][4] - matrix[1][3] * w - matrix[1][2] * z, matrix[1][1])
x = Fraction(matrix[0][4] - matrix[0][3] * w - matrix[0][2] * z - matrix[0][1] * y, matrix[0][0])

# Results
a = x  # Price of a sheep
b = y  # Price of a dog
c = z  # Price of a chicken
d = w  # Price of a rabbit

# Output the results
a, b, c, d


"""


### Explanation:
1. **Matrix Representation**: Each equation is represented as a row in the matrix, with the last column being the constant term.
2. **Elimination**: We eliminate variables step by step, reducing the system to an upper triangular form.
3. **Back-Substitution**: Once the matrix is in triangular form, we solve for the variables starting from the last row.

### Answer:
The prices of the animals are:
- \( a \): Price of a sheep
- \( b \): Price of a dog
- \( c \): Price of a chicken
- \( d \): Price of a rabbit

The exact values will be computed when the code is executed.
"""


"""
"""
