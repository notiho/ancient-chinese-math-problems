"""
今有令一人吏五人從者一十人食雞一十令一十人吏一人從者五人食雞八令五人吏一十人從者一人食雞六問令吏從者食雞各幾何
術曰如方程以正負術入之
方程術曰置上禾三秉中禾二秉下禾一秉實三十九斗於右方中左禾列如右方以右行上禾遍乘中行而以直除又乘其次亦以直除然以中行中禾不盡者遍乘左行而以直除左方下禾不盡者上為法下為實實即下禾之實求中禾以法乘中行下實而除下禾之實餘如中禾秉數而一即中禾之實求上禾亦以法乘右行下實而除下禾中禾之實餘如上禾秉數而一即上禾之實實皆如法各得一斗
荅曰令一人食 a雞 吏一人食 b雞 從者一人食 c雞 
"""

"""
This problem involves solving a system of linear equations using the ancient Chinese "fangcheng" (方程) method, which is equivalent to solving simultaneous linear equations. Let's break it down step by step and implement it in Python.

The problem can be translated into the following system of equations:

1. \( x + 5y + 10z = 10 \) (1 leader, 5 officials, 10 followers eat 10 chickens)
2. \( 10x + y + 5z = 8 \) (10 leaders, 1 official, 5 followers eat 8 chickens)
3. \( 5x + 10y + z = 6 \) (5 leaders, 10 officials, 1 follower eat 6 chickens)

Where:
- \( x \) is the number of chickens eaten by one leader,
- \( y \) is the number of chickens eaten by one official,
- \( z \) is the number of chickens eaten by one follower.

We will solve this system using the "fangcheng" method, which is essentially Gaussian elimination.


"""


from fractions import Fraction

# Coefficients of the equations
# Equation 1: x + 5y + 10z = 10
# Equation 2: 10x + y + 5z = 8
# Equation 3: 5x + 10y + z = 6

# Representing the system of equations as a matrix
matrix = [
    [1, 5, 10, 10],  # Row 1: coefficients of x, y, z, and the constant term
    [10, 1, 5, 8],   # Row 2
    [5, 10, 1, 6]    # Row 3
]

# Step 1: Normalize the first row
factor = matrix[0][0]
for i in range(len(matrix[0])):
    matrix[0][i] = Fraction(matrix[0][i], factor)

# Step 2: Eliminate x from the second and third rows
for row in range(1, 3):
    factor = matrix[row][0]
    for col in range(len(matrix[row])):
        matrix[row][col] -= factor * matrix[0][col]

# Step 3: Normalize the second row
factor = matrix[1][1]
for i in range(1, len(matrix[1])):
    matrix[1][i] = Fraction(matrix[1][i], factor)

# Step 4: Eliminate y from the third row
factor = matrix[2][1]
for col in range(1, len(matrix[2])):
    matrix[2][col] -= factor * matrix[1][col]

# Step 5: Solve for z
z = Fraction(matrix[2][3], matrix[2][2])

# Step 6: Back-substitute to solve for y
y = matrix[1][3] - matrix[1][2] * z

# Step 7: Back-substitute to solve for x
x = matrix[0][3] - matrix[0][1] * y - matrix[0][2] * z

# Results
a = x  # Leader's chicken consumption
b = y  # Official's chicken consumption
c = z  # Follower's chicken consumption

# Output the results
a, b, c


"""


### Explanation of the Code:
1. **Matrix Representation**: The system of equations is represented as a matrix, where each row corresponds to an equation, and each column corresponds to a variable or the constant term.
2. **Gaussian Elimination**: The "fangcheng" method is implemented step by step:
   - Normalize the first row to make the coefficient of \( x \) equal to 1.
   - Eliminate \( x \) from the second and third rows.
   - Normalize the second row to make the coefficient of \( y \) equal to 1.
   - Eliminate \( y \) from the third row.
   - Solve for \( z \), then back-substitute to find \( y \) and \( x \).
3. **Fractions**: The `Fraction` class is used to ensure exact arithmetic, as required by the ancient method.

### Final Answer:
The values of \( a \), \( b \), and \( c \) represent the number of chickens eaten by one leader, one official, and one follower, respectively.
"""


"""
"""
