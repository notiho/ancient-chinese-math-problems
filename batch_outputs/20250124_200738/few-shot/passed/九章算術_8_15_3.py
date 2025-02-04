"""
今有令一人、吏五人、從者一十人，食雞一十；令一十人、吏一人、從者五人，食雞八；令五人、吏一十人、從者一人，食雞六。問︰令、吏、從者食雞各幾何？
術曰：如方程，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：令一人食 a雞 ，吏一人食 b雞 ，從者一人食 c雞 。
"""

"""
This problem involves solving a system of linear equations using the ancient Chinese method of elimination, as described in the "方程術" (method of solving simultaneous equations). Below is the Python implementation of the solution:


"""

#----- content starts here -----

from fractions import Fraction

# Define the equations based on the problem:
# Let x = number of chickens eaten by one "令" (official)
# Let y = number of chickens eaten by one "吏" (clerk)
# Let z = number of chickens eaten by one "從者" (attendant)

# Equations:
# 1x + 5y + 10z = 10
# 10x + 1y + 5z = 8
# 5x + 10y + 1z = 6

# Step 1: Represent the equations as a matrix
# Each row corresponds to an equation: [coefficient of x, coefficient of y, coefficient of z, constant term]
matrix = [
    [1, 5, 10, 10],  # 1x + 5y + 10z = 10
    [10, 1, 5, 8],   # 10x + 1y + 5z = 8
    [5, 10, 1, 6]    # 5x + 10y + 1z = 6
]

# Step 2: Perform Gaussian elimination (similar to the "正負術" described in the text)
# Eliminate the first variable (x) from the second and third equations
for i in range(1, 3):
    factor = Fraction(matrix[i][0], matrix[0][0])
    for j in range(4):
        matrix[i][j] -= factor * matrix[0][j]

# Eliminate the second variable (y) from the third equation
factor = Fraction(matrix[2][1], matrix[1][1])
for j in range(4):
    matrix[2][j] -= factor * matrix[1][j]

# Step 3: Back-substitution to solve for z, y, and x
# Solve for z
z = Fraction(matrix[2][3], matrix[2][2])

# Solve for y
y = Fraction(matrix[1][3] - matrix[1][2] * z, matrix[1][1])

# Solve for x
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
1. **Matrix Representation**: The system of equations is represented as a matrix where each row corresponds to an equation.
2. **Gaussian Elimination**: The process of elimination is used to reduce the matrix to an upper triangular form, as described in the "方程術".
3. **Back-Substitution**: Once the matrix is in upper triangular form, the values of the variables are solved starting from the last equation.
4. **Fractions**: The `Fraction` class is used to ensure exact arithmetic, as required by the problem.

### Final Answer:
- 令一人食 \( a \) 雞
- 吏一人食 \( b \) 雞
- 從者一人食 \( c \) 雞
"""


"""
"""
