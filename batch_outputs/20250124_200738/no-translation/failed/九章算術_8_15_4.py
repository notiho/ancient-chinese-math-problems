"""
今有令一人、吏五人、從者一十人，食雞一十；令一十人、吏一人、從者五人，食雞八；令五人、吏一十人、從者一人，食雞六。問︰令、吏、從者食雞各幾何？
術曰：如方程，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：令一人食 a雞 ，吏一人食 b雞 ，從者一人食 c雞 。
"""

"""
To solve this problem, we will use the ancient Chinese method of solving simultaneous linear equations, as described in the "方程術". The problem involves three equations with three unknowns, representing the amount of chicken eaten by a "令" (official), a "吏" (scribe), and a "從者" (attendant). Let's translate this into Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Define the coefficients of the equations
# Equation 1: 1令 + 5吏 + 10從者 = 10雞
# Equation 2: 10令 + 1吏 + 5從者 = 8雞
# Equation 3: 5令 + 10吏 + 1從者 = 6雞

# Coefficients matrix
A = [
    [1, 5, 10],
    [10, 1, 5],
    [5, 10, 1]
]

# Constants (right-hand side)
B = [10, 8, 6]

# Step 1: Eliminate the first variable (令) from the second and third equations
# Multiply the first row by 10 (to match the coefficient of 令 in the second equation)
# and subtract it from the second row
factor = Fraction(A[1][0], A[0][0])
A[1] = [A[1][i] - factor * A[0][i] for i in range(3)]
B[1] = B[1] - factor * B[0]

# Multiply the first row by 5 (to match the coefficient of 令 in the third equation)
# and subtract it from the third row
factor = Fraction(A[2][0], A[0][0])
A[2] = [A[2][i] - factor * A[0][i] for i in range(3)]
B[2] = B[2] - factor * B[0]

# Step 2: Eliminate the second variable (吏) from the third equation
# Multiply the second row by the appropriate factor and subtract it from the third row
factor = Fraction(A[2][1], A[1][1])
A[2] = [A[2][i] - factor * A[1][i] for i in range(3)]
B[2] = B[2] - factor * B[1]

# Step 3: Solve for the third variable (從者)
c = Fraction(B[2], A[2][2])

# Step 4: Solve for the second variable (吏)
b = Fraction(B[1] - A[1][2] * c, A[1][1])

# Step 5: Solve for the first variable (令)
a = Fraction(B[0] - A[0][1] * b - A[0][2] * c, A[0][0])

# Results
a = float(a)
b = float(b)
c = float(c)
#----- content ends here -----


"""


### Explanation:
1. **Matrix Representation**: The problem is represented as a system of linear equations.
2. **Elimination**: The "正負術" (elimination method) is used to reduce the system to a triangular form.
3. **Back Substitution**: Solve for the variables starting from the last equation.

### Answer:
- 令一人食 `a` 雞
- 吏一人食 `b` 雞
- 從者一人食 `c` 雞
"""


"""
Variable 'a' has wrong value. Expected: 45/122, Actual: 0.36885245901639346
Variable 'b' has wrong value. Expected: 41/122, Actual: 0.3360655737704918
Variable 'c' has wrong value. Expected: 97/122, Actual: 0.7950819672131147"""
