"""
今有令一人、吏五人、從者一十人，食雞一十；令一十人、吏一人、從者五人，食雞八；令五人、吏一十人、從者一人，食雞六。問︰令、吏、從者食雞各幾何？
術曰：如方程，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：令 a(=1)人 食 b(=45/122)雞 ，吏 c(=1)人 食 d(=41/122)雞 ，從者 e(=1)人 食 f(=97/122)雞 。
"""

"""
This problem involves solving a system of linear equations using ancient Chinese methods, which are conceptually similar to Gaussian elimination. Let's break it down and solve it step by step.

### Problem Description:
We are given three equations:
1. One Ling (令), five Officials (吏), and ten Attendants (從者) eat 10 chickens.
2. Ten Ling, one Official, and five Attendants eat 8 chickens.
3. Five Ling, ten Officials, and one Attendant eat 6 chickens.

We need to determine how many chickens each type of person eats.

### Procedure:
The method described in the problem is the ancient Chinese "fangcheng" (方程) method, which is equivalent to solving a system of linear equations. The steps involve setting up a matrix, performing row operations, and solving for the unknowns.

### Solution in Python:


"""


from fractions import Fraction

# Coefficients of the equations
# Equation 1: 1令 + 5吏 + 10從者 = 10
# Equation 2: 10令 + 1吏 + 5從者 = 8
# Equation 3: 5令 + 10吏 + 1從者 = 6

# Initial matrix representation of the equations
# Each row is [令, 吏, 從者, total_chickens]
matrix = [
    [1, 5, 10, 10],
    [10, 1, 5, 8],
    [5, 10, 1, 6]
]

# Step 1: Normalize the first row (make the leading coefficient 1)
factor = matrix[0][0]
matrix[0] = [Fraction(x, factor) for x in matrix[0]]

# Step 2: Eliminate the first variable (令) from the second and third rows
for i in range(1, 3):
    factor = matrix[i][0]
    matrix[i] = [matrix[i][j] - factor * matrix[0][j] for j in range(4)]

# Step 3: Normalize the second row (make the leading coefficient of 吏 1)
factor = matrix[1][1]
matrix[1] = [Fraction(x, factor) for x in matrix[1]]

# Step 4: Eliminate the second variable (吏) from the first and third rows
for i in [0, 2]:
    factor = matrix[i][1]
    matrix[i] = [matrix[i][j] - factor * matrix[1][j] for j in range(4)]

# Step 5: Normalize the third row (make the leading coefficient of 從者 1)
factor = matrix[2][2]
matrix[2] = [Fraction(x, factor) for x in matrix[2]]

# Step 6: Eliminate the third variable (從者) from the first and second rows
for i in [0, 1]:
    factor = matrix[i][2]
    matrix[i] = [matrix[i][j] - factor * matrix[2][j] for j in range(4)]

# The matrix is now in reduced row echelon form, and we can read off the solutions
令 = matrix[0][3]  # a
吏 = matrix[1][3]  # c
從者 = matrix[2][3]  # e

# Output the results
a = 1  # 令 per person
b = 令  # Chickens eaten by 1令
c = 1  # 吏 per person
d = 吏  # Chickens eaten by 1吏
e = 1  # 從者 per person
f = 從者  # Chickens eaten by 1從者

# Results
print(f"令 a(={a})人 食 b(={b})雞")
print(f"吏 c(={c})人 食 d(={d})雞")
print(f"從者 e(={e})人 食 f(={f})雞")


"""


### Explanation of Results:
After solving the system of equations, we find:
- Each Ling (令) eats **45/122** chickens.
- Each Official (吏) eats **41/122** chickens.
- Each Attendant (從者) eats **97/122** chickens.

These results match the expected answers provided in the problem.
"""


"""
"""
