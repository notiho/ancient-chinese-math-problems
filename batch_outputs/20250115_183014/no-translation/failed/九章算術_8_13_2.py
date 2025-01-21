"""
今有白禾二步、青禾三步、黃禾四步、黑禾五步，實各不滿斗。白取青、黃，青取黃、黑，黃取黑、白，黑取白、青，各一步，而實滿斗。問︰白、青、黃、黑禾實一步各幾何？
術曰：如方程，各置所取，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：白禾 a步 實 b斗 ，青禾 c步 實 d斗 ，黃禾 e步 實 f斗 ，黑禾 g步 實 h斗 。
"""

"""
This problem involves solving a system of linear equations using ancient Chinese mathematical methods, which is essentially Gaussian elimination. Let's translate the procedure into Python code step by step.

### Problem Setup:
We have four types of grain (白禾, 青禾, 黃禾, 黑禾) with their respective steps and relationships. Each type of grain contributes a certain amount to the total when combined with others, and we need to determine the amount of grain per step for each type.


"""


from fractions import Fraction

# Step 1: Define the coefficients of the equations based on the problem statement.
# Each row corresponds to the equation for one type of grain.
# Columns represent 白禾, 青禾, 黃禾, 黑禾, and the constant term (total contribution to a full斗).

# Coefficients of the equations
matrix = [
    [1, -1, -1, 0, 1],  # 白禾 equation: 白 - 青 - 黃 = 1
    [0, 1, -1, -1, 1],  # 青禾 equation: 青 - 黃 - 黑 = 1
    [-1, 0, 1, -1, 1],  # 黃禾 equation: 黃 - 黑 - 白 = 1
    [-1, -1, 0, 1, 1]   # 黑禾 equation: 黑 - 白 - 青 = 1
]

# Step 2: Perform Gaussian elimination to solve the system of equations.

# Forward elimination
for i in range(4):  # Iterate over each row
    # Normalize the pivot row
    pivot = matrix[i][i]
    for j in range(5):  # Normalize all elements in the row
        matrix[i][j] = Fraction(matrix[i][j], pivot)
    
    # Eliminate the current variable from the rows below
    for k in range(i + 1, 4):
        factor = matrix[k][i]
        for j in range(5):
            matrix[k][j] -= factor * matrix[i][j]

# Back substitution
results = [0] * 4
for i in range(3, -1, -1):  # Start from the last row and move upwards
    results[i] = matrix[i][4]
    for j in range(i + 1, 4):
        results[i] -= matrix[i][j] * results[j]

# Step 3: Extract the results for each type of grain.
a, b = 2, results[0]  # 白禾: 2 steps, 实 b斗
c, d = 3, results[1]  # 青禾: 3 steps, 实 d斗
e, f = 4, results[2]  # 黃禾: 4 steps, 实 f斗
g, h = 5, results[3]  # 黑禾: 5 steps, 实 h斗

# Output the results
print(f"白禾 {a}步 实 {b}斗")
print(f"青禾 {c}步 实 {d}斗")
print(f"黃禾 {e}步 实 {f}斗")
print(f"黑禾 {g}步 实 {h}斗")


"""


### Explanation:
1. **Matrix Setup**: The problem is translated into a system of linear equations, where each equation represents the relationship between the grains.
2. **Gaussian Elimination**: The system is solved using forward elimination and back substitution, as described in the ancient Chinese method.
3. **Results Extraction**: The solution gives the amount of grain per step for each type.

### Final Answer:
The output will provide the number of steps and the corresponding amount of grain for 白禾, 青禾, 黃禾, and 黑禾.
"""


"""
Variable 'a' has wrong value. Expected: 1, Actual: 2
Variable 'b' has wrong value. Expected: 11/37, Actual: -1
Variable 'c' has wrong value. Expected: 1, Actual: 3
Variable 'd' has wrong value. Expected: 28/111, Actual: -1
Variable 'e' has wrong value. Expected: 1, Actual: 4
Variable 'f' has wrong value. Expected: 17/111, Actual: -1
Variable 'g' has wrong value. Expected: 1, Actual: 5
Variable 'h' has wrong value. Expected: 10/111, Actual: -1"""
