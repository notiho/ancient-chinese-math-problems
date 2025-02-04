"""
今有賣牛二羊五以買十三豕有餘錢一千賣牛三豕三以買九羊錢適足賣羊六豕八以買五牛錢不足六百問牛羊豕價各幾何
術曰如方程置牛二羊五正豕一十三負餘錢數正次牛三正羊九負豕三正次牛五負羊六正豕八正不足錢負以正負術入之
方程術曰置上禾三秉中禾二秉下禾一秉實三十九斗於右方中左禾列如右方以右行上禾遍乘中行而以直除又乘其次亦以直除然以中行中禾不盡者遍乘左行而以直除左方下禾不盡者上為法下為實實即下禾之實求中禾以法乘中行下實而除下禾之實餘如中禾秉數而一即中禾之實求上禾亦以法乘右行下實而除下禾中禾之實餘如上禾秉數而一即上禾之實實皆如法各得一斗
荅曰牛價 a 羊價 b 豕價 c 
"""

"""
This is a classic system of linear equations problem from ancient Chinese mathematics. The problem involves solving for the prices of cows, sheep, and pigs based on the given transactions. Below is the Python implementation of the procedure using the ancient "fangcheng" (matrix) method.


"""


from fractions import Fraction

# Define the equations based on the problem:
# 1. Selling 2 cows and 5 sheep to buy 13 pigs, with 1000 money left over:
#    2牛 + 5羊 - 13豕 = 1000
# 2. Selling 3 cows and 3 pigs to buy 9 sheep, with no money left over:
#    3牛 - 9羊 + 3豕 = 0
# 3. Selling 6 sheep and 8 pigs to buy 5 cows, with 600 money short:
#    -5牛 + 6羊 + 8豕 = -600

# Coefficients of the equations
# Each row represents an equation: [牛, 羊, 豕, constant]
matrix = [
    [2, 5, -13, 1000],  # Equation 1
    [3, -9, 3, 0],      # Equation 2
    [-5, 6, 8, -600]    # Equation 3
]

# Step 1: Normalize the first row (make the first coefficient 1)
factor = matrix[0][0]
for i in range(len(matrix[0])):
    matrix[0][i] = Fraction(matrix[0][i], factor)

# Step 2: Eliminate the first variable (牛) from the second and third rows
for row in range(1, 3):
    factor = matrix[row][0]
    for col in range(len(matrix[row])):
        matrix[row][col] -= factor * matrix[0][col]

# Step 3: Normalize the second row (make the second coefficient 1)
factor = matrix[1][1]
for i in range(len(matrix[1])):
    matrix[1][i] = Fraction(matrix[1][i], factor)

# Step 4: Eliminate the second variable (羊) from the first and third rows
for row in [0, 2]:
    factor = matrix[row][1]
    for col in range(len(matrix[row])):
        matrix[row][col] -= factor * matrix[1][col]

# Step 5: Normalize the third row (make the third coefficient 1)
factor = matrix[2][2]
for i in range(len(matrix[2])):
    matrix[2][i] = Fraction(matrix[2][i], factor)

# Step 6: Eliminate the third variable (豕) from the first and second rows
for row in [0, 1]:
    factor = matrix[row][2]
    for col in range(len(matrix[row])):
        matrix[row][col] -= factor * matrix[2][col]

# The results are now in the last column of the matrix
a = matrix[0][3]  # 牛價
b = matrix[1][3]  # 羊價
c = matrix[2][3]  # 豕價

# Output the results
a, b, c


"""


### Explanation of the Code:
1. **Matrix Representation**: The equations are represented as a matrix where each row corresponds to an equation, and each column corresponds to a variable or the constant term.
2. **Normalization and Elimination**: The procedure follows the ancient "fangcheng" method, which is essentially Gaussian elimination. It involves normalizing rows and eliminating variables step by step.
3. **Final Results**: After the elimination process, the last column of the matrix contains the solutions for the variables (prices of cows, sheep, and pigs).

### Answer:
The prices of the cow, sheep, and pig are:
- 牛價 (price of a cow): `a`
- 羊價 (price of a sheep): `b`
- 豕價 (price of a pig): `c`
"""


"""
"""
