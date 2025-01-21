"""
今有令一人、吏五人、從者一十人，食雞一十；令一十人、吏一人、從者五人，食雞八；令五人、吏一十人、從者一人，食雞六。問︰令、吏、從者食雞各幾何？
術曰：如方程，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：令 a人 食 b雞 ，吏 c人 食 d雞 ，從者 e人 食 f雞 。
"""

"""
This problem involves solving a system of linear equations using the ancient Chinese method of elimination, which is similar to Gaussian elimination. Let's translate the procedure into Python code step by step.

The problem can be represented as the following system of equations:

1. \( x + 5y + 10z = 10 \)  (Equation for the first scenario)
2. \( 10x + y + 5z = 8 \)   (Equation for the second scenario)
3. \( 5x + 10y + z = 6 \)   (Equation for the third scenario)

Where:
- \( x \) represents the number of chickens eaten by one "令" (leader),
- \( y \) represents the number of chickens eaten by one "吏" (official),
- \( z \) represents the number of chickens eaten by one "從者" (attendant).

Now, let's solve this step by step using the described method.


"""


from fractions import Fraction

# Coefficients of the equations
# First equation: x + 5y + 10z = 10
# Second equation: 10x + y + 5z = 8
# Third equation: 5x + 10y + z = 6

# Initial matrix representation of the system
matrix = [
    [1, 5, 10, 10],  # Coefficients and constant term of the first equation
    [10, 1, 5, 8],   # Coefficients and constant term of the second equation
    [5, 10, 1, 6]    # Coefficients and constant term of the third equation
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

# Step 3: Back substitution to solve for z, y, and x
z = Fraction(matrix[2][3], matrix[2][2])
y = Fraction(matrix[1][3] - matrix[1][2] * z, matrix[1][1])
x = Fraction(matrix[0][3] - matrix[0][2] * z - matrix[0][1] * y, matrix[0][0])

# Results
a = 1  # Number of "令" (leaders)
b = x  # Chickens eaten by one "令"

c = 1  # Number of "吏" (officials)
d = y  # Chickens eaten by one "吏"

e = 1  # Number of "從者" (attendants)
f = z  # Chickens eaten by one "從者"

# Output results
a, b, c, d, e, f


"""


This code solves the system of equations step by step using the described ancient Chinese elimination method. The results \( b \), \( d \), and \( f \) represent the number of chickens eaten by one "令", one "吏", and one "從者", respectively.
"""


"""
"""
