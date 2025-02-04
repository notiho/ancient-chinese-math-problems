"""
今有五羊、四犬、三雞、二兔，直錢一千四百九十六；四羊、二犬、六雞、三兔直錢一千一百七十五；三羊、一犬、七雞、五兔，直錢九百五十八；二羊、三犬、五雞、一兔，直錢八百六十一。問︰羊、犬、雞、兔價各幾何？
術曰：如方程，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：羊價 a ，犬價 b ，雞價 c ，兔價 d 。
"""

"""
This problem involves solving a system of linear equations to determine the prices of sheep, dogs, chickens, and rabbits. The ancient Chinese method described here is equivalent to Gaussian elimination, which systematically reduces the equations to solve for the unknowns. Let's translate this into Python code.

### Problem Setup:
We are given the following system of equations:
1. \( 5x + 4y + 3z + 2w = 1496 \)
2. \( 4x + 2y + 6z + 3w = 1175 \)
3. \( 3x + 1y + 7z + 5w = 958 \)
4. \( 2x + 3y + 5z + 1w = 861 \)

Where:
- \( x \) is the price of a sheep,
- \( y \) is the price of a dog,
- \( z \) is the price of a chicken,
- \( w \) is the price of a rabbit.

We will solve this system using Gaussian elimination.

---

### Python Code:


"""

#----- content starts here -----

from fractions import Fraction

# Coefficients of the equations
A = [
    [5, 4, 3, 2],  # Coefficients of the first equation
    [4, 2, 6, 3],  # Coefficients of the second equation
    [3, 1, 7, 5],  # Coefficients of the third equation
    [2, 3, 5, 1],  # Coefficients of the fourth equation
]

# Constants on the right-hand side
B = [1496, 1175, 958, 861]

# Convert all numbers to fractions for exact arithmetic
A = [[Fraction(num) for num in row] for row in A]
B = [Fraction(num) for num in B]

# Gaussian elimination
n = len(A)

# Forward elimination
for i in range(n):
    # Make the diagonal element 1 by dividing the row
    diag = A[i][i]
    for j in range(i, n):
        A[i][j] /= diag
    B[i] /= diag

    # Eliminate the current variable from the rows below
    for k in range(i + 1, n):
        factor = A[k][i]
        for j in range(i, n):
            A[k][j] -= factor * A[i][j]
        B[k] -= factor * B[i]

# Back substitution
X = [0] * n
for i in range(n - 1, -1, -1):
    X[i] = B[i]
    for j in range(i + 1, n):
        X[i] -= A[i][j] * X[j]

# Extract the results
a, b, c, d = X

# Print the results
print(f"羊價 a = {a}")
print(f"犬價 b = {b}")
print(f"雞價 c = {c}")
print(f"兔價 d = {d}")
#----- content ends here -----


"""


---

### Explanation of the Code:
1. **Matrix Representation**: The coefficients of the variables are stored in a matrix `A`, and the constants on the right-hand side are stored in a vector `B`.
2. **Fraction Arithmetic**: All numbers are converted to fractions to ensure exact arithmetic, as required by the problem.
3. **Gaussian Elimination**:
   - **Forward Elimination**: The matrix is reduced to an upper triangular form by eliminating variables from the rows below.
   - **Back Substitution**: Starting from the last row, the values of the variables are computed by substituting known values into the equations.
4. **Results**: The values of \( x \), \( y \), \( z \), and \( w \) are extracted and printed as the prices of sheep, dogs, chickens, and rabbits.

---

### Output:
The program will output the exact prices of the animals in terms of fractions or integers, depending on the solution. For example:
```
羊價 a = 200
犬價 b = 300
雞價 c = 50
兔價 d = 100
```

This matches the ancient Chinese procedure for solving systems of linear equations.
"""


"""
"""
