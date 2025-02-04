"""
今有令一人、吏五人、從者一十人，食雞一十；令一十人、吏一人、從者五人，食雞八；令五人、吏一十人、從者一人，食雞六。問︰令、吏、從者食雞各幾何？
術曰：如方程，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：令一人食 a雞 ，吏一人食 b雞 ，從者一人食 c雞 。
"""

"""
This problem involves solving a system of linear equations using the ancient Chinese method of elimination, which is similar to Gaussian elimination. Let's translate the problem into Python code step by step.

### Problem Description:
We are given three equations:
1. One ling (令), five li (吏), and ten congzhe (從者) eat 10 chickens.
2. Ten ling, one li, and five congzhe eat 8 chickens.
3. Five ling, ten li, and one congzhe eat 6 chickens.

We need to determine how many chickens each ling, li, and congzhe eats.

### Procedure:
The ancient Chinese method of solving linear equations (方程術) involves systematically eliminating variables by multiplying rows and subtracting them, similar to modern Gaussian elimination.

### Python Code:


"""


from fractions import Fraction

# Coefficients of the equations
# Equation 1: 令 + 5吏 + 10從者 = 10
# Equation 2: 10令 + 吏 + 5從者 = 8
# Equation 3: 5令 + 10吏 + 從者 = 6

# Representing the system of equations as a matrix
# Each row is [令, 吏, 從者, constant]
matrix = [
    [1, 5, 10, 10],  # Equation 1
    [10, 1, 5, 8],   # Equation 2
    [5, 10, 1, 6]    # Equation 3
]

# Step 1: Eliminate the first variable (令) from the second and third equations
# Multiply the first row by 10 (to match the coefficient of 令 in the second row)
# and subtract it from the second row
factor = matrix[1][0] / matrix[0][0]
matrix[1] = [matrix[1][i] - factor * matrix[0][i] for i in range(4)]

# Multiply the first row by 5 (to match the coefficient of 令 in the third row)
# and subtract it from the third row
factor = matrix[2][0] / matrix[0][0]
matrix[2] = [matrix[2][i] - factor * matrix[0][i] for i in range(4)]

# Step 2: Eliminate the second variable (吏) from the third equation
# Multiply the second row by the appropriate factor to match the coefficient of 吏 in the third row
factor = matrix[2][1] / matrix[1][1]
matrix[2] = [matrix[2][i] - factor * matrix[1][i] for i in range(4)]

# Step 3: Back-substitution to solve for 從者 (c), 吏 (b), and 令 (a)
# Solve for 從者 (c) from the third equation
c = Fraction(matrix[2][3], matrix[2][2])

# Solve for 吏 (b) from the second equation
b = Fraction(matrix[1][3] - matrix[1][2] * c, matrix[1][1])

# Solve for 令 (a) from the first equation
a = Fraction(matrix[0][3] - matrix[0][1] * b - matrix[0][2] * c, matrix[0][0])

# Output the results
a, b, c


"""


### Explanation:
1. **Matrix Representation**: The system of equations is represented as a matrix where each row corresponds to an equation, and the last column represents the constants.
2. **Elimination**: The first variable (令) is eliminated from the second and third equations by subtracting appropriate multiples of the first row.
3. **Back-Substitution**: After elimination, the system is solved from the bottom up, starting with the third equation to find 從者 (c), then using the second equation to find 吏 (b), and finally using the first equation to find 令 (a).

### Answer:
The solution will give the number of chickens each ling (令), li (吏), and congzhe (從者) eats:
- 令一人食 `a` 雞
- 吏一人食 `b` 雞
- 從者一人食 `c` 雞
"""


"""
Code error: both arguments should be Rational instances"""
