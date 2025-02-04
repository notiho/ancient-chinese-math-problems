"""
今有武馬一匹，中馬二匹，下馬三匹，皆載四十石至阪，皆不能上。武馬借中馬一匹，中馬借下馬一匹，下馬借武馬一匹，乃皆上。問︰武、中、下馬一匹各力引幾何？
術曰：如方程各置所借，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：武馬一匹力引 a石 ，中馬一匹力引 b石 ，下馬一匹力引 c石 。
"""

"""
This problem involves solving a system of equations using the ancient Chinese method of elimination, similar to Gaussian elimination. Let's translate the procedure into Python code step by step.

### Problem Breakdown:
- There are three types of horses: 武馬 (strong horse), 中馬 (medium horse), and 下馬 (weak horse).
- Each horse type carries 40 石 (shi) but cannot climb the slope alone.
- Borrowing occurs:
  - 武馬 borrows 1 中馬.
  - 中馬 borrows 1 下馬.
  - 下馬 borrows 1 武馬.
- The goal is to find the pulling force (力引) of each horse type.

### Procedure:
The procedure uses a system of equations to represent the borrowing and solving for the pulling force of each horse type.

Let:
- \( x \): pulling force of 武馬 (strong horse).
- \( y \): pulling force of 中馬 (medium horse).
- \( z \): pulling force of 下馬 (weak horse).

The equations are:
1. \( x + y = 40 \) (武馬 borrows 1 中馬).
2. \( y + z = 40 \) (中馬 borrows 1 下馬).
3. \( z + x = 40 \) (下馬 borrows 1 武馬).

We solve this system of equations using the method described.

---

### Python Code Implementation:


"""


from fractions import Fraction

# Step 1: Define the coefficients and constants of the equations.
# The equations are:
# x + y = 40
# y + z = 40
# z + x = 40

# Coefficients matrix (left-hand side of equations)
coefficients = [
    [1, 1, 0],  # x + y = 40
    [0, 1, 1],  # y + z = 40
    [1, 0, 1]   # z + x = 40
]

# Constants (right-hand side of equations)
constants = [40, 40, 40]

# Step 2: Elimination process (similar to Gaussian elimination).
# Normalize the first row.
factor = coefficients[0][0]
coefficients[0] = [Fraction(c, factor) for c in coefficients[0]]
constants[0] = Fraction(constants[0], factor)

# Eliminate x from the second and third rows.
factor = coefficients[1][0]
coefficients[1] = [coefficients[1][i] - factor * coefficients[0][i] for i in range(3)]
constants[1] = constants[1] - factor * constants[0]

factor = coefficients[2][0]
coefficients[2] = [coefficients[2][i] - factor * coefficients[0][i] for i in range(3)]
constants[2] = constants[2] - factor * constants[0]

# Normalize the second row.
factor = coefficients[1][1]
coefficients[1] = [Fraction(c, factor) for c in coefficients[1]]
constants[1] = Fraction(constants[1], factor)

# Eliminate y from the third row.
factor = coefficients[2][1]
coefficients[2] = [coefficients[2][i] - factor * coefficients[1][i] for i in range(3)]
constants[2] = constants[2] - factor * constants[1]

# Normalize the third row.
factor = coefficients[2][2]
coefficients[2] = [Fraction(c, factor) for c in coefficients[2]]
constants[2] = Fraction(constants[2], factor)

# Step 3: Back substitution to solve for x, y, z.
z = constants[2]
y = constants[1] - coefficients[1][2] * z
x = constants[0] - coefficients[0][1] * y - coefficients[0][2] * z

# Step 4: Output the results.
a = x  # 武馬 pulling force
b = y  # 中馬 pulling force
c = z  # 下馬 pulling force

print(f"武馬一匹力引 {a} 石，中馬一匹力引 {b} 石，下馬一匹力引 {c} 石。")


"""


---

### Explanation of the Code:
1. **Coefficients and Constants**:
   - The system of equations is represented as a matrix of coefficients and a vector of constants.
2. **Elimination**:
   - The elimination process follows the ancient Chinese method, which is similar to Gaussian elimination.
   - Each row is normalized, and variables are eliminated step by step.
3. **Back Substitution**:
   - Once the matrix is in row-echelon form, the variables are solved starting from the last equation.
4. **Output**:
   - The pulling forces of 武馬, 中馬, and 下馬 are printed as fractions for exact values.

---

### Answer:
The pulling forces are:
- 武馬: \( a \) 石.
- 中馬: \( b \) 石.
- 下馬: \( c \) 石.
"""


"""
Variable 'a' has wrong value. Expected: 160/7, Actual: 20
Variable 'b' has wrong value. Expected: 120/7, Actual: 20
Variable 'c' has wrong value. Expected: 40/7, Actual: 20"""
