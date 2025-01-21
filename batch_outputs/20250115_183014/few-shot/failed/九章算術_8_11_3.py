"""
今有武馬一匹，中馬二匹，下馬三匹，皆載四十石至阪，皆不能上。武馬借中馬一匹，中馬借下馬一匹，下馬借武馬一匹，乃皆上。問︰武、中、下馬一匹各力引幾何？
術曰：如方程各置所借，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：武馬 a匹 力引 b石 ，中馬 c匹 力引 d石 ，下馬 e匹 力引 f石 。
"""

"""
This problem involves solving a system of equations using ancient Chinese methods, specifically the "fangcheng" (方程) method, which is an early form of linear algebra. Let's translate the problem and solution into Python code step by step.

### Problem Breakdown:
- There are three types of horses: 武馬 (strong horse), 中馬 (medium horse), and 下馬 (weak horse).
- Each horse type cannot carry 40 shi (石) up a slope on its own.
- Borrowing occurs:
  - 武馬 borrows 1 中馬.
  - 中馬 borrows 1 下馬.
  - 下馬 borrows 1 武馬.
- After borrowing, all horses can carry the load.
- The goal is to determine the pulling power (力引) of each type of horse.

### Procedure:
The "fangcheng" method is used to solve the system of equations. The procedure involves:
1. Setting up equations based on the borrowing and carrying conditions.
2. Using elimination and substitution to solve for the pulling power of each horse type.

Let's implement this in Python:


"""


from fractions import Fraction

# Step 1: Define the borrowing equations
# Let x = 武馬 pulling power, y = 中馬 pulling power, z = 下馬 pulling power
# Each horse must pull 40 shi after borrowing:
# 武馬 + 中馬 = 40
# 中馬 + 下馬 = 40
# 下馬 + 武馬 = 40

# Step 2: Represent the equations in matrix form
# Coefficients of the equations:
# x + y       = 40
#     y + z   = 40
# x     + z   = 40

# Matrix representation:
# [ 1  1  0 ] [x]   [40]
# [ 0  1  1 ] [y] = [40]
# [ 1  0  1 ] [z]   [40]

# Step 3: Solve using elimination (fangcheng method)
# Start with the matrix:
# A = [[1, 1, 0], [0, 1, 1], [1, 0, 1]]
# B = [40, 40, 40]

# Initialize variables
A = [
    [1, 1, 0],  # Coefficients of the first equation
    [0, 1, 1],  # Coefficients of the second equation
    [1, 0, 1]   # Coefficients of the third equation
]
B = [40, 40, 40]  # Constants on the right-hand side

# Elimination process
# Step 3.1: Eliminate x from the second and third rows
factor1 = Fraction(A[1][0], A[0][0])  # Factor to eliminate x from row 2
A[1] = [A[1][i] - factor1 * A[0][i] for i in range(3)]
B[1] = B[1] - factor1 * B[0]

factor2 = Fraction(A[2][0], A[0][0])  # Factor to eliminate x from row 3
A[2] = [A[2][i] - factor2 * A[0][i] for i in range(3)]
B[2] = B[2] - factor2 * B[0]

# Step 3.2: Eliminate y from the third row
factor3 = Fraction(A[2][1], A[1][1])  # Factor to eliminate y from row 3
A[2] = [A[2][i] - factor3 * A[1][i] for i in range(3)]
B[2] = B[2] - factor3 * B[1]

# Step 3.3: Back substitution to solve for z, y, x
z = Fraction(B[2], A[2][2])  # Solve for z
y = Fraction(B[1] - A[1][2] * z, A[1][1])  # Solve for y
x = Fraction(B[0] - A[0][1] * y - A[0][2] * z, A[0][0])  # Solve for x

# Step 4: Output the results
a = 1  # 武馬 count
b = x  # 武馬 pulling power
c = 1  # 中馬 count
d = y  # 中馬 pulling power
e = 1  # 下馬 count
f = z  # 下馬 pulling power

print(f"武馬 {a}匹 力引 {b}石")
print(f"中馬 {c}匹 力引 {d}石")
print(f"下馬 {e}匹 力引 {f}石")


"""


### Explanation of the Code:
1. The equations are set up based on the problem description.
2. The "fangcheng" method (elimination) is applied to solve the system of linear equations.
3. The results are expressed as fractions to ensure accuracy.

### Output:
The pulling power of each type of horse will be displayed as fractions of shi (石).
"""


"""
Variable 'b' has wrong value. Expected: 160/7, Actual: 20
Variable 'd' has wrong value. Expected: 120/7, Actual: 20
Variable 'f' has wrong value. Expected: 40/7, Actual: 20"""
