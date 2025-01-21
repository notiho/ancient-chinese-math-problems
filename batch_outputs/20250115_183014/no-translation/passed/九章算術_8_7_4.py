"""
今有賣牛二、羊五，以買十三豕，有餘錢一千。賣牛三、豕三，以買九羊，錢適足。賣羊六、豕八，以買五牛，錢不足六百。問︰牛、羊、豕價各幾何？
術曰：如方程，置牛二、羊五正，豕一十三負，餘錢數正；次牛三正，羊九負，豕三正；次牛五負，羊六正，豕八正，不足錢負。以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：牛價 a ，羊價 b ，豕價 c 。
"""

"""
To solve this problem, we need to translate the ancient Chinese "方程術" (method of solving simultaneous linear equations) into Python code. The problem involves three equations with three unknowns (牛價, 羊價, 豕價). Let's proceed step by step.

### Problem Setup:
The equations based on the problem are:
1. \( 2x + 5y - 13z = 1000 \)  (Equation 1)
2. \( 3x - 9y + 3z = 0 \)      (Equation 2)
3. \( -5x + 6y + 8z = -600 \)  (Equation 3)

Here:
- \( x \) is the price of a cow (牛價),
- \( y \) is the price of a sheep (羊價),
- \( z \) is the price of a pig (豕價).

We will solve these equations using the described method.

---

### Python Code:


"""


from fractions import Fraction

# Coefficients of the equations
# Equation 1: 2x + 5y - 13z = 1000
# Equation 2: 3x - 9y + 3z = 0
# Equation 3: -5x + 6y + 8z = -600

# Representing the equations as a matrix
matrix = [
    [2, 5, -13, 1000],  # Equation 1
    [3, -9, 3, 0],      # Equation 2
    [-5, 6, 8, -600]    # Equation 3
]

# Step 1: Normalize the first row
factor = matrix[0][0]
matrix[0] = [Fraction(x, factor) for x in matrix[0]]

# Step 2: Eliminate x from the second and third rows
for i in range(1, 3):
    factor = matrix[i][0]
    matrix[i] = [matrix[i][j] - factor * matrix[0][j] for j in range(4)]

# Step 3: Normalize the second row
factor = matrix[1][1]
matrix[1] = [Fraction(x, factor) for x in matrix[1]]

# Step 4: Eliminate y from the first and third rows
for i in [0, 2]:
    factor = matrix[i][1]
    matrix[i] = [matrix[i][j] - factor * matrix[1][j] for j in range(4)]

# Step 5: Normalize the third row
factor = matrix[2][2]
matrix[2] = [Fraction(x, factor) for x in matrix[2]]

# Step 6: Eliminate z from the first and second rows
for i in [0, 1]:
    factor = matrix[i][2]
    matrix[i] = [matrix[i][j] - factor * matrix[2][j] for j in range(4)]

# The solution is now in the last column of the matrix
a = matrix[0][3]  # 牛價
b = matrix[1][3]  # 羊價
c = matrix[2][3]  # 豕價

# Output the results
a, b, c


"""


---

### Explanation of the Code:
1. **Matrix Representation**: The equations are represented as a matrix where each row corresponds to an equation, and the last column is the constant term.
2. **Row Operations**: The algorithm performs Gaussian elimination to reduce the matrix to row echelon form. This involves:
   - Normalizing rows by dividing by the leading coefficient.
   - Eliminating variables from other rows by subtracting multiples of the current row.
3. **Back Substitution**: Once the matrix is in row echelon form, the solution is directly read from the last column.

---

### Final Answer:
After running the code, the values of \( a \), \( b \), and \( c \) (牛價, 羊價, 豕價) will be computed. These represent the prices of a cow, a sheep, and a pig, respectively.
"""


"""
"""
