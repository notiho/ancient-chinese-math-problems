"""
今有賣牛二羊五以買十三豕有餘錢一千賣牛三豕三以買九羊錢適足賣羊六豕八以買五牛錢不足六百問牛羊豕價各幾何
術曰如方程置牛二羊五正豕一十三負餘錢數正次牛三正羊九負豕三正次牛五負羊六正豕八正不足錢負以正負術入之
方程術曰置上禾三秉中禾二秉下禾一秉實三十九斗於右方中左禾列如右方以右行上禾遍乘中行而以直除又乘其次亦以直除然以中行中禾不盡者遍乘左行而以直除左方下禾不盡者上為法下為實實即下禾之實求中禾以法乘中行下實而除下禾之實餘如中禾秉數而一即中禾之實求上禾亦以法乘右行下實而除下禾中禾之實餘如上禾秉數而一即上禾之實實皆如法各得一斗荅曰牛價 a 羊價 b 豕價 c 
"""

"""
This problem involves solving a system of linear equations to determine the prices of cows, sheep, and pigs. The ancient Chinese method for solving such problems is known as the "fangcheng" (方程) method, which is essentially an early form of Gaussian elimination. Below is the translation of the problem and its solution into Python code.

### Problem Translation:
"""
Suppose:
- Selling 2 cows and 5 sheep to buy 13 pigs leaves 1000 qian.
- Selling 3 cows and 3 pigs to buy 9 sheep results in no leftover money.
- Selling 6 sheep and 8 pigs to buy 5 cows results in a shortage of 600 qian.

Question: What are the prices of cows, sheep, and pigs?

Procedure:
1. Represent the relationships as equations:
   - 2牛 + 5羊 - 13豕 = 1000
   - 3牛 - 9羊 + 3豕 = 0
   - 5牛 - 6羊 - 8豕 = -600
2. Use the fangcheng method to solve the system of equations:
   - Place the coefficients of 牛 (cows), 羊 (sheep), and 豕 (pigs) in rows, along with the constants on the right-hand side.
   - Perform row operations to reduce the system to upper triangular form.
   - Solve for each variable starting from the bottom row.

Answer: 牛價 (price of a cow) = *a*, 羊價 (price of a sheep) = *b*, 豕價 (price of a pig) = *c*.
"""

### Python Code Implementation:


"""


from fractions import Fraction

# Coefficients of the equations
# Equation 1: 2牛 + 5羊 - 13豕 = 1000
# Equation 2: 3牛 - 9羊 + 3豕 = 0
# Equation 3: 5牛 - 6羊 - 8豕 = -600

# Initialize the matrix (augmented matrix for the system of equations)
matrix = [
    [2, 5, -13, 1000],  # Row 1
    [3, -9, 3, 0],      # Row 2
    [5, -6, -8, -600]   # Row 3
]

# Step 1: Normalize the first row
factor = matrix[0][0]
matrix[0] = [Fraction(x, factor) for x in matrix[0]]

# Step 2: Eliminate the first variable (牛) from the second and third rows
for i in range(1, 3):
    factor = matrix[i][0]
    matrix[i] = [matrix[i][j] - factor * matrix[0][j] for j in range(4)]

# Step 3: Normalize the second row
factor = matrix[1][1]
matrix[1] = [Fraction(x, factor) for x in matrix[1]]

# Step 4: Eliminate the second variable (羊) from the third row
factor = matrix[2][1]
matrix[2] = [matrix[2][j] - factor * matrix[1][j] for j in range(4)]

# Step 5: Solve for the third variable (豕)
c = Fraction(matrix[2][3], matrix[2][2])

# Step 6: Back-substitute to solve for the second variable (羊)
b = Fraction(matrix[1][3] - matrix[1][2] * c, matrix[1][1])

# Step 7: Back-substitute to solve for the first variable (牛)
a = Fraction(matrix[0][3] - matrix[0][2] * c - matrix[0][1] * b, matrix[0][0])

# Output the results
a, b, c  # 牛價, 羊價, 豕價


"""


### Explanation of the Code:
1. **Matrix Representation**: The system of equations is represented as an augmented matrix, where each row corresponds to an equation, and the last column contains the constants.
2. **Row Operations**: The fangcheng method involves normalizing rows and eliminating variables step by step to reduce the matrix to upper triangular form.
3. **Back-Substitution**: Once the matrix is in upper triangular form, the variables are solved starting from the last row and substituting the results back into the previous rows.
4. **Fractions**: The `Fraction` class is used to ensure exact arithmetic, as required by the ancient Chinese method.

### Answer:
The variables `a`, `b`, and `c` represent the prices of cows, sheep, and pigs, respectively.
"""


"""
Variable 'a' has wrong value. Expected: 1200, Actual: 6300
Variable 'b' has wrong value. Expected: 500, Actual: 2750
Variable 'c' has wrong value. Expected: 300, Actual: 1950"""
