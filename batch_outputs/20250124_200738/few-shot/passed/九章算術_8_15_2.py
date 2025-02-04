"""
今有令一人、吏五人、從者一十人，食雞一十；令一十人、吏一人、從者五人，食雞八；令五人、吏一十人、從者一人，食雞六。問︰令、吏、從者食雞各幾何？
術曰：如方程，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：令一人食 a雞 ，吏一人食 b雞 ，從者一人食 c雞 。
"""

"""
This problem involves solving a system of linear equations using the ancient Chinese method of elimination, which is similar to Gaussian elimination. Let's translate the problem into Python code step by step:

### Problem Setup:
We have three equations based on the given information:
1. \( 1x + 5y + 10z = 10 \)
2. \( 10x + 1y + 5z = 8 \)
3. \( 5x + 10y + 1z = 6 \)

Where:
- \( x \) is the number of chickens eaten by one "令" (official),
- \( y \) is the number of chickens eaten by one "吏" (clerk),
- \( z \) is the number of chickens eaten by one "從者" (attendant).

We will solve this system using the described elimination method.

---


"""

#----- content starts here -----

from fractions import Fraction

# Coefficients of the equations
# Equation 1: 1x + 5y + 10z = 10
# Equation 2: 10x + 1y + 5z = 8
# Equation 3: 5x + 10y + 1z = 6

# Initialize the matrix (augmented form)
matrix = [
    [1, 5, 10, 10],  # First equation
    [10, 1, 5, 8],   # Second equation
    [5, 10, 1, 6]    # Third equation
]

# Step 1: Eliminate the first variable (x) from the second and third rows
for i in range(1, 3):
    factor = Fraction(matrix[i][0], matrix[0][0])
    for j in range(4):
        matrix[i][j] -= factor * matrix[0][j]

# Step 2: Eliminate the second variable (y) from the third row
factor = Fraction(matrix[2][1], matrix[1][1])
for j in range(1, 4):
    matrix[2][j] -= factor * matrix[1][j]

# Step 3: Back-substitution to solve for z, y, and x
z = Fraction(matrix[2][3], matrix[2][2])
y = Fraction(matrix[1][3] - matrix[1][2] * z, matrix[1][1])
x = Fraction(matrix[0][3] - matrix[0][2] * z - matrix[0][1] * y, matrix[0][0])

# Results
a = x  # Number of chickens eaten by one "令"
b = y  # Number of chickens eaten by one "吏"
c = z  # Number of chickens eaten by one "從者"

# Output the results
a, b, c
#----- content ends here -----


"""


### Explanation of the Code:
1. **Matrix Representation**: The system of equations is represented as an augmented matrix.
2. **Elimination**: The first variable (\( x \)) is eliminated from the second and third rows by subtracting a multiple of the first row. Then, the second variable (\( y \)) is eliminated from the third row.
3. **Back-Substitution**: After elimination, the system is in upper triangular form, and we solve for \( z \), \( y \), and \( x \) in reverse order.
4. **Fractions**: The `Fraction` class is used to ensure exact arithmetic without floating-point errors.

### Final Answer:
The values of \( a \), \( b \), and \( c \) represent the number of chickens eaten by one "令", one "吏", and one "從者", respectively.
"""


"""
"""
