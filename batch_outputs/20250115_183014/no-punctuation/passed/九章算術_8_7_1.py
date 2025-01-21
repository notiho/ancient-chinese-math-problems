"""
今有賣牛二羊五以買十三豕有餘錢一千賣牛三豕三以買九羊錢適足賣羊六豕八以買五牛錢不足六百問牛羊豕價各幾何
術曰如方程置牛二羊五正豕一十三負餘錢數正次牛三正羊九負豕三正次牛五負羊六正豕八正不足錢負以正負術入之
方程術曰置上禾三秉中禾二秉下禾一秉實三十九斗於右方中左禾列如右方以右行上禾遍乘中行而以直除又乘其次亦以直除然以中行中禾不盡者遍乘左行而以直除左方下禾不盡者上為法下為實實即下禾之實求中禾以法乘中行下實而除下禾之實餘如中禾秉數而一即中禾之實求上禾亦以法乘右行下實而除下禾中禾之實餘如上禾秉數而一即上禾之實實皆如法各得一斗荅曰牛價 a 羊價 b 豕價 c 
"""

"""
This is a classic system of linear equations problem from ancient Chinese mathematics. The problem involves determining the prices of cows, sheep, and pigs based on three transactions. Below is the translation of the problem and its solution into Python code, following the structure of the procedure ("術") provided.


"""


from fractions import Fraction

# 賣牛二羊五以買十三豕有餘錢一千
# Equation 1: 2牛 + 5羊 - 13豕 = 1000
eq1 = [2, 5, -13, 1000]

# 賣牛三豕三以買九羊錢適足
# Equation 2: 3牛 - 9羊 + 3豕 = 0
eq2 = [3, -9, 3, 0]

# 賣羊六豕八以買五牛錢不足六百
# Equation 3: -5牛 + 6羊 + 8豕 = -600
eq3 = [-5, 6, 8, -600]

# 方程術
# Step 1: Arrange the equations into a matrix form
matrix = [eq1, eq2, eq3]

# Step 2: Eliminate variables using the method described in the 方程術
# Normalize the first row
factor1 = matrix[0][0]
matrix[0] = [Fraction(x, factor1) for x in matrix[0]]

# Eliminate the first variable from the second and third rows
factor2 = matrix[1][0]
matrix[1] = [matrix[1][i] - factor2 * matrix[0][i] for i in range(4)]

factor3 = matrix[2][0]
matrix[2] = [matrix[2][i] - factor3 * matrix[0][i] for i in range(4)]

# Normalize the second row
factor4 = matrix[1][1]
matrix[1] = [Fraction(x, factor4) for x in matrix[1]]

# Eliminate the second variable from the third row
factor5 = matrix[2][1]
matrix[2] = [matrix[2][i] - factor5 * matrix[1][i] for i in range(4)]

# Normalize the third row
factor6 = matrix[2][2]
matrix[2] = [Fraction(x, factor6) for x in matrix[2]]

# Step 3: Back-substitute to solve for the variables
c = matrix[2][3]  # 豕價 (price of pigs)
b = matrix[1][3] - matrix[1][2] * c  # 羊價 (price of sheep)
a = matrix[0][3] - matrix[0][2] * c - matrix[0][1] * b  # 牛價 (price of cows)

# Output the results
a, b, c


"""


### Explanation of the Code:
1. **Equations Setup**: The three transactions are translated into equations:
   - `2牛 + 5羊 - 13豕 = 1000`
   - `3牛 - 9羊 + 3豕 = 0`
   - `-5牛 + 6羊 + 8豕 = -600`

2. **Matrix Representation**: The equations are represented as a matrix for systematic elimination.

3. **Gaussian Elimination**: The procedure described in the 方程術 is essentially Gaussian elimination:
   - Normalize the rows by dividing by the leading coefficient.
   - Eliminate variables from subsequent rows.
   - Back-substitute to solve for the variables.

4. **Results**: The final values of `a`, `b`, and `c` represent the prices of cows, sheep, and pigs, respectively.

### Answer:
The prices of the animals are:
- 牛價 (price of cows): `a`
- 羊價 (price of sheep): `b`
- 豕價 (price of pigs): `c`
"""


"""
"""
