"""
今有武馬一匹中馬二匹下馬三匹皆載四十石至阪皆不能上武馬借中馬一匹中馬借下馬一匹下馬借武馬一匹乃皆上問武中下馬一匹各力引幾何
術曰如方程各置所借以正負術入之
方程術曰置上禾三秉中禾二秉下禾一秉實三十九斗於右方中左禾列如右方以右行上禾遍乘中行而以直除又乘其次亦以直除然以中行中禾不盡者遍乘左行而以直除左方下禾不盡者上為法下為實實即下禾之實求中禾以法乘中行下實而除下禾之實餘如中禾秉數而一即中禾之實求上禾亦以法乘右行下實而除下禾中禾之實餘如上禾秉數而一即上禾之實實皆如法各得一斗荅曰武馬 a匹 力引 b石 中馬 c匹 力引 d石 下馬 e匹 力引 f石 
"""

"""
This problem involves solving a system of equations using an ancient Chinese method akin to Gaussian elimination. The problem describes three types of horses (武馬, 中馬, 下馬) with different pulling capacities. Each horse type borrows another horse to help carry a load of 40 shi up a slope, and the goal is to determine the pulling capacity of each horse type.

The procedure (術) describes how to set up and solve the system of equations using the "方程術" (method of equations). Below is the Python implementation of the procedure:


"""


from fractions import Fraction

# Define the total load each horse type must pull
total_load = 40  # in 石

# Define the number of horses of each type
武馬_count = 1
中馬_count = 2
下馬_count = 3

# Define the borrowing relationships and their equations
# 武馬借中馬一匹, 中馬借下馬一匹, 下馬借武馬一匹
# Let 武馬 = a, 中馬 = b, 下馬 = c (their pulling capacities in 石)
# The equations are:
# 1. 武馬 + 中馬 = 40
# 2. 中馬 + 下馬 = 40
# 3. 下馬 + 武馬 = 40

# Set up the system of equations as a matrix
# Coefficients of a, b, c and the constants on the right-hand side
matrix = [
    [1, 1, 0, total_load],  # 武馬 + 中馬 = 40
    [0, 1, 1, total_load],  # 中馬 + 下馬 = 40
    [1, 0, 1, total_load],  # 下馬 + 武馬 = 40
]

# Solve the system of equations using the 方程術
# Step 1: Eliminate the first variable (武馬) from the second and third equations
factor1 = Fraction(matrix[1][0], matrix[0][0])
matrix[1] = [matrix[1][i] - factor1 * matrix[0][i] for i in range(4)]

factor2 = Fraction(matrix[2][0], matrix[0][0])
matrix[2] = [matrix[2][i] - factor2 * matrix[0][i] for i in range(4)]

# Step 2: Eliminate the second variable (中馬) from the third equation
factor3 = Fraction(matrix[2][1], matrix[1][1])
matrix[2] = [matrix[2][i] - factor3 * matrix[1][i] for i in range(4)]

# Step 3: Back-substitute to find the values of 下馬, 中馬, and 武馬
下馬 = Fraction(matrix[2][3], matrix[2][2])
中馬 = Fraction(matrix[1][3] - matrix[1][2] * 下馬, matrix[1][1])
武馬 = Fraction(matrix[0][3] - matrix[0][1] * 中馬 - matrix[0][2] * 下馬, matrix[0][0])

# Output the results
a = 武馬
b = 武馬  # 武馬 pulling capacity in 石
c = 中馬
d = 中馬  # 中馬 pulling capacity in 石
e = 下馬
f = 下馬  # 下馬 pulling capacity in 石

print(f"武馬 {a}匹 力引 {b}石")
print(f"中馬 {c}匹 力引 {d}石")
print(f"下馬 {e}匹 力引 {f}石")


"""


### Explanation of the Code:
1. **Matrix Setup**: The system of equations is represented as a matrix, where each row corresponds to an equation, and each column corresponds to a variable or the constant term.
2. **Elimination**: The 方程術 describes a process similar to Gaussian elimination, where variables are eliminated step-by-step to solve for the remaining variables.
3. **Back-Substitution**: Once the matrix is in row-echelon form, the variables are solved starting from the last equation and substituting back into the earlier equations.
4. **Results**: The pulling capacities of 武馬, 中馬, and 下馬 are calculated and displayed.

### Answer:
武馬 `a`匹 力引 `b`石  
中馬 `c`匹 力引 `d`石  
下馬 `e`匹 力引 `f`石
"""


"""
Variable 'a' has wrong value. Expected: 1, Actual: 20
Variable 'b' has wrong value. Expected: 160/7, Actual: 20
Variable 'c' has wrong value. Expected: 1, Actual: 20
Variable 'd' has wrong value. Expected: 120/7, Actual: 20
Variable 'e' has wrong value. Expected: 1, Actual: 20
Variable 'f' has wrong value. Expected: 40/7, Actual: 20"""
