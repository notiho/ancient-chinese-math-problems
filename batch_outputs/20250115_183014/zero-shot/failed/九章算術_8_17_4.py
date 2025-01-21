"""
今有麻九斗、麥七斗、菽三斗、答二斗、黍五斗，直錢一百四十；麻七斗、麥六斗、菽四斗、答五斗、黍三斗，直錢一百二十八；麻三斗、麥五斗、菽七斗、答六斗、黍四斗，直錢一百一十六；麻二斗、麥五斗、菽三斗、答九斗、黍四斗，直錢一百一十二；麻一斗、麥三斗、菽二斗、答八斗、黍五斗，直錢九十五。問︰一斗直幾何？
術曰：如方程，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：麻 a斗 b錢 ，麥 c斗 d錢 ，菽 e斗 f錢 ，答 g斗 h錢 ，黍 i斗 j錢 。
"""

"""
To solve this problem, we need to translate the ancient Chinese mathematical problem into a system of linear equations and solve for the unknowns. Each unknown represents the price of one斗 of a specific grain. We will use Python and the `Fraction` class to ensure precise calculations.

The problem provides the following system of equations:

1. \( 9a + 7c + 3e + 2g + 5i = 140 \)
2. \( 7a + 6c + 4e + 5g + 3i = 128 \)
3. \( 3a + 5c + 7e + 6g + 4i = 116 \)
4. \( 2a + 5c + 3e + 9g + 4i = 112 \)
5. \( 1a + 3c + 2e + 8g + 5i = 95 \)

Here, \( a, c, e, g, i \) represent the prices per斗 of 麻 (a), 麥 (c), 菽 (e), 答 (g), and 黍 (i), respectively.

We will solve this system of linear equations using Python.


"""


from fractions import Fraction

# Coefficients of the equations
# 9a + 7c + 3e + 2g + 5i = 140
# 7a + 6c + 4e + 5g + 3i = 128
# 3a + 5c + 7e + 6g + 4i = 116
# 2a + 5c + 3e + 9g + 4i = 112
# 1a + 3c + 2e + 8g + 5i = 95

# Representing the system of equations as matrices
A = [
    [9, 7, 3, 2, 5],
    [7, 6, 4, 5, 3],
    [3, 5, 7, 6, 4],
    [2, 5, 3, 9, 4],
    [1, 3, 2, 8, 5]
]

B = [140, 128, 116, 112, 95]

# Solving the system of equations using Gaussian elimination
def gaussian_elimination(A, B):
    n = len(A)
    # Forward elimination
    for i in range(n):
        # Make the diagonal element 1
        diag = A[i][i]
        for j in range(i, n):
            A[i][j] = Fraction(A[i][j], diag)
        B[i] = Fraction(B[i], diag)
        
        # Make the elements below the diagonal 0
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

# Solve for the unknowns
solution = gaussian_elimination(A, B)

# Assign the solutions to the respective variables
a, c, e, g, i = solution

# Print the results
print(f"麻 (a): {a} 錢")
print(f"麥 (c): {c} 錢")
print(f"菽 (e): {e} 錢")
print(f"答 (g): {g} 錢")
print(f"黍 (i): {i} 錢")


"""


### Explanation:
1. The system of equations is represented as a matrix \( A \) (coefficients) and a vector \( B \) (constants).
2. Gaussian elimination is used to solve the system of linear equations. This involves forward elimination to create an upper triangular matrix and back substitution to find the solution.
3. The solutions are assigned to the variables \( a, c, e, g, i \), which represent the prices per斗 of the respective grains.

### Output:
The program will output the prices of each grain in terms of 錢 (money).
"""


"""
Variable 'a' has wrong value. Expected: 1, Actual: 7
Missing variable in output: 'b'
Variable 'c' has wrong value. Expected: 1, Actual: 4
Missing variable in output: 'd'
Variable 'e' has wrong value. Expected: 1, Actual: 3
Missing variable in output: 'f'
Variable 'g' has wrong value. Expected: 1, Actual: 5
Missing variable in output: 'h'
Variable 'i' has wrong value. Expected: 1, Actual: 6
Missing variable in output: 'j'"""
