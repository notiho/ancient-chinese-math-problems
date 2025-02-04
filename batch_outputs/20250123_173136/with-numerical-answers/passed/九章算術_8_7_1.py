"""
今有賣牛二、羊五，以買十三豕，有餘錢一千。賣牛三、豕三，以買九羊，錢適足。賣羊六、豕八，以買五牛，錢不足六百。問︰牛、羊、豕價各幾何？
術曰：如方程，置牛二、羊五正，豕一十三負，餘錢數正；次牛三正，羊九負，豕三正；次牛五負，羊六正，豕八正，不足錢負。以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：牛價 a(=1200) ，羊價 b(=500) ，豕價 c(=300) 。
"""

"""
This is a classic system of linear equations problem from ancient Chinese mathematics, solved using the "fangcheng" (方程) method, which is an early form of Gaussian elimination. Let's translate the problem and solution into Python code step by step.

### Problem:
We are given three equations based on the transactions:
1. Selling 2 cows and 5 sheep can buy 13 pigs, with 1000 money left over.
2. Selling 3 cows and 3 pigs can buy 9 sheep, with no money left over.
3. Selling 6 sheep and 8 pigs can buy 5 cows, but 600 money is still needed.

We need to find the prices of a cow (`a`), a sheep (`b`), and a pig (`c`).

### Procedure:
The "fangcheng" method involves setting up a system of linear equations and solving it using elimination. Here's the Python implementation:


"""


from fractions import Fraction

# Coefficients of the equations
# Equation 1: 2a + 5b - 13c = 1000
# Equation 2: 3a - 9b + 3c = 0
# Equation 3: -5a + 6b + 8c = -600

# Representing the system of equations as a matrix
# Each row corresponds to an equation: [a_coeff, b_coeff, c_coeff, constant_term]
matrix = [
    [2, 5, -13, 1000],  # Equation 1
    [3, -9, 3, 0],      # Equation 2
    [-5, 6, 8, -600]    # Equation 3
]

# Step 1: Normalize the first row (make the first coefficient 1)
factor = matrix[0][0]
matrix[0] = [Fraction(x, factor) for x in matrix[0]]

# Step 2: Eliminate the first variable (a) from the second and third rows
for i in range(1, 3):
    factor = matrix[i][0]
    matrix[i] = [matrix[i][j] - factor * matrix[0][j] for j in range(4)]

# Step 3: Normalize the second row (make the second coefficient 1)
factor = matrix[1][1]
matrix[1] = [Fraction(x, factor) for x in matrix[1]]

# Step 4: Eliminate the second variable (b) from the first and third rows
for i in [0, 2]:
    factor = matrix[i][1]
    matrix[i] = [matrix[i][j] - factor * matrix[1][j] for j in range(4)]

# Step 5: Normalize the third row (make the third coefficient 1)
factor = matrix[2][2]
matrix[2] = [Fraction(x, factor) for x in matrix[2]]

# Step 6: Eliminate the third variable (c) from the first and second rows
for i in [0, 1]:
    factor = matrix[i][2]
    matrix[i] = [matrix[i][j] - factor * matrix[2][j] for j in range(4)]

# The matrix is now in reduced row-echelon form, and the solution can be read directly
a = matrix[0][3]  # Price of a cow
b = matrix[1][3]  # Price of a sheep
c = matrix[2][3]  # Price of a pig

# Convert results to integers (since prices are in whole numbers)
a = int(a)
b = int(b)
c = int(c)

# Output the results
a, b, c  # a = 1200, b = 500, c = 300


"""


### Explanation of the Code:
1. **Matrix Representation**: The system of equations is represented as a matrix, where each row corresponds to an equation, and each column corresponds to a variable or the constant term.
2. **Normalization and Elimination**: The "fangcheng" method involves making the leading coefficient of each row 1 (normalization) and then eliminating the corresponding variable from the other rows.
3. **Back Substitution**: Once the matrix is in reduced row-echelon form, the solution can be read directly from the last column.

### Answer:
The prices are:
- Cow (`a`): 1200
- Sheep (`b`): 500
- Pig (`c`): 300
"""


"""
"""
