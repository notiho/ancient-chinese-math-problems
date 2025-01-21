"""
今有令一人、吏五人、從者一十人，食雞一十；令一十人、吏一人、從者五人，食雞八；令五人、吏一十人、從者一人，食雞六。問︰令、吏、從者食雞各幾何？
術曰：如方程，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：令 a人 食 b雞 ，吏 c人 食 d雞 ，從者 e人 食 f雞 。
"""

"""
This problem involves solving a system of linear equations using the ancient Chinese method of elimination, which is similar to Gaussian elimination. The problem can be translated into a system of equations based on the given information about the number of people and the chickens they consume.

### Problem Setup:
Let:
- \( x \): the number of chickens consumed by one "令" (official).
- \( y \): the number of chickens consumed by one "吏" (clerk).
- \( z \): the number of chickens consumed by one "從者" (attendant).

From the problem, we have the following equations:
1. \( 1x + 5y + 10z = 10 \)
2. \( 10x + 1y + 5z = 8 \)
3. \( 5x + 10y + 1z = 6 \)

We will solve this system using the elimination method described in the "方程術".

---

### Step 1: Represent the equations in matrix form
The system can be written as:
\[
\begin{bmatrix}
1 & 5 & 10 \\
10 & 1 & 5 \\
5 & 10 & 1
\end{bmatrix}
\begin{bmatrix}
x \\
y \\
z
\end{bmatrix}
=
\begin{bmatrix}
10 \\
8 \\
6
\end{bmatrix}
\]

---

### Step 2: Implement the elimination process in Python


"""


from fractions import Fraction

# Coefficients of the equations
matrix = [
    [1, 5, 10, 10],  # 1x + 5y + 10z = 10
    [10, 1, 5, 8],   # 10x + 1y + 5z = 8
    [5, 10, 1, 6]    # 5x + 10y + 1z = 6
]

# Step 1: Normalize the first row
for i in range(4):
    matrix[0][i] = Fraction(matrix[0][i], matrix[0][0])

# Step 2: Eliminate the first variable (x) from the second and third rows
for i in range(1, 3):
    factor = matrix[i][0]
    for j in range(4):
        matrix[i][j] -= factor * matrix[0][j]

# Step 3: Normalize the second row
for i in range(1, 4):
    matrix[1][i] = Fraction(matrix[1][i], matrix[1][1])

# Step 4: Eliminate the second variable (y) from the third row
factor = matrix[2][1]
for i in range(1, 4):
    matrix[2][i] -= factor * matrix[1][i]

# Step 5: Solve for z
z = Fraction(matrix[2][3], matrix[2][2])

# Step 6: Solve for y
y = matrix[1][3] - matrix[1][2] * z

# Step 7: Solve for x
x = matrix[0][3] - matrix[0][2] * z - matrix[0][1] * y

# Results
a, b = 1, x
c, d = 5, y
e, f = 10, z

print(f"令 {a}人 食 {b}雞 ，吏 {c}人 食 {d}雞 ，從者 {e}人 食 {f}雞 。")


"""


---

### Explanation of the Code:
1. **Matrix Representation**: The coefficients of the equations are stored in a matrix, with the last column representing the constants on the right-hand side of the equations.
2. **Normalization**: Each row is normalized by dividing through by the leading coefficient to simplify the elimination process.
3. **Elimination**: Variables are eliminated step by step, starting with \( x \), then \( y \), leaving a single equation for \( z \).
4. **Back Substitution**: Once \( z \) is found, substitute it back into the previous rows to find \( y \), and then \( x \).

---

### Final Answer:
The solution will output the number of chickens consumed by each type of person.
"""


"""
Variable 'b' has wrong value. Expected: 45/122, Actual: 1070/737
Variable 'c' has wrong value. Expected: 1, Actual: 5
Variable 'd' has wrong value. Expected: 41/122, Actual: -164/737
Variable 'e' has wrong value. Expected: 1, Actual: 10
Variable 'f' has wrong value. Expected: 97/122, Actual: 712/737"""
