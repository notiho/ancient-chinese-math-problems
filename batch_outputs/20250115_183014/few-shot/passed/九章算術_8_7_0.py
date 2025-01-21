"""
今有賣牛二、羊五，以買十三豕，有餘錢一千。賣牛三、豕三，以買九羊，錢適足。賣羊六、豕八，以買五牛，錢不足六百。問︰牛、羊、豕價各幾何？
術曰：如方程，置牛二、羊五正，豕一十三負，餘錢數正；次牛三正，羊九負，豕三正；次牛五負，羊六正，豕八正，不足錢負。以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：牛價 a ，羊價 b ，豕價 c 。
"""

"""
This problem involves solving a system of linear equations using the ancient Chinese method of elimination, which is conceptually similar to Gaussian elimination. Let's translate the problem and solution into Python code.

### Problem Description:
We are given three scenarios involving the prices of cows, sheep, and pigs:
1. Selling 2 cows and 5 sheep to buy 13 pigs, with 1000 units of money left over.
2. Selling 3 cows and 3 pigs to buy 9 sheep, with no money left over.
3. Selling 6 sheep and 8 pigs to buy 5 cows, but falling short by 600 units of money.

We need to find the price of a cow (`a`), a sheep (`b`), and a pig (`c`).

### Procedure:
The ancient Chinese elimination method (方程術) is described in the problem. It involves systematically eliminating variables to solve the system of equations.

### Equations:
From the problem, we can derive the following equations:
1. \( 2a + 5b - 13c = 1000 \)
2. \( 3a - 9b + 3c = 0 \)
3. \( -5a + 6b + 8c = -600 \)

Let's implement this in Python:


"""


from fractions import Fraction

# Coefficients of the equations
# Equation 1: 2a + 5b - 13c = 1000
# Equation 2: 3a - 9b + 3c = 0
# Equation 3: -5a + 6b + 8c = -600

# Representing the system of equations as a matrix
matrix = [
    [2, 5, -13, 1000],  # Equation 1
    [3, -9, 3, 0],      # Equation 2
    [-5, 6, 8, -600]    # Equation 3
]

# Step 1: Eliminate the first variable (a) from the second and third equations
# Normalize the first row
factor = matrix[0][0]
matrix[0] = [Fraction(x, factor) for x in matrix[0]]

# Eliminate 'a' from the second row
factor = matrix[1][0]
matrix[1] = [matrix[1][i] - factor * matrix[0][i] for i in range(4)]

# Eliminate 'a' from the third row
factor = matrix[2][0]
matrix[2] = [matrix[2][i] - factor * matrix[0][i] for i in range(4)]

# Step 2: Eliminate the second variable (b) from the third equation
# Normalize the second row
factor = matrix[1][1]
matrix[1] = [Fraction(x, factor) for x in matrix[1]]

# Eliminate 'b' from the third row
factor = matrix[2][1]
matrix[2] = [matrix[2][i] - factor * matrix[1][i] for i in range(4)]

# Step 3: Solve for the third variable (c)
# Normalize the third row
factor = matrix[2][2]
matrix[2] = [Fraction(x, factor) for x in matrix[2]]

# The value of c is now the last element of the third row
c = matrix[2][3]

# Step 4: Back-substitute to find b
b = matrix[1][3] - matrix[1][2] * c

# Step 5: Back-substitute to find a
a = matrix[0][3] - matrix[0][2] * c - matrix[0][1] * b

# Results
a = float(a)
b = float(b)
c = float(c)

print(f"牛價 a = {a}")
print(f"羊價 b = {b}")
print(f"豕價 c = {c}")


"""


### Explanation:
1. The system of equations is represented as a matrix, where each row corresponds to an equation.
2. The elimination process systematically reduces the matrix to an upper triangular form, where each variable can be solved step by step.
3. The solution is back-substituted to find the values of the variables.

### Answer:
The values of `a`, `b`, and `c` (prices of cows, sheep, and pigs) will be printed as the result.
"""


"""
"""
