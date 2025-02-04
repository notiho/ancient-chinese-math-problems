"""
今有令一人、吏五人、從者一十人，食雞一十；令一十人、吏一人、從者五人，食雞八；令五人、吏一十人、從者一人，食雞六。問︰令、吏、從者食雞各幾何？
術曰：如方程，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：令一人食 a雞 ，吏一人食 b雞 ，從者一人食 c雞 。
"""

"""
To solve this problem using the described "方程術" (method of solving simultaneous equations), we will translate the procedure into Python code step by step. The problem involves three equations with three unknowns, which can be solved systematically.

The equations are:
1. \( x + 5y + 10z = 10 \)  (令一人, 吏五人, 從者十人 eat 10 chickens)
2. \( 10x + y + 5z = 8 \)   (令十人, 吏一人, 從者五人 eat 8 chickens)
3. \( 5x + 10y + z = 6 \)   (令五人, 吏十人, 從者一人 eat 6 chickens)

Where:
- \( x \) is the number of chickens eaten by one 令 (official),
- \( y \) is the number of chickens eaten by one 吏 (clerk),
- \( z \) is the number of chickens eaten by one 從者 (attendant).

Here is the Python code:


"""


from fractions import Fraction

# Coefficients of the equations
# Equation 1: x + 5y + 10z = 10
# Equation 2: 10x + y + 5z = 8
# Equation 3: 5x + 10y + z = 6

# Step 1: Represent the equations as a matrix
A = [
    [1, 5, 10],  # Coefficients of x, y, z in equation 1
    [10, 1, 5],  # Coefficients of x, y, z in equation 2
    [5, 10, 1]   # Coefficients of x, y, z in equation 3
]
B = [10, 8, 6]  # Constants on the right-hand side

# Step 2: Eliminate variables using the 方程術 (Gaussian elimination)

# Normalize the first row
factor = A[0][0]
A[0] = [Fraction(A[0][i], factor) for i in range(3)]
B[0] = Fraction(B[0], factor)

# Eliminate x from the second and third rows
factor = A[1][0]
A[1] = [A[1][i] - factor * A[0][i] for i in range(3)]
B[1] = B[1] - factor * B[0]

factor = A[2][0]
A[2] = [A[2][i] - factor * A[0][i] for i in range(3)]
B[2] = B[2] - factor * B[0]

# Normalize the second row
factor = A[1][1]
A[1] = [Fraction(A[1][i], factor) for i in range(3)]
B[1] = Fraction(B[1], factor)

# Eliminate y from the third row
factor = A[2][1]
A[2] = [A[2][i] - factor * A[1][i] for i in range(3)]
B[2] = B[2] - factor * B[1]

# Normalize the third row
factor = A[2][2]
A[2] = [Fraction(A[2][i], factor) for i in range(3)]
B[2] = Fraction(B[2], factor)

# Step 3: Back-substitute to find the values of x, y, z
z = B[2]
y = B[1] - A[1][2] * z
x = B[0] - A[0][1] * y - A[0][2] * z

# Results
a = x  # Number of chickens eaten by one 令
b = y  # Number of chickens eaten by one 吏
c = z  # Number of chickens eaten by one 從者

# Output the results
a, b, c


"""


### Explanation:
1. The equations are represented as a matrix \( A \) for the coefficients and a vector \( B \) for the constants.
2. Gaussian elimination is applied to reduce the matrix to row-echelon form.
3. Back-substitution is used to solve for \( x \), \( y \), and \( z \).
4. The results \( a \), \( b \), and \( c \) represent the number of chickens eaten by one 令, 吏, and 從者, respectively.
"""


"""
"""
