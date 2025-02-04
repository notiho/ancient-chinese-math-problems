"""
今有五羊、四犬、三雞、二兔，直錢一千四百九十六；四羊、二犬、六雞、三兔直錢一千一百七十五；三羊、一犬、七雞、五兔，直錢九百五十八；二羊、三犬、五雞、一兔，直錢八百六十一。問︰羊、犬、雞、兔價各幾何？
荅曰：羊價 a ，犬價 b ，雞價 c ，兔價 d 。
"""

"""
This is a system of linear equations problem. Let's solve it step by step in Python using the given equations.

### Problem:
We are given the following equations based on the problem:

1. \( 5a + 4b + 3c + 2d = 1496 \)
2. \( 4a + 2b + 6c + 3d = 1175 \)
3. \( 3a + 1b + 7c + 5d = 958 \)
4. \( 2a + 3b + 5c + 1d = 861 \)

Where:
- \( a \) is the price of a sheep,
- \( b \) is the price of a dog,
- \( c \) is the price of a chicken,
- \( d \) is the price of a rabbit.

We will solve for \( a \), \( b \), \( c \), and \( d \).

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

# Define the coefficients matrix and the constants vector
coefficients = [
    [5, 4, 3, 2],
    [4, 2, 6, 3],
    [3, 1, 7, 5],
    [2, 3, 5, 1]
]

constants = [1496, 1175, 958, 861]

# Solve using substitution/elimination (manual Gaussian elimination)
# Step 1: Convert to row echelon form
def gaussian_elimination(coefficients, constants):
    n = len(coefficients)
    for i in range(n):
        # Make the diagonal element 1
        diag_element = coefficients[i][i]
        for j in range(i, n):
            coefficients[i][j] = Fraction(coefficients[i][j], diag_element)
        constants[i] = Fraction(constants[i], diag_element)
        
        # Eliminate the current column in rows below
        for k in range(i + 1, n):
            factor = coefficients[k][i]
            for j in range(i, n):
                coefficients[k][j] -= factor * coefficients[i][j]
            constants[k] -= factor * constants[i]
    
    return coefficients, constants

# Step 2: Back substitution
def back_substitution(coefficients, constants):
    n = len(coefficients)
    solution = [0] * n
    for i in range(n - 1, -1, -1):
        solution[i] = constants[i]
        for j in range(i + 1, n):
            solution[i] -= coefficients[i][j] * solution[j]
    return solution

# Perform Gaussian elimination and back substitution
coefficients, constants = gaussian_elimination(coefficients, constants)
solution = back_substitution(coefficients, constants)

# Extract the results
a, b, c, d = solution

# Print the results
print(f"羊價 a = {a}")
print(f"犬價 b = {b}")
print(f"雞價 c = {c}")
print(f"兔價 d = {d}")
#----- content ends here -----


"""


---

### Explanation of the Code:
1. **Gaussian Elimination**:
   - We first convert the system of equations into an upper triangular matrix (row echelon form) by dividing rows and eliminating variables step by step.
   
2. **Back Substitution**:
   - Once the matrix is in row echelon form, we solve for the variables starting from the last equation and substituting back into the previous ones.

3. **Fractions**:
   - The `Fraction` class is used to ensure exact arithmetic without floating-point errors.

---

### Output:
After running the code, the values of \( a \), \( b \), \( c \), and \( d \) will be printed, representing the prices of a sheep, a dog, a chicken, and a rabbit, respectively.
"""


"""
"""
