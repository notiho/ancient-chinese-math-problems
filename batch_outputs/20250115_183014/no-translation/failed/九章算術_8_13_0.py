"""
今有白禾二步、青禾三步、黃禾四步、黑禾五步，實各不滿斗。白取青、黃，青取黃、黑，黃取黑、白，黑取白、青，各一步，而實滿斗。問︰白、青、黃、黑禾實一步各幾何？
術曰：如方程，各置所取，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：白禾 a步 實 b斗 ，青禾 c步 實 d斗 ，黃禾 e步 實 f斗 ，黑禾 g步 實 h斗 。
"""

"""
This problem involves solving a system of linear equations, which is described in the ancient Chinese method of elimination. Below is the Python implementation of the described procedure:


"""


from fractions import Fraction

# Step 1: Define the coefficients of the equations based on the problem
# White (白禾), Green (青禾), Yellow (黃禾), Black (黑禾)
# Each row corresponds to an equation, and each column corresponds to a variable (禾步).
# The last column represents the total (實滿斗).

equations = [
    [1, 1, 1, 0, 1],  # 白禾取青、黃
    [0, 1, 1, 1, 1],  # 青禾取黃、黑
    [1, 0, 1, 1, 1],  # 黃禾取黑、白
    [1, 1, 0, 1, 1],  # 黑禾取白、青
]

# Step 2: Perform Gaussian elimination to solve the system of equations
# Normalize the first row
for i in range(4):
    factor = equations[i][i]
    for j in range(5):
        equations[i][j] = Fraction(equations[i][j], factor)
    # Eliminate the variable in other rows
    for k in range(4):
        if k != i:
            factor = equations[k][i]
            for j in range(5):
                equations[k][j] -= factor * equations[i][j]

# Step 3: Extract the results
a, b = 1, equations[0][4]  # 白禾步數 and 實
c, d = 1, equations[1][4]  # 青禾步數 and 實
e, f = 1, equations[2][4]  # 黃禾步數 and 實
g, h = 1, equations[3][4]  # 黑禾步數 and 實

# Results
print(f"白禾 {a}步 實 {b}斗")
print(f"青禾 {c}步 實 {d}斗")
print(f"黃禾 {e}步 實 {f}斗")
print(f"黑禾 {g}步 實 {h}斗")


"""


### Explanation of the Code:
1. **Equations Setup**: The coefficients of the equations are set up based on the problem description. Each row represents an equation, and the last column represents the total (實滿斗).
2. **Gaussian Elimination**: The system of equations is solved using the method of Gaussian elimination, as described in the ancient Chinese text.
3. **Results Extraction**: After solving, the values for each variable (禾步 and 實) are extracted and displayed.

### Results:
The output will provide the number of steps (步) and the actual amount (實) for each type of grain (白禾, 青禾, 黃禾, 黑禾).
"""


"""
Variable 'b' has wrong value. Expected: 11/37, Actual: 1/3
Variable 'd' has wrong value. Expected: 28/111, Actual: 1/3
Variable 'f' has wrong value. Expected: 17/111, Actual: 1/3
Variable 'h' has wrong value. Expected: 10/111, Actual: 1/3"""
