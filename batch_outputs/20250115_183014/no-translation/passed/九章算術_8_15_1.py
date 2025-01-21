"""
今有令一人、吏五人、從者一十人，食雞一十；令一十人、吏一人、從者五人，食雞八；令五人、吏一十人、從者一人，食雞六。問︰令、吏、從者食雞各幾何？
術曰：如方程，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：令 a人 食 b雞 ，吏 c人 食 d雞 ，從者 e人 食 f雞 。
"""

"""
To solve this problem, we need to translate the ancient Chinese method of solving simultaneous equations into Python code. The problem involves three equations with three unknowns, which can be solved using the described "正負術" (method of elimination). Here's the Python implementation:


"""


from fractions import Fraction

# Define the equations based on the problem:
# Let x = number of chickens eaten by one "令"
# Let y = number of chickens eaten by one "吏"
# Let z = number of chickens eaten by one "從者"

# Equation 1: 1x + 5y + 10z = 10
# Equation 2: 10x + 1y + 5z = 8
# Equation 3: 5x + 10y + 1z = 6

# Coefficients of the equations
A = [
    [1, 5, 10],
    [10, 1, 5],
    [5, 10, 1]
]

# Constants on the right-hand side
B = [10, 8, 6]

# Step 1: Eliminate the first variable (x) from the second and third equations
factor1 = Fraction(A[1][0], A[0][0])
factor2 = Fraction(A[2][0], A[0][0])

for j in range(3):
    A[1][j] -= factor1 * A[0][j]
    A[2][j] -= factor2 * A[0][j]

B[1] -= factor1 * B[0]
B[2] -= factor2 * B[0]

# Step 2: Eliminate the second variable (y) from the third equation
factor3 = Fraction(A[2][1], A[1][1])

for j in range(1, 3):
    A[2][j] -= factor3 * A[1][j]

B[2] -= factor3 * B[1]

# Step 3: Solve for z, y, and x
z = Fraction(B[2], A[2][2])
y = Fraction(B[1] - A[1][2] * z, A[1][1])
x = Fraction(B[0] - A[0][1] * y - A[0][2] * z, A[0][0])

# Results
a = 1  # Number of "令"
b = x  # Chickens eaten by one "令"
c = 1  # Number of "吏"
d = y  # Chickens eaten by one "吏"
e = 1  # Number of "從者"
f = z  # Chickens eaten by one "從者"

# Output
print(f"令 {a}人 食 {b}雞 ，吏 {c}人 食 {d}雞 ，從者 {e}人 食 {f}雞 。")


"""


### Explanation of the Code:
1. **Define the equations**: The coefficients of the variables (令, 吏, 從者) and the constants on the right-hand side are stored in matrices `A` and `B`.
2. **Elimination process**: The elimination method described in the problem is implemented step by step:
   - Eliminate the first variable (`x`) from the second and third equations.
   - Eliminate the second variable (`y`) from the third equation.
3. **Back-substitution**: Solve for `z`, then `y`, and finally `x` using the simplified equations.
4. **Output the results**: The solution is printed in the required format.

This code adheres to the ancient Chinese method of solving simultaneous equations and provides the solution for the problem.
"""


"""
"""
