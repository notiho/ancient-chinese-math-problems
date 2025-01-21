"""
今有賣牛二羊五以買十三豕有餘錢一千賣牛三豕三以買九羊錢適足賣羊六豕八以買五牛錢不足六百問牛羊豕價各幾何
術曰如方程置牛二羊五正豕一十三負餘錢數正次牛三正羊九負豕三正次牛五負羊六正豕八正不足錢負以正負術入之
方程術曰置上禾三秉中禾二秉下禾一秉實三十九斗於右方中左禾列如右方以右行上禾遍乘中行而以直除又乘其次亦以直除然以中行中禾不盡者遍乘左行而以直除左方下禾不盡者上為法下為實實即下禾之實求中禾以法乘中行下實而除下禾之實餘如中禾秉數而一即中禾之實求上禾亦以法乘右行下實而除下禾中禾之實餘如上禾秉數而一即上禾之實實皆如法各得一斗荅曰牛價 a 羊價 b 豕價 c 
"""

"""
This is a classical system of linear equations problem from ancient Chinese mathematics. The problem involves determining the prices of cows, sheep, and pigs based on three transactions. Below is the Python implementation of the solution using the described "fangcheng" (matrix elimination) method.


"""


from fractions import Fraction

# Define the coefficients of the equations
# 牛 (cows), 羊 (sheep), 豕 (pigs), and the constant term (money)
# Equation 1: 2牛 + 5羊 - 13豕 = 1000
# Equation 2: 3牛 - 9羊 + 3豕 = 0
# Equation 3: 5牛 - 6羊 - 8豕 = -600

# Coefficients matrix (left-hand side)
matrix = [
    [2, 5, -13, 1000],  # Equation 1
    [3, -9, 3, 0],      # Equation 2
    [5, -6, -8, -600]   # Equation 3
]

# Fangcheng method (Gaussian elimination)

# Step 1: Normalize the first row
for i in range(4):  # Divide the first row by the leading coefficient (2)
    matrix[0][i] = Fraction(matrix[0][i], 2)

# Step 2: Eliminate the first variable (牛) from the second and third rows
for row in range(1, 3):  # For rows 2 and 3
    factor = matrix[row][0]  # Leading coefficient of the current row
    for col in range(4):  # Subtract the scaled first row
        matrix[row][col] -= factor * matrix[0][col]

# Step 3: Normalize the second row
for i in range(1, 4):  # Divide the second row by the new leading coefficient
    matrix[1][i] = Fraction(matrix[1][i], matrix[1][1])
matrix[1][0] = 0  # The first column should now be zero

# Step 4: Eliminate the second variable (羊) from the third row
factor = matrix[2][1]  # Leading coefficient of the third row
for col in range(1, 4):  # Subtract the scaled second row
    matrix[2][col] -= factor * matrix[1][col]

# Step 5: Normalize the third row
for i in range(2, 4):  # Divide the third row by the new leading coefficient
    matrix[2][i] = Fraction(matrix[2][i], matrix[2][2])
matrix[2][0] = 0  # The first column should now be zero
matrix[2][1] = 0  # The second column should now be zero

# Step 6: Back-substitution to find the values of 豕 (pigs), 羊 (sheep), and 牛 (cows)
c = matrix[2][3]  # Value of 豕 (pigs)
b = matrix[1][3] - matrix[1][2] * c  # Value of 羊 (sheep)
a = matrix[0][3] - matrix[0][2] * c - matrix[0][1] * b  # Value of 牛 (cows)

# Final results
a = float(a)
b = float(b)
c = float(c)

print(f"牛價 a = {a}")
print(f"羊價 b = {b}")
print(f"豕價 c = {c}")


"""


### Explanation of the Code:
1. **Matrix Representation**: The problem is represented as a system of linear equations. Each row corresponds to one equation, and the last column represents the constant term.
2. **Fangcheng Method**: This is essentially Gaussian elimination, where we normalize rows and eliminate variables step by step.
3. **Back-Substitution**: After reducing the matrix to row-echelon form, we solve for the variables starting from the last row.

### Answer:
The values of `a`, `b`, and `c` represent the prices of cows, sheep, and pigs, respectively.
"""


"""
Variable 'a' has wrong value. Expected: 1200, Actual: -1931587.5
Variable 'b' has wrong value. Expected: 500, Actual: 692625.0
Variable 'c' has wrong value. Expected: 300, Actual: -30850.0"""
