"""
今有令一人、吏五人、從者一十人，食雞一十；令一十人、吏一人、從者五人，食雞八；令五人、吏一十人、從者一人，食雞六。問︰令、吏、從者食雞各幾何？
術曰：如方程，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：令 a人 食 b雞 ，吏 c人 食 d雞 ，從者 e人 食 f雞 。
"""

"""
This problem involves solving a system of linear equations using the ancient Chinese method of elimination, which is similar to Gaussian elimination. The problem can be translated into Python code as follows:


"""


from fractions import Fraction

# Define the coefficients of the equations
# Equation 1: 令1人 + 吏5人 + 從者10人 = 10雞
# Equation 2: 令10人 + 吏1人 + 從者5人 = 8雞
# Equation 3: 令5人 + 吏10人 + 從者1人 = 6雞

# Coefficients matrix
A = [
    [1, 5, 10],
    [10, 1, 5],
    [5, 10, 1]
]

# Constants (right-hand side)
B = [10, 8, 6]

# Step 1: Elimination to make the matrix upper triangular
for i in range(len(A)):
    # Normalize the current row
    factor = A[i][i]
    for j in range(len(A[i])):
        A[i][j] = Fraction(A[i][j], factor)
    B[i] = Fraction(B[i], factor)
    
    # Eliminate the current variable from subsequent rows
    for k in range(i + 1, len(A)):
        factor = A[k][i]
        for j in range(len(A[k])):
            A[k][j] -= factor * A[i][j]
        B[k] -= factor * B[i]

# Step 2: Back substitution to solve for the variables
X = [0] * len(A)
for i in range(len(A) - 1, -1, -1):
    X[i] = B[i]
    for j in range(i + 1, len(A)):
        X[i] -= A[i][j] * X[j]

# Results
a = 1  # Number of 令
b = X[0]  # Chickens eaten by 令
c = 5  # Number of 吏
d = X[1]  # Chickens eaten by 吏
e = 10  # Number of 從者
f = X[2]  # Chickens eaten by 從者

# Output results
print(f"令 {a}人 食 {b}雞 ，吏 {c}人 食 {d}雞 ，從者 {e}人 食 {f}雞 。")


"""


### Explanation of the Code:
1. **Matrix Representation**: The problem is represented as a system of linear equations. The coefficients of the variables (令, 吏, 從者) are stored in matrix `A`, and the constants (total chickens eaten) are stored in vector `B`.

2. **Gaussian Elimination**: The matrix is transformed into an upper triangular form by normalizing rows and eliminating variables from subsequent rows.

3. **Back Substitution**: Once the matrix is in upper triangular form, the solution is found by substituting values back into the equations.

4. **Results**: The solution gives the number of chickens eaten per person for 令, 吏, and 從者.

This code adheres to the ancient Chinese method described in the problem, using elimination and substitution to solve the system of equations.
"""


"""
Variable 'c' has wrong value. Expected: 1, Actual: 5
Variable 'e' has wrong value. Expected: 1, Actual: 10"""
