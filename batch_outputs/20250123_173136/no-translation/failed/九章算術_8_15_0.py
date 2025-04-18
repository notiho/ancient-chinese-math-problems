"""
今有令一人、吏五人、從者一十人，食雞一十；令一十人、吏一人、從者五人，食雞八；令五人、吏一十人、從者一人，食雞六。問︰令、吏、從者食雞各幾何？
術曰：如方程，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：令一人食 a雞 ，吏一人食 b雞 ，從者一人食 c雞 。
"""

"""
To solve this problem, we need to use a system of linear equations based on the given data. The problem describes three equations with three unknowns: the amount of chicken eaten by one "令" (denoted as `a`), one "吏" (denoted as `b`), and one "從者" (denoted as `c`). Here's how we can translate the ancient Chinese method into Python code:


"""


from fractions import Fraction

# Define the equations based on the problem:
# 1令 + 5吏 + 10從者 = 10雞
# 10令 + 1吏 + 5從者 = 8雞
# 5令 + 10吏 + 1從者 = 6雞

# Coefficients of the equations
A = [
    [1, 5, 10],  # Coefficients for the first equation
    [10, 1, 5],  # Coefficients for the second equation
    [5, 10, 1]   # Coefficients for the third equation
]

# Constants on the right-hand side
B = [10, 8, 6]

# Step 1: Eliminate the first variable (令) from the second and third equations
factor1 = Fraction(A[1][0], A[0][0])
factor2 = Fraction(A[2][0], A[0][0])

for i in range(3):
    A[1][i] -= factor1 * A[0][i]
    A[2][i] -= factor2 * A[0][i]

B[1] -= factor1 * B[0]
B[2] -= factor2 * B[0]

# Step 2: Eliminate the second variable (吏) from the third equation
factor3 = Fraction(A[2][1], A[1][1])

for i in range(3):
    A[2][i] -= factor3 * A[1][i]

B[2] -= factor3 * B[1]

# Step 3: Solve for the variables
c = Fraction(B[2], A[2][2])  # Solve for 從者 (c)
b = Fraction(B[1] - A[1][2] * c, A[1][1])  # Solve for 吏 (b)
a = Fraction(B[0] - A[0][1] * b - A[0][2] * c, A[0][0])  # Solve for 令 (a)

# Results
a = float(a)
b = float(b)
c = float(c)

print(f"令一人食 {a} 雞，吏一人食 {b} 雞，從者一人食 {c} 雞。")


"""


### Explanation of the Code:
1. **Define the System of Equations**: The coefficients of the equations are stored in a matrix `A`, and the constants on the right-hand side are stored in a list `B`.
2. **Gaussian Elimination**: The ancient Chinese method described is essentially Gaussian elimination. We eliminate variables step by step to reduce the system to a triangular form.
3. **Back Substitution**: Once the system is in triangular form, we solve for the variables starting from the last equation.
4. **Fractions**: The `Fraction` class is used to ensure exact arithmetic, as required by the problem.

### Final Answer:
The values of `a`, `b`, and `c` represent the amount of chicken eaten by one "令", one "吏", and one "從者", respectively.
"""


"""
Variable 'a' has wrong value. Expected: 45/122, Actual: 0.36885245901639346
Variable 'b' has wrong value. Expected: 41/122, Actual: 0.3360655737704918
Variable 'c' has wrong value. Expected: 97/122, Actual: 0.7950819672131147"""
