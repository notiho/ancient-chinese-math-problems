"""
今有武馬一匹，中馬二匹，下馬三匹，皆載四十石至阪，皆不能上。武馬借中馬一匹，中馬借下馬一匹，下馬借武馬一匹，乃皆上。問︰武、中、下馬一匹各力引幾何？
術曰：如方程各置所借，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：武馬一匹力引 a石 ，中馬一匹力引 b石 ，下馬一匹力引 c石 。
"""

"""
To solve this problem, we will translate the ancient Chinese mathematical procedure into Python code step by step. The problem involves solving a system of linear equations using the described method, which is essentially Gaussian elimination.

### Problem Setup:
Let:
- \( x \): the pulling power of a 武馬 (Wu horse).
- \( y \): the pulling power of a 中馬 (Zhong horse).
- \( z \): the pulling power of a 下馬 (Xia horse).

The equations are derived from the problem's description:
1. 武馬借中馬一匹: \( x + y = 40 \)
2. 中馬借下馬一匹: \( y + z = 40 \)
3. 下馬借武馬一匹: \( z + x = 40 \)

We need to solve for \( x \), \( y \), and \( z \).

---

### Python Code Implementation:


"""


from fractions import Fraction

# Coefficients of the equations
# Equation 1: x + y = 40
# Equation 2: y + z = 40
# Equation 3: z + x = 40

# Step 1: Represent the system of equations as a matrix
# [ 1  1  0 | 40 ]
# [ 0  1  1 | 40 ]
# [ 1  0  1 | 40 ]

# Initialize the augmented matrix
matrix = [
    [1, 1, 0, 40],  # x + y = 40
    [0, 1, 1, 40],  # y + z = 40
    [1, 0, 1, 40]   # z + x = 40
]

# Step 2: Perform Gaussian elimination
# Make the first column's pivot 1 (already done), eliminate below
matrix[1] = [matrix[1][i] - matrix[0][i] * matrix[1][0] for i in range(4)]
matrix[2] = [matrix[2][i] - matrix[0][i] * matrix[2][0] for i in range(4)]

# Make the second column's pivot 1 (already done), eliminate below
matrix[2] = [matrix[2][i] - matrix[1][i] * matrix[2][1] for i in range(4)]

# Step 3: Back substitution to solve for z, y, x
z = Fraction(matrix[2][3], matrix[2][2])
y = Fraction(matrix[1][3] - matrix[1][2] * z, matrix[1][1])
x = Fraction(matrix[0][3] - matrix[0][1] * y, matrix[0][0])

# Results
a = x  # 武馬 pulling power
b = y  # 中馬 pulling power
c = z  # 下馬 pulling power

# Output the results
a, b, c


"""


---

### Explanation of the Code:
1. **Matrix Representation**: The system of equations is represented as an augmented matrix.
2. **Gaussian Elimination**: The procedure described in the problem is essentially Gaussian elimination:
   - Eliminate variables column by column.
   - Use back substitution to solve for the variables.
3. **Fractions**: The `Fraction` class is used to ensure exact arithmetic, as required by the problem.

### Final Answer:
The pulling power of each horse is:
- 武馬 (Wu horse): \( a = 20 \) 石
- 中馬 (Zhong horse): \( b = 20 \) 石
- 下馬 (Xia horse): \( c = 20 \) 石
"""


"""
Variable 'a' has wrong value. Expected: 160/7, Actual: 20
Variable 'b' has wrong value. Expected: 120/7, Actual: 20
Variable 'c' has wrong value. Expected: 40/7, Actual: 20"""
