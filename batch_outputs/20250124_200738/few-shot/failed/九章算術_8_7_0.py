"""
今有賣牛二、羊五，以買十三豕，有餘錢一千。賣牛三、豕三，以買九羊，錢適足。賣羊六、豕八，以買五牛，錢不足六百。問︰牛、羊、豕價各幾何？
術曰：如方程，置牛二、羊五正，豕一十三負，餘錢數正；次牛三正，羊九負，豕三正；次牛五負，羊六正，豕八正，不足錢負。以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：牛價 a ，羊價 b ，豕價 c 。
"""

"""
This problem involves solving a system of linear equations using the ancient Chinese method of elimination, which is similar to Gaussian elimination. Let's translate the problem and procedure into Python code step by step.

### Problem:
We are given three equations based on the transactions:
1. Selling 2 cows and 5 sheep to buy 13 pigs, with 1000 money left over.
2. Selling 3 cows and 3 pigs to buy 9 sheep, with no money left over.
3. Selling 6 sheep and 8 pigs to buy 5 cows, falling short by 600 money.

We need to find the price of a cow (`a`), a sheep (`b`), and a pig (`c`).

### Procedure:
The procedure uses elimination to solve the system of equations. Let's implement this step by step.

---


"""

#----- content starts here -----

from fractions import Fraction

# Step 1: Represent the equations as a matrix
# Each row corresponds to an equation: [coefficients of a, b, c, constant term]
matrix = [
    [2, 5, -13, 1000],  # 2a + 5b - 13c = 1000
    [3, -9, 3, 0],      # 3a - 9b + 3c = 0
    [-5, 6, 8, -600]    # -5a + 6b + 8c = -600
]

# Step 2: Perform Gaussian elimination
# Normalize the first row
for i in range(4):
    matrix[0][i] = Fraction(matrix[0][i], matrix[0][0])

# Eliminate the first variable (a) from the second and third rows
for row in range(1, 3):
    factor = matrix[row][0]
    for col in range(4):
        matrix[row][col] -= factor * matrix[0][col]

# Normalize the second row
for i in range(1, 4):
    matrix[1][i] = Fraction(matrix[1][i], matrix[1][1])

# Eliminate the second variable (b) from the third row
factor = matrix[2][1]
for col in range(1, 4):
    matrix[2][col] -= factor * matrix[1][col]

# Normalize the third row
matrix[2][3] = Fraction(matrix[2][3], matrix[2][2])

# Back-substitute to find the values of c, b, and a
c = matrix[2][3]
b = matrix[1][3] - matrix[1][2] * c
a = matrix[0][3] - matrix[0][2] * c - matrix[0][1] * b

# Output the results
a, b, c
#----- content ends here -----


"""


### Explanation of the Code:
1. **Matrix Representation**: Each equation is represented as a row in the matrix, with the coefficients of `a`, `b`, `c`, and the constant term.
2. **Gaussian Elimination**: The process involves normalizing rows and eliminating variables step by step:
   - Normalize the first row to make the coefficient of `a` equal to 1.
   - Subtract multiples of the first row from the second and third rows to eliminate `a` from those rows.
   - Normalize the second row to make the coefficient of `b` equal to 1.
   - Subtract multiples of the second row from the third row to eliminate `b`.
   - Normalize the third row to make the coefficient of `c` equal to 1.
3. **Back-Substitution**: After elimination, the values of `c`, `b`, and `a` are computed by substituting back into the equations.

### Answer:
The values of `a`, `b`, and `c` (prices of a cow, sheep, and pig) are stored in the variables `a`, `b`, and `c`.
"""


"""
Variable 'a' has wrong value. Expected: 1200, Actual: 23800/1359
Variable 'b' has wrong value. Expected: 500, Actual: 4600/453
Variable 'c' has wrong value. Expected: 300, Actual: -97400/1359"""
