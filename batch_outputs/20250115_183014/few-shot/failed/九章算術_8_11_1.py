"""
今有武馬一匹，中馬二匹，下馬三匹，皆載四十石至阪，皆不能上。武馬借中馬一匹，中馬借下馬一匹，下馬借武馬一匹，乃皆上。問︰武、中、下馬一匹各力引幾何？
術曰：如方程各置所借，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：武馬 a匹 力引 b石 ，中馬 c匹 力引 d石 ，下馬 e匹 力引 f石 。
"""

"""
This problem involves solving a system of linear equations using ancient Chinese methods, which is equivalent to Gaussian elimination in modern terms. Let's break it down step by step and encode the solution in Python.

### Problem Explanation:
We have three types of horses: 武馬 (strong horse), 中馬 (medium horse), and 下馬 (weak horse). Each horse type has a certain pulling capacity. Initially, none of them can pull 40 shi (石) up the slope. By borrowing horses from each other, they manage to succeed. The goal is to determine the pulling capacity of each type of horse.

The procedure involves setting up equations based on the borrowing scenario and solving them using elimination techniques.

---

### Python Code Implementation:


"""


from fractions import Fraction

# Step 1: Define the equations based on the problem description.
# Let x = 武馬 pulling capacity (石)
# Let y = 中馬 pulling capacity (石)
# Let z = 下馬 pulling capacity (石)

# Equation 1: 武馬 borrows 1 中馬
# x + y = 40
# Equation 2: 中馬 borrows 1 下馬
# y + z = 40
# Equation 3: 下馬 borrows 1 武馬
# z + x = 40

# Step 2: Represent the equations in matrix form.
# Coefficients matrix:
# [ 1  1  0 ] [x]   [40]
# [ 0  1  1 ] [y] = [40]
# [ 1  0  1 ] [z]   [40]

# Augmented matrix:
matrix = [
    [1, 1, 0, 40],  # x + y = 40
    [0, 1, 1, 40],  # y + z = 40
    [1, 0, 1, 40]   # z + x = 40
]

# Step 3: Perform Gaussian elimination to solve the system.

# Normalize the first row (make the leading coefficient 1).
for i in range(3):
    factor = matrix[i][i]
    for j in range(4):
        matrix[i][j] = Fraction(matrix[i][j], factor)

# Eliminate the first variable (x) from the second and third rows.
for i in range(1, 3):
    factor = matrix[i][0]
    for j in range(4):
        matrix[i][j] -= factor * matrix[0][j]

# Eliminate the second variable (y) from the third row.
factor = matrix[2][1]
for j in range(4):
    matrix[2][j] -= factor * matrix[1][j]

# Back-substitution to find the values of x, y, and z.
z = matrix[2][3] / matrix[2][2]
y = (matrix[1][3] - matrix[1][2] * z) / matrix[1][1]
x = (matrix[0][3] - matrix[0][1] * y) / matrix[0][0]

# Step 4: Output the results.
a, b = 1, x  # 武馬: 1匹, pulling capacity b 石
c, d = 1, y  # 中馬: 1匹, pulling capacity d 石
e, f = 1, z  # 下馬: 1匹, pulling capacity f 石

# Answer:
print(f"武馬 {a}匹 力引 {b}石")
print(f"中馬 {c}匹 力引 {d}石")
print(f"下馬 {e}匹 力引 {f}石")


"""


---

### Explanation of the Code:
1. **Equations Setup**:
   - We derive three equations based on the borrowing scenario.
   - These equations are represented in matrix form for solving.

2. **Gaussian Elimination**:
   - The matrix is normalized and reduced step by step to isolate each variable.
   - Back-substitution is used to calculate the values of \(x\), \(y\), and \(z\).

3. **Output**:
   - The pulling capacity of each type of horse is printed.

---

### Final Answer:
After running the code, the output will be:

```
武馬 1匹 力引 20石
中馬 1匹 力引 20石
下馬 1匹 力引 20石
```
"""


"""
Variable 'b' has wrong value. Expected: 160/7, Actual: 20
Variable 'd' has wrong value. Expected: 120/7, Actual: 20
Variable 'f' has wrong value. Expected: 40/7, Actual: 20"""
