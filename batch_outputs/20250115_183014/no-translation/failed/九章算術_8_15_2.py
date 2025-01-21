"""
今有令一人、吏五人、從者一十人，食雞一十；令一十人、吏一人、從者五人，食雞八；令五人、吏一十人、從者一人，食雞六。問︰令、吏、從者食雞各幾何？
術曰：如方程，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：令 a人 食 b雞 ，吏 c人 食 d雞 ，從者 e人 食 f雞 。
"""

"""
This problem involves solving a system of linear equations using the ancient Chinese method described in the "方程術" (method of solving simultaneous equations). Let's translate this into Python code step by step.

The problem gives us the following equations based on the number of people and the chickens they consume:

1. \( 1 \cdot \text{令} + 5 \cdot \text{吏} + 10 \cdot \text{從者} = 10 \) (Equation 1)
2. \( 10 \cdot \text{令} + 1 \cdot \text{吏} + 5 \cdot \text{從者} = 8 \) (Equation 2)
3. \( 5 \cdot \text{令} + 10 \cdot \text{吏} + 1 \cdot \text{從者} = 6 \) (Equation 3)

We will solve this system of equations using the method described.


"""


from fractions import Fraction

# Coefficients of the equations
# Equation 1: 1令 + 5吏 + 10從者 = 10
# Equation 2: 10令 + 1吏 + 5從者 = 8
# Equation 3: 5令 + 10吏 + 1從者 = 6

# Step 1: Represent the equations as a matrix
matrix = [
    [1, 5, 10, 10],  # Coefficients and constant term for Equation 1
    [10, 1, 5, 8],   # Coefficients and constant term for Equation 2
    [5, 10, 1, 6]    # Coefficients and constant term for Equation 3
]

# Step 2: Perform Gaussian elimination
# Normalize the first row
factor = matrix[0][0]
matrix[0] = [Fraction(x, factor) for x in matrix[0]]

# Eliminate the first variable from the second and third rows
for i in range(1, 3):
    factor = matrix[i][0]
    matrix[i] = [matrix[i][j] - factor * matrix[0][j] for j in range(4)]

# Normalize the second row
factor = matrix[1][1]
matrix[1] = [Fraction(x, factor) for x in matrix[1]]

# Eliminate the second variable from the third row
factor = matrix[2][1]
matrix[2] = [matrix[2][j] - factor * matrix[1][j] for j in range(4)]

# Normalize the third row
factor = matrix[2][2]
matrix[2] = [Fraction(x, factor) for x in matrix[2]]

# Step 3: Back substitution to find the solution
從者 = matrix[2][3]
吏 = matrix[1][3] - matrix[1][2] * 從者
令 = matrix[0][3] - matrix[0][2] * 從者 - matrix[0][1] * 吏

# Results
a = 令
b = 令
c = 吏
d = 吏
e = 從者
f = 從者

# Output the results
print(f"令 {a}人 食 {b}雞 ，吏 {c}人 食 {d}雞 ，從者 {e}人 食 {f}雞 。")


"""


This code follows the ancient Chinese method of solving simultaneous equations using elimination and back substitution. The results will give the number of chickens consumed by each type of person.
"""


"""
Variable 'a' has wrong value. Expected: 1, Actual: 45/122
Variable 'c' has wrong value. Expected: 1, Actual: 41/122
Variable 'e' has wrong value. Expected: 1, Actual: 97/122"""
