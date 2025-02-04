"""
今有賣牛二、羊五，以買十三豕，有餘錢一千。賣牛三、豕三，以買九羊，錢適足。賣羊六、豕八，以買五牛，錢不足六百。問︰牛、羊、豕價各幾何？
術曰：如方程，置牛二、羊五正，豕一十三負，餘錢數正；次牛三正，羊九負，豕三正；次牛五負，羊六正，豕八正，不足錢負。以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：牛價 a(=1200) ，羊價 b(=500) ，豕價 c(=300) 。
"""

"""
To solve this problem, we will translate the ancient Chinese mathematical procedure into Python code. The problem involves solving a system of linear equations using the method described in the "方程術" (method of solving simultaneous equations). Here's the step-by-step solution:

### Problem Breakdown:
1. **Equations derived from the problem:**
   - Selling 2 cows and 5 sheep can buy 13 pigs, with 1000 money left:
     \( 2a + 5b - 13c = 1000 \)
   - Selling 3 cows and 3 pigs can buy 9 sheep, with no money left:
     \( 3a - 9b + 3c = 0 \)
   - Selling 6 sheep and 8 pigs can buy 5 cows, but 600 money is short:
     \( -5a + 6b + 8c = -600 \)

2. **Goal:** Solve for \( a \) (price of a cow), \( b \) (price of a sheep), and \( c \) (price of a pig).

3. **Method:** Use the ancient "方程術" (method of solving simultaneous equations), which is equivalent to Gaussian elimination.

---

### Python Code Implementation:


"""

#----- content starts here -----

from fractions import Fraction

# Coefficients of the equations
# Equation 1: 2a + 5b - 13c = 1000
# Equation 2: 3a - 9b + 3c = 0
# Equation 3: -5a + 6b + 8c = -600

# Initialize the augmented matrix
matrix = [
    [2, 5, -13, 1000],  # Row 1
    [3, -9, 3, 0],      # Row 2
    [-5, 6, 8, -600]    # Row 3
]

# Step 1: Normalize the first row
factor = matrix[0][0]
matrix[0] = [Fraction(x, factor) for x in matrix[0]]

# Step 2: Eliminate the first variable (a) from the second and third rows
for i in range(1, 3):
    factor = matrix[i][0]
    matrix[i] = [matrix[i][j] - factor * matrix[0][j] for j in range(4)]

# Step 3: Normalize the second row
factor = matrix[1][1]
matrix[1] = [Fraction(x, factor) for x in matrix[1]]

# Step 4: Eliminate the second variable (b) from the first and third rows
for i in [0, 2]:
    factor = matrix[i][1]
    matrix[i] = [matrix[i][j] - factor * matrix[1][j] for j in range(4)]

# Step 5: Normalize the third row
factor = matrix[2][2]
matrix[2] = [Fraction(x, factor) for x in matrix[2]]

# Step 6: Eliminate the third variable (c) from the first and second rows
for i in [0, 1]:
    factor = matrix[i][2]
    matrix[i] = [matrix[i][j] - factor * matrix[2][j] for j in range(4)]

# The solution is now in the last column of the matrix
a = matrix[0][3]  # Price of a cow
b = matrix[1][3]  # Price of a sheep
c = matrix[2][3]  # Price of a pig

# Output the results
a = float(a) #1200
b =float(b)#500
#----- content ends here -----


"""

"""


"""
"""
