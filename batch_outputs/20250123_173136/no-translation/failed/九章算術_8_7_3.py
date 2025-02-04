"""
今有賣牛二、羊五，以買十三豕，有餘錢一千。賣牛三、豕三，以買九羊，錢適足。賣羊六、豕八，以買五牛，錢不足六百。問︰牛、羊、豕價各幾何？
術曰：如方程，置牛二、羊五正，豕一十三負，餘錢數正；次牛三正，羊九負，豕三正；次牛五負，羊六正，豕八正，不足錢負。以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：牛價 a ，羊價 b ，豕價 c 。
"""

"""
This problem involves solving a system of linear equations using the ancient Chinese method of elimination, similar to Gaussian elimination. Here's how to translate the procedure into Python code:


"""


from fractions import Fraction

# Define the equations based on the problem:
# 2牛 + 5羊 - 13豕 = 1000
# 3牛 - 9羊 + 3豕 = 0
# -5牛 + 6羊 + 8豕 = -600

# Represent the equations as a matrix (augmented matrix form)
matrix = [
    [2, 5, -13, 1000],  # First equation
    [3, -9, 3, 0],      # Second equation
    [-5, 6, 8, -600]    # Third equation
]

# Step 1: Normalize the first row
for i in range(4):
    matrix[0][i] = Fraction(matrix[0][i], matrix[0][0])

# Step 2: Eliminate the first variable from the second and third rows
for row in range(1, 3):
    factor = matrix[row][0]
    for col in range(4):
        matrix[row][col] -= factor * matrix[0][col]

# Step 3: Normalize the second row
for i in range(1, 4):
    matrix[1][i] = Fraction(matrix[1][i], matrix[1][1])

# Step 4: Eliminate the second variable from the third row
factor = matrix[2][1]
for col in range(1, 4):
    matrix[2][col] -= factor * matrix[1][col]

# Step 5: Solve for the third variable
matrix[2][3] = Fraction(matrix[2][3], matrix[2][2])
c = matrix[2][3]

# Step 6: Back-substitute to solve for the second variable
matrix[1][3] -= matrix[1][2] * c
b = matrix[1][3]

# Step 7: Back-substitute to solve for the first variable
matrix[0][3] -= matrix[0][2] * c
matrix[0][3] -= matrix[0][1] * b
a = matrix[0][3]

# Output the results
a, b, c


"""


### Explanation of the Code:
1. **Matrix Representation**: The system of equations is represented as an augmented matrix.
2. **Normalization and Elimination**: The matrix is manipulated row by row to eliminate variables, following the ancient Chinese elimination method.
3. **Back-Substitution**: After reducing the matrix to upper triangular form, the variables are solved starting from the last row.
4. **Fractions**: The `Fraction` class is used to ensure exact arithmetic, as required by the problem.

### Final Answer:
- `a` is the price of a cow (牛價).
- `b` is the price of a sheep (羊價).
- `c` is the price of a pig (豕價).
"""


"""
Variable 'a' has wrong value. Expected: 1200, Actual: 23800/1359
Variable 'b' has wrong value. Expected: 500, Actual: 4600/453
Variable 'c' has wrong value. Expected: 300, Actual: -97400/1359"""
