"""
今有上禾三秉中禾二秉下禾一秉實三十九斗上禾二秉中禾三秉下禾一秉實三十四斗上禾一秉中禾二秉下禾三秉實二十六斗問上中下禾實一秉各幾何
方程術曰置上禾三秉中禾二秉下禾一秉實三十九斗於右方中左禾列如右方以右行上禾遍乘中行而以直除又乘其次亦以直除然以中行中禾不盡者遍乘左行而以直除左方下禾不盡者上為法下為實實即下禾之實求中禾以法乘中行下實而除下禾之實餘如中禾秉數而一即中禾之實求上禾亦以法乘右行下實而除下禾中禾之實餘如上禾秉數而一即上禾之實實皆如法各得一斗
荅曰上禾 a秉  b斗 中禾 c秉  d斗 下禾 e秉  f斗 
"""

"""
This problem involves solving a system of linear equations using ancient Chinese mathematical procedures described in the "fangcheng" (method of solving systems of linear equations). Let's translate the problem into Python code step by step.

The problem involves three types of grain bundles (上禾, 中禾, 下禾) and their respective contributions to the total amount of grain. We are tasked with finding how much grain (斗) each type of bundle contributes per unit (秉).

### Problem Setup:
1. **Equations:**
   - \( 3 \cdot 上禾 + 2 \cdot 中禾 + 1 \cdot 下禾 = 39 \) (斗)
   - \( 2 \cdot 上禾 + 3 \cdot 中禾 + 1 \cdot 下禾 = 34 \) (斗)
   - \( 1 \cdot 上禾 + 2 \cdot 中禾 + 3 \cdot 下禾 = 26 \) (斗)

2. **Goal:**
   Solve for the grain contribution per bundle (秉) for 上禾, 中禾, and 下禾.

### Procedure:
The "fangcheng" method involves systematically eliminating variables by multiplying rows and subtracting them to isolate each variable. Let's implement this step by step in Python.


"""


from fractions import Fraction

# Coefficients of the equations
# 3 * 上禾 + 2 * 中禾 + 1 * 下禾 = 39
# 2 * 上禾 + 3 * 中禾 + 1 * 下禾 = 34
# 1 * 上禾 + 2 * 中禾 + 3 * 下禾 = 26

# Initialize the matrix (augmented form)
matrix = [
    [3, 2, 1, 39],  # Row 1
    [2, 3, 1, 34],  # Row 2
    [1, 2, 3, 26]   # Row 3
]

# Step 1: Normalize the first row by dividing by the coefficient of 上禾 (3)
for i in range(len(matrix[0])):
    matrix[0][i] = Fraction(matrix[0][i], 3)

# Step 2: Eliminate 上禾 from the second and third rows
for i in range(len(matrix[1])):
    matrix[1][i] = matrix[1][i] - matrix[0][i] * 2  # Subtract 2 * Row 1 from Row 2
    matrix[2][i] = matrix[2][i] - matrix[0][i] * 1  # Subtract 1 * Row 1 from Row 3

# Step 3: Normalize the second row by dividing by the coefficient of 中禾 (Fraction(5, 3))
for i in range(len(matrix[1])):
    matrix[1][i] = Fraction(matrix[1][i], Fraction(5, 3))

# Step 4: Eliminate 中禾 from the third row
for i in range(len(matrix[2])):
    matrix[2][i] = matrix[2][i] - matrix[1][i] * Fraction(4, 5)

# Step 5: Solve for 下禾 (last variable)
下禾 = matrix[2][3] / matrix[2][2]

# Step 6: Back-substitute to solve for 中禾
中禾 = (matrix[1][3] - matrix[1][2] * 下禾) / matrix[1][1]

# Step 7: Back-substitute to solve for 上禾
上禾 = (matrix[0][3] - matrix[0][2] * 下禾 - matrix[0][1] * 中禾) / matrix[0][0]

# Results
a, b = 1, 上禾  # 上禾: 1秉 contributes b斗
c, d = 1, 中禾  # 中禾: 1秉 contributes d斗
e, f = 1, 下禾  # 下禾: 1秉 contributes f斗

print(f"上禾 {a}秉 {b}斗")
print(f"中禾 {c}秉 {d}斗")
print(f"下禾 {e}秉 {f}斗")


"""


### Explanation of the Code:
1. **Matrix Representation:** The system of equations is represented as an augmented matrix.
2. **Row Operations:** The fangcheng method involves normalizing rows and eliminating variables systematically.
3. **Back-Substitution:** Once the last variable is isolated, we substitute back to find the others.

### Answer:
The output will provide the grain contribution per bundle (斗) for 上禾, 中禾, and 下禾.
"""


"""
Variable 'b' has wrong value. Expected: 37/4, Actual: 1705/188
Variable 'd' has wrong value. Expected: 17/4, Actual: 765/188
Variable 'f' has wrong value. Expected: 11/4, Actual: 687/188"""
