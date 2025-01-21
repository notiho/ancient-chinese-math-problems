"""
今有白禾二步、青禾三步、黃禾四步、黑禾五步，實各不滿斗。白取青、黃，青取黃、黑，黃取黑、白，黑取白、青，各一步，而實滿斗。問︰白、青、黃、黑禾實一步各幾何？
術曰：如方程，各置所取，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：白禾 a步 實 b斗 ，青禾 c步 實 d斗 ，黃禾 e步 實 f斗 ，黑禾 g步 實 h斗 。
"""

"""
This problem involves solving a system of linear equations using the ancient Chinese method of elimination, which is similar to Gaussian elimination. Let's break it down step by step and translate it into Python code.

### Problem Setup:
We are given:
- White grain (白禾): 2 bu
- Green grain (青禾): 3 bu
- Yellow grain (黃禾): 4 bu
- Black grain (黑禾): 5 bu

Each grain exchanges a specific amount with others, and together, their total fills exactly 1 dou. We need to determine how much each grain contributes to 1 bu of its respective type.

### Procedure:
The ancient method involves setting up equations for the exchanges and solving them systematically using elimination. Here's the Python implementation:


"""


from fractions import Fraction

# Step 1: Define the coefficients of the equations based on the problem description
# Each row represents an equation for the exchanges, and the right-hand side is 1 (full dou).
# Coefficients are based on the exchanges described in the problem.
coefficients = [
    [1, -1, -1,  0],  # White grain equation
    [0,  1, -1, -1],  # Green grain equation
    [-1, 0,  1, -1],  # Yellow grain equation
    [-1, -1, 0,  1]   # Black grain equation
]

# Right-hand side of the equations (total = 1 dou)
rhs = [1, 1, 1, 1]

# Step 2: Perform Gaussian elimination to solve the system of equations
# Convert the coefficients and rhs into fractions for precise calculations
for i in range(len(coefficients)):
    for j in range(len(coefficients[i])):
        coefficients[i][j] = Fraction(coefficients[i][j])
    rhs[i] = Fraction(rhs[i])

# Forward elimination
for i in range(len(coefficients)):
    # Normalize the pivot row
    pivot = coefficients[i][i]
    for j in range(i, len(coefficients[i])):
        coefficients[i][j] /= pivot
    rhs[i] /= pivot

    # Eliminate the current variable from the rows below
    for k in range(i + 1, len(coefficients)):
        factor = coefficients[k][i]
        for j in range(i, len(coefficients[k])):
            coefficients[k][j] -= factor * coefficients[i][j]
        rhs[k] -= factor * rhs[i]

# Back substitution
solution = [0] * len(coefficients)
for i in range(len(coefficients) - 1, -1, -1):
    solution[i] = rhs[i]
    for j in range(i + 1, len(coefficients)):
        solution[i] -= coefficients[i][j] * solution[j]

# Step 3: Extract the results
a, b = 2, solution[0]  # White grain: 2 bu, solution[0] dou
c, d = 3, solution[1]  # Green grain: 3 bu, solution[1] dou
e, f = 4, solution[2]  # Yellow grain: 4 bu, solution[2] dou
g, h = 5, solution[3]  # Black grain: 5 bu, solution[3] dou

# Output the results
print(f"白禾 {a}步 實 {b}斗")
print(f"青禾 {c}步 實 {d}斗")
print(f"黃禾 {e}步 實 {f}斗")
print(f"黑禾 {g}步 實 {h}斗")


"""


### Explanation:
1. **Setup the equations**: Each grain exchanges a specific amount with others, forming a system of linear equations.
2. **Gaussian elimination**: The system is solved step by step using forward elimination and back substitution.
3. **Extract results**: The solution gives the amount of dou each grain contributes per bu.

### Answer:
The output will provide the amount of dou each grain contributes for 1 bu of its respective type.
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
