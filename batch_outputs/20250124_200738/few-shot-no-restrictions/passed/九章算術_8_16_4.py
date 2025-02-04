"""
今有五羊、四犬、三雞、二兔，直錢一千四百九十六；四羊、二犬、六雞、三兔直錢一千一百七十五；三羊、一犬、七雞、五兔，直錢九百五十八；二羊、三犬、五雞、一兔，直錢八百六十一。問︰羊、犬、雞、兔價各幾何？
術曰：如方程，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：羊價 a ，犬價 b ，雞價 c ，兔價 d 。
"""

"""
This problem is a classic system of linear equations, where we are tasked with solving for the prices of sheep (羊), dogs (犬), chickens (雞), and rabbits (兔). The problem can be solved using matrix methods or Gaussian elimination, as described in the ancient Chinese "方程術" (method of solving simultaneous equations). Below is the Python implementation of the solution:

---

### Problem Setup:
We are given four equations:
1. \( 5x + 4y + 3z + 2w = 1496 \)
2. \( 4x + 2y + 6z + 3w = 1175 \)
3. \( 3x + y + 7z + 5w = 958 \)
4. \( 2x + 3y + 5z + w = 861 \)

Where:
- \( x \) is the price of a sheep (羊價),
- \( y \) is the price of a dog (犬價),
- \( z \) is the price of a chicken (雞價),
- \( w \) is the price of a rabbit (兔價).

We will solve this system of equations using Gaussian elimination.

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
    [2, 3, 5, 1]   # Coefficients of the fourth equation
]

# Constants on the right-hand side
B = [1496, 1175, 958, 861]

# Convert to fractions for exact arithmetic
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
print(f"羊價 (price of a sheep): {a}")
print(f"犬價 (price of a dog): {b}")
print(f"雞價 (price of a chicken): {c}")
print(f"兔價 (price of a rabbit): {d}")
#----- content ends here -----


"""


---

### Explanation of the Code:
1. **Matrix Representation**: The coefficients of the variables are stored in matrix `A`, and the constants on the right-hand side are stored in vector `B`.
2. **Gaussian Elimination**:
   - **Forward Elimination**: The matrix is transformed into an upper triangular form by eliminating variables row by row.
   - **Back Substitution**: Starting from the last row, the values of the variables are calculated by substituting known values into the equations.
3. **Exact Arithmetic**: The `Fraction` class is used to ensure exact arithmetic throughout the calculations, avoiding floating-point errors.

---

### Output:
The solution will provide the exact prices of the sheep, dogs, chickens, and rabbits:
```
羊價 (price of a sheep): a
犬價 (price of a dog): b
雞價 (price of a chicken): c
兔價 (price of a rabbit): d
```

Replace `a`, `b`, `c`, and `d` with the computed values.
"""


"""
"""
