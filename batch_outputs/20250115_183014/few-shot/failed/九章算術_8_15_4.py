"""
今有令一人、吏五人、從者一十人，食雞一十；令一十人、吏一人、從者五人，食雞八；令五人、吏一十人、從者一人，食雞六。問︰令、吏、從者食雞各幾何？
術曰：如方程，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：令 a人 食 b雞 ，吏 c人 食 d雞 ，從者 e人 食 f雞 。
"""

"""
This problem involves solving a system of linear equations using the ancient Chinese method of elimination, which is similar to Gaussian elimination. Let's break it down step by step and translate it into Python code.

### Problem Setup:
We are given three equations:
1. One Ling (令), five Li (吏), and ten Congzhe (從者) eat 10 chickens.
2. Ten Ling, one Li, and five Congzhe eat 8 chickens.
3. Five Ling, ten Li, and one Congzhe eat 6 chickens.

We need to determine how many chickens each Ling, Li, and Congzhe eats.

### Procedure:
The ancient Chinese method of elimination (方程術) is described, which involves systematically eliminating variables to solve for the unknowns. This is equivalent to solving a system of linear equations.

---


"""


from fractions import Fraction

# Coefficients of the equations
# Equation 1: 1令 + 5吏 + 10從者 = 10
# Equation 2: 10令 + 1吏 + 5從者 = 8
# Equation 3: 5令 + 10吏 + 1從者 = 6

# Representing the equations as a matrix
# Each row is [令, 吏, 從者, total]
matrix = [
    [1, 5, 10, 10],
    [10, 1, 5, 8],
    [5, 10, 1, 6]
]

# Step 1: Eliminate the first variable (令) from the second and third rows
for i in range(1, 3):
    factor = Fraction(matrix[i][0], matrix[0][0])
    for j in range(4):
        matrix[i][j] -= factor * matrix[0][j]

# Step 2: Eliminate the second variable (吏) from the third row
factor = Fraction(matrix[2][1], matrix[1][1])
for j in range(1, 4):
    matrix[2][j] -= factor * matrix[1][j]

# Step 3: Back-substitution to solve for 從者, 吏, and 令
# Solve for 從者 (third variable)
從者 = Fraction(matrix[2][3], matrix[2][2])

# Solve for 吏 (second variable)
吏 = Fraction(matrix[1][3] - matrix[1][2] * 從者, matrix[1][1])

# Solve for 令 (first variable)
令 = Fraction(matrix[0][3] - matrix[0][1] * 吏 - matrix[0][2] * 從者, matrix[0][0])

# Results
a = 令
b = 令 * 1  # Number of chickens eaten by one Ling
c = 吏
d = 吏 * 1  # Number of chickens eaten by one Li
e = 從者
f = 從者 * 1  # Number of chickens eaten by one Congzhe

print(f"令 {a}人 食 {b}雞 ，吏 {c}人 食 {d}雞 ，從者 {e}人 食 {f}雞 。")


"""


### Explanation of the Code:
1. **Matrix Representation**: The system of equations is represented as a matrix, where each row corresponds to an equation, and the last column is the total (number of chickens).
2. **Elimination**: The first variable (令) is eliminated from the second and third rows, and then the second variable (吏) is eliminated from the third row.
3. **Back-Substitution**: The values of 從者, 吏, and 令 are calculated by substituting back into the equations.
4. **Results**: The values of a, b, c, d, e, and f are printed, representing the number of people and chickens for each role.

### Output:
The output will display the number of chickens eaten by each Ling, Li, and Congzhe.
"""


"""
Variable 'a' has wrong value. Expected: 1, Actual: 45/122
Variable 'c' has wrong value. Expected: 1, Actual: 41/122
Variable 'e' has wrong value. Expected: 1, Actual: 97/122"""
