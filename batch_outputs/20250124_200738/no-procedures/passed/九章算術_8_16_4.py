"""
今有五羊、四犬、三雞、二兔，直錢一千四百九十六；四羊、二犬、六雞、三兔直錢一千一百七十五；三羊、一犬、七雞、五兔，直錢九百五十八；二羊、三犬、五雞、一兔，直錢八百六十一。問︰羊、犬、雞、兔價各幾何？
荅曰：羊價 a ，犬價 b ，雞價 c ，兔價 d 。
"""

"""
This problem involves solving a system of linear equations to determine the price of each animal (sheep, dog, chicken, and rabbit). Let's translate this into Python code using the `Fraction` class to ensure precise calculations.

### Problem:
We are given the following equations based on the problem statement:

1. \( 5a + 4b + 3c + 2d = 1496 \)
2. \( 4a + 2b + 6c + 3d = 1175 \)
3. \( 3a + 1b + 7c + 5d = 958 \)
4. \( 2a + 3b + 5c + 1d = 861 \)

Where:
- \( a \) is the price of a sheep,
- \( b \) is the price of a dog,
- \( c \) is the price of a chicken,
- \( d \) is the price of a rabbit.

We need to solve for \( a \), \( b \), \( c \), and \( d \).

---

### Python Code:


"""

#----- content starts here -----

from fractions import Fraction

# Coefficients of the equations
# 5a + 4b + 3c + 2d = 1496
# 4a + 2b + 6c + 3d = 1175
# 3a + 1b + 7c + 5d = 958
# 2a + 3b + 5c + 1d = 861

# Representing the equations as matrices
A = [
    [5, 4, 3, 2],
    [4, 2, 6, 3],
    [3, 1, 7, 5],
    [2, 3, 5, 1]
]

B = [1496, 1175, 958, 861]

# Function to perform Gaussian elimination
def gaussian_elimination(A, B):
    n = len(A)
    # Forward elimination
    for i in range(n):
        # Make the diagonal element 1
        diag = A[i][i]
        for j in range(i, n):
            A[i][j] = Fraction(A[i][j], diag)
        B[i] = Fraction(B[i], diag)
        
        # Eliminate the current column in rows below
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
    return X

# Solve the system of equations
result = gaussian_elimination(A, B)

# Extract the results
a, b, c, d = result

# Print the results
print(f"羊價 a = {a}")
print(f"犬價 b = {b}")
print(f"雞價 c = {c}")
print(f"兔價 d = {d}")
#----- content ends here -----


"""


---

### Explanation:
1. **Matrix Representation**:
   - The coefficients of \( a \), \( b \), \( c \), and \( d \) are stored in matrix `A`.
   - The constants on the right-hand side of the equations are stored in vector `B`.

2. **Gaussian Elimination**:
   - The function `gaussian_elimination` performs forward elimination to convert the matrix into an upper triangular form.
   - Then, back substitution is used to solve for the variables \( a \), \( b \), \( c \), and \( d \).

3. **Output**:
   - The solution gives the price of each animal in terms of fractions for precise results.

---

### Results:
When you run the code, it will output the prices of the sheep, dog, chicken, and rabbit.
"""


"""
"""
