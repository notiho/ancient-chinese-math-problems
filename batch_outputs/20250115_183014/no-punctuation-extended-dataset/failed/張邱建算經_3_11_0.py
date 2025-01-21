"""
今有上錦三疋中錦二疋下錦一疋直絹四十五疋上錦二疋中錦三疋下錦一疋直絹四十三疋上錦一疋中錦二疋下錦三疋直絹三十五疋問上中下錦各直絹幾何
術曰如方程
方程術曰置上禾三秉中禾二秉下禾一秉實三十九斗於右方中左禾列如右方以右行上禾遍乘中行而以直除又乘其次亦以直除然以中行中禾不盡者遍乘左行而以直除左方下禾不盡者上為法下為實實即下禾之實求中禾以法乘中行下實而除下禾之實餘如中禾秉數而一即中禾之實求上禾亦以法乘右行下實而除下禾中禾之實餘如上禾秉數而一即上禾之實實皆如法各得一斗答曰上錦 a疋 直絹 b疋 中錦 c疋 直絹 d疋 下錦 e疋 直絹 f疋
"""

"""
This problem involves solving a system of linear equations, which is described in the ancient Chinese mathematical text as "方程術" (method of solving simultaneous equations). The problem can be translated into a system of equations based on the relationships provided. Let's solve it step by step.

### Problem Restatement:
We are given:
1. 3 units of upper brocade, 2 units of middle brocade, and 1 unit of lower brocade are worth 45 bolts of plain silk.
2. 2 units of upper brocade, 3 units of middle brocade, and 1 unit of lower brocade are worth 43 bolts of plain silk.
3. 1 unit of upper brocade, 2 units of middle brocade, and 3 units of lower brocade are worth 35 bolts of plain silk.

We need to find the value of each type of brocade (upper, middle, and lower) in terms of bolts of plain silk.

---

### Procedure:
The method described in the text is essentially Gaussian elimination. Let's solve it step by step.

---


"""


from fractions import Fraction

# Coefficients of the equations
# 3a + 2b + 1c = 45
# 2a + 3b + 1c = 43
# 1a + 2b + 3c = 35

# Step 1: Represent the equations as a matrix
matrix = [
    [3, 2, 1, 45],  # First equation
    [2, 3, 1, 43],  # Second equation
    [1, 2, 3, 35]   # Third equation
]

# Step 2: Normalize the first row (make the leading coefficient 1)
factor = matrix[0][0]
matrix[0] = [Fraction(x, factor) for x in matrix[0]]

# Step 3: Eliminate the first variable from the second and third rows
for i in range(1, 3):
    factor = matrix[i][0]
    matrix[i] = [matrix[i][j] - factor * matrix[0][j] for j in range(4)]

# Step 4: Normalize the second row (make the leading coefficient of the second variable 1)
factor = matrix[1][1]
matrix[1] = [Fraction(x, factor) for x in matrix[1]]

# Step 5: Eliminate the second variable from the first and third rows
for i in [0, 2]:
    factor = matrix[i][1]
    matrix[i] = [matrix[i][j] - factor * matrix[1][j] for j in range(4)]

# Step 6: Normalize the third row (make the leading coefficient of the third variable 1)
factor = matrix[2][2]
matrix[2] = [Fraction(x, factor) for x in matrix[2]]

# Step 7: Eliminate the third variable from the first and second rows
for i in [0, 1]:
    factor = matrix[i][2]
    matrix[i] = [matrix[i][j] - factor * matrix[2][j] for j in range(4)]

# The matrix is now in reduced row-echelon form, and the solutions are:
a = matrix[0][3]  # Value of upper brocade
b = matrix[1][3]  # Value of middle brocade
c = matrix[2][3]  # Value of lower brocade

# Output the results
a, b, c


"""


---

### Explanation of the Code:
1. **Matrix Representation**: The system of equations is represented as an augmented matrix, where each row corresponds to an equation.
2. **Row Operations**: The procedure involves normalizing rows and eliminating variables step by step, following the ancient method described in the text.
3. **Final Solution**: The reduced row-echelon form of the matrix gives the values of the variables directly.

---

### Answer:
The values of the brocades in terms of bolts of plain silk are:
- Upper brocade: `a` bolts
- Middle brocade: `b` bolts
- Lower brocade: `c` bolts
"""


"""
Variable 'a' has wrong value. Expected: 1, Actual: 9
Variable 'b' has wrong value. Expected: 9, Actual: 7
Variable 'c' has wrong value. Expected: 1, Actual: 4
Missing variable in output: 'd'
Missing variable in output: 'e'
Missing variable in output: 'f'"""
