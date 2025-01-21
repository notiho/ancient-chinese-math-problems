"""
今有令一人、吏五人、從者一十人，食雞一十；令一十人、吏一人、從者五人，食雞八；令五人、吏一十人、從者一人，食雞六。問︰令、吏、從者食雞各幾何？
術曰：如方程，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：令 a(=1)人 食 b(=45/122)雞 ，吏 c(=1)人 食 d(=41/122)雞 ，從者 e(=1)人 食 f(=97/122)雞 。
"""

"""
This problem involves solving a system of linear equations using ancient Chinese methods, specifically the "fangcheng" (方程) procedure, which is equivalent to solving simultaneous equations. The problem provides the consumption of chickens by three groups of people (officials, clerks, and attendants) under different scenarios, and the goal is to determine how much chicken each type of person consumes.

The procedure described in the problem is a step-by-step elimination method, similar to Gaussian elimination. Below is the Python implementation of the solution:


"""


from fractions import Fraction

# Define the equations based on the problem:
# Let x = chicken consumption by one official (令)
# Let y = chicken consumption by one clerk (吏)
# Let z = chicken consumption by one attendant (從者)
# The equations are:
# 1x + 5y + 10z = 10
# 10x + 1y + 5z = 8
# 5x + 10y + 1z = 6

# Coefficients of the equations
matrix = [
    [1, 5, 10, 10],  # 1x + 5y + 10z = 10
    [10, 1, 5, 8],   # 10x + 1y + 5z = 8
    [5, 10, 1, 6]    # 5x + 10y + 1z = 6
]

# Step 1: Eliminate x from the second and third equations
factor1 = Fraction(matrix[1][0], matrix[0][0])
factor2 = Fraction(matrix[2][0], matrix[0][0])

for i in range(4):
    matrix[1][i] -= factor1 * matrix[0][i]
    matrix[2][i] -= factor2 * matrix[0][i]

# Step 2: Eliminate y from the third equation
factor3 = Fraction(matrix[2][1], matrix[1][1])

for i in range(4):
    matrix[2][i] -= factor3 * matrix[1][i]

# Step 3: Solve for z, y, and x
z = Fraction(matrix[2][3], matrix[2][2])
y = Fraction(matrix[1][3] - matrix[1][2] * z, matrix[1][1])
x = Fraction(matrix[0][3] - matrix[0][2] * z - matrix[0][1] * y, matrix[0][0])

# Results
a = 1  # One official
b = x  # Chicken consumption by one official
c = 1  # One clerk
d = y  # Chicken consumption by one clerk
e = 1  # One attendant
f = z  # Chicken consumption by one attendant

# Output results
a, b, c, d, e, f  # (1, 45/122, 1, 41/122, 1, 97/122)


"""


### Explanation of the Code:
1. **Matrix Representation**: The problem is represented as a system of linear equations in matrix form.
2. **Elimination Process**: The coefficients are manipulated to eliminate variables step by step, following the "fangcheng" procedure.
3. **Back Substitution**: After elimination, the values of `z`, `y`, and `x` are calculated in reverse order.
4. **Results**: The consumption of chickens by each type of person is expressed as fractions.

### Final Answer:
- One official (令) consumes **45/122** chickens.
- One clerk (吏) consumes **41/122** chickens.
- One attendant (從者) consumes **97/122** chickens.
"""


"""
"""
