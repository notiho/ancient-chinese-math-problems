"""
今有武馬一匹，中馬二匹，下馬三匹，皆載四十石至阪，皆不能上。武馬借中馬一匹，中馬借下馬一匹，下馬借武馬一匹，乃皆上。問︰武、中、下馬一匹各力引幾何？
術曰：如方程各置所借，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：武馬 a匹 力引 b石 ，中馬 c匹 力引 d石 ，下馬 e匹 力引 f石 。
"""

"""
This problem involves solving a system of linear equations using ancient Chinese methods, which is essentially equivalent to Gaussian elimination. Let's translate the problem and solution into Python code step by step.

### Problem Description:
There are three types of horses: Wu horse (武馬), Zhong horse (中馬), and Xia horse (下馬). Each horse is tasked with carrying 40 shi (石) up a hill but cannot do so alone. To solve this, they borrow strength from each other:
- Wu horse borrows one Zhong horse.
- Zhong horse borrows one Xia horse.
- Xia horse borrows one Wu horse.

The question is: How much pulling power (力引) does each type of horse have?

### Procedure:
The ancient Chinese method for solving this involves setting up equations based on the borrowing relationships and solving them step by step using elimination.

---


"""


from fractions import Fraction

# Step 1: Define the borrowing relationships as equations
# 武馬 (Wu horse) + 中馬 (Zhong horse) = 40 shi
# 中馬 (Zhong horse) + 下馬 (Xia horse) = 40 shi
# 下馬 (Xia horse) + 武馬 (Wu horse) = 40 shi

# Let:
# 武馬力引 = a
# 中馬力引 = b
# 下馬力引 = c

# The equations are:
# a + b = 40
# b + c = 40
# c + a = 40

# Step 2: Represent the equations in matrix form
# Coefficients matrix:
# | 1  1  0 |   | a |   | 40 |
# | 0  1  1 | * | b | = | 40 |
# | 1  0  1 |   | c |   | 40 |

# Step 3: Solve using elimination (Gaussian elimination)

# Initialize the augmented matrix
matrix = [
    [1, 1, 0, 40],  # a + b = 40
    [0, 1, 1, 40],  # b + c = 40
    [1, 0, 1, 40]   # c + a = 40
]

# Step 4: Eliminate the first variable (a) from the second and third rows
for i in range(1, 3):
    factor = Fraction(matrix[i][0], matrix[0][0])
    for j in range(4):
        matrix[i][j] -= factor * matrix[0][j]

# Step 5: Eliminate the second variable (b) from the third row
factor = Fraction(matrix[2][1], matrix[1][1])
for j in range(4):
    matrix[2][j] -= factor * matrix[1][j]

# Step 6: Back-substitute to find the values of a, b, and c
c = Fraction(matrix[2][3], matrix[2][2])
b = Fraction(matrix[1][3] - matrix[1][2] * c, matrix[1][1])
a = Fraction(matrix[0][3] - matrix[0][1] * b, matrix[0][0])

# Step 7: Output the results
a = float(a)
b = float(b)
c = float(c)

# 武馬力引 = a 石
# 中馬力引 = b 石
# 下馬力引 = c 石

print(f"武馬力引: {a} 石")
print(f"中馬力引: {b} 石")
print(f"下馬力引: {c} 石")


"""


### Explanation of the Code:
1. **Matrix Representation**: The equations are represented as an augmented matrix.
2. **Gaussian Elimination**: The matrix is reduced row by row to isolate each variable.
3. **Back-Substitution**: The values of the variables are calculated by substituting back into the equations.
4. **Output**: The pulling power of each type of horse is printed.

### Answer:
- 武馬力引 = `a` 石
- 中馬力引 = `b` 石
- 下馬力引 = `c` 石
"""


"""
Variable 'a' has wrong value. Expected: 1, Actual: 20.0
Variable 'b' has wrong value. Expected: 160/7, Actual: 20.0
Variable 'c' has wrong value. Expected: 1, Actual: 20.0
Missing variable in output: 'd'
Missing variable in output: 'e'
Missing variable in output: 'f'"""
