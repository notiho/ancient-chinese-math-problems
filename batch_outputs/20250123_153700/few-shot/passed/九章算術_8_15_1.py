"""
今有令一人、吏五人、從者一十人，食雞一十；令一十人、吏一人、從者五人，食雞八；令五人、吏一十人、從者一人，食雞六。問︰令、吏、從者食雞各幾何？
術曰：如方程，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：令一人食 a雞 ，吏一人食 b雞 ，從者一人食 c雞 。
"""

"""
This problem involves solving a system of linear equations using the ancient Chinese method of elimination, which is similar to Gaussian elimination. Let's translate the problem and solve it step by step in Python.

### Problem:
There are three groups of people:
1. One official ("令"), five clerks ("吏"), and ten attendants ("從者") eat 10 chickens.
2. Ten officials, one clerk, and five attendants eat 8 chickens.
3. Five officials, ten clerks, and one attendant eat 6 chickens.

We are tasked to find how many chickens each person in each category eats.

### Procedure:
The ancient Chinese method of solving systems of linear equations, as described in the "方程術" (method of elimination), involves systematically eliminating variables by multiplying rows and subtracting them, similar to modern Gaussian elimination.

### Translation into Python:


"""


from fractions import Fraction

# Coefficients of the equations
# Equation 1: 令 + 5吏 + 10從者 = 10
# Equation 2: 10令 + 吏 + 5從者 = 8
# Equation 3: 5令 + 10吏 + 從者 = 6

# Representing the system of equations as a matrix
# Each row is [令, 吏, 從者, constant]
matrix = [
    [1, 5, 10, 10],
    [10, 1, 5, 8],
    [5, 10, 1, 6]
]

# Step 1: Eliminate the first variable ("令") from the second and third rows
factor1 = Fraction(matrix[1][0], matrix[0][0])  # Factor to eliminate "令" from row 2
for i in range(4):
    matrix[1][i] -= factor1 * matrix[0][i]

factor2 = Fraction(matrix[2][0], matrix[0][0])  # Factor to eliminate "令" from row 3
for i in range(4):
    matrix[2][i] -= factor2 * matrix[0][i]

# Step 2: Eliminate the second variable ("吏") from the third row
factor3 = Fraction(matrix[2][1], matrix[1][1])  # Factor to eliminate "吏" from row 3
for i in range(4):
    matrix[2][i] -= factor3 * matrix[1][i]

# Step 3: Back-substitution to solve for the variables
# Solve for 從者 (c)
c = Fraction(matrix[2][3], matrix[2][2])

# Solve for 吏 (b)
b = Fraction(matrix[1][3] - matrix[1][2] * c, matrix[1][1])

# Solve for 令 (a)
a = Fraction(matrix[0][3] - matrix[0][1] * b - matrix[0][2] * c, matrix[0][0])

# Output the results
a, b, c


"""


### Explanation of the Code:
1. **Matrix Representation**: The system of equations is represented as a matrix where each row corresponds to an equation, and the last column represents the constants.
2. **Elimination**: The first variable ("令") is eliminated from the second and third rows by subtracting appropriate multiples of the first row. Then, the second variable ("吏") is eliminated from the third row.
3. **Back-Substitution**: After elimination, the system is in upper triangular form, allowing us to solve for the variables starting from the last row.
4. **Fractions**: The `Fraction` class is used to ensure exact arithmetic throughout the calculations.

### Answer:
The result will be:
- `a`: Number of chickens eaten by one official ("令").
- `b`: Number of chickens eaten by one clerk ("吏").
- `c`: Number of chickens eaten by one attendant ("從者").
"""


"""
"""
