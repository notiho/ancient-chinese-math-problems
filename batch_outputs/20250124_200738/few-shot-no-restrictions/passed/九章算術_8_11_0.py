"""
今有武馬一匹，中馬二匹，下馬三匹，皆載四十石至阪，皆不能上。武馬借中馬一匹，中馬借下馬一匹，下馬借武馬一匹，乃皆上。問︰武、中、下馬一匹各力引幾何？
術曰：如方程各置所借，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：武馬一匹力引 a石 ，中馬一匹力引 b石 ，下馬一匹力引 c石 。
"""

"""
This is a classic problem from ancient Chinese mathematics, specifically from the "Nine Chapters on the Mathematical Art" (九章算術). It involves solving a system of linear equations using a method similar to Gaussian elimination. Let's translate the problem and solution into Python code.

---

### Problem:
There are three types of horses:
- 1 Wu horse (武馬),
- 2 Zhong horses (中馬),
- 3 Xia horses (下馬).

Each horse is tasked with carrying 40 shi (石) of weight up a slope, but none of them can do it alone. To solve this:
- The Wu horse borrows 1 Zhong horse.
- The Zhong horse borrows 1 Xia horse.
- The Xia horse borrows 1 Wu horse.

With this arrangement, all horses can carry the weight up the slope. The question is: how much pulling force (in shi) does each type of horse contribute?

---

### Solution:
The procedure involves setting up a system of linear equations based on the borrowing relationships and solving it using elimination.

---

### Python Code:


"""

#----- content starts here -----

from fractions import Fraction

# Define the system of equations:
# Let:
#   a = pulling force of 1 Wu horse (武馬)
#   b = pulling force of 1 Zhong horse (中馬)
#   c = pulling force of 1 Xia horse (下馬)

# Equations based on the problem:
# 1. Wu horse + 1 Zhong horse = 40 shi
# 2. 2 Zhong horses + 1 Xia horse = 40 shi
# 3. 3 Xia horses + 1 Wu horse = 40 shi

# Represent the equations as a matrix:
# Coefficients of a, b, c and the constants on the right-hand side
matrix = [
    [1, 1, 0, 40],  # Wu + Zhong = 40
    [0, 2, 1, 40],  # 2 Zhong + Xia = 40
    [1, 0, 3, 40]   # Wu + 3 Xia = 40
]

# Perform Gaussian elimination to solve the system of equations
def gaussian_elimination(matrix):
    n = len(matrix)
    
    # Forward elimination
    for i in range(n):
        # Normalize the pivot row
        pivot = matrix[i][i]
        for j in range(i, n + 1):
            matrix[i][j] = Fraction(matrix[i][j], pivot)
        
        # Eliminate the current variable from the rows below
        for k in range(i + 1, n):
            factor = matrix[k][i]
            for j in range(i, n + 1):
                matrix[k][j] -= factor * matrix[i][j]
    
    # Back substitution
    solution = [0] * n
    for i in range(n - 1, -1, -1):
        solution[i] = matrix[i][n]
        for j in range(i + 1, n):
            solution[i] -= matrix[i][j] * solution[j]
    
    return solution

# Solve the system
solution = gaussian_elimination(matrix)

# Extract the results
a, b, c = solution

# Output the results
print(f"武馬一匹力引 {a} 石")
print(f"中馬一匹力引 {b} 石")
print(f"下馬一匹力引 {c} 石")
#----- content ends here -----


"""


---

### Explanation of the Code:
1. **Matrix Representation**:
   - Each row in the matrix represents one of the equations.
   - The last column contains the constants on the right-hand side of the equations.

2. **Gaussian Elimination**:
   - The forward elimination step transforms the matrix into an upper triangular form.
   - The back substitution step solves for the variables starting from the last row.

3. **Fractions**:
   - The `Fraction` class is used to ensure exact arithmetic throughout the calculations.

---

### Answer:
After running the code, the results will be:
- 武馬 (Wu horse) pulls `a` shi.
- 中馬 (Zhong horse) pulls `b` shi.
- 下馬 (Xia horse) pulls `c` shi.

This approach ensures the solution is accurate and follows the ancient method described in the problem.
"""


"""
"""
