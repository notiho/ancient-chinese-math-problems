"""
今有白禾二步、青禾三步、黃禾四步、黑禾五步，實各不滿斗。白取青、黃，青取黃、黑，黃取黑、白，黑取白、青，各一步，而實滿斗。問︰白、青、黃、黑禾實一步各幾何？
術曰：如方程，各置所取，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：白禾一步實 a斗 ，青禾一步實 b斗 ，黃禾一步實 c斗 ，黑禾一步實 d斗 。
"""

"""
This problem involves solving a system of linear equations using ancient Chinese methods, which are equivalent to Gaussian elimination. Let's translate the problem and solution into Python code step by step.

### Problem Description:
We have four types of grain: white, green, yellow, and black. Each type of grain occupies a certain area (in steps), but their actual volume does not fill a full dou. The grains are mixed in specific proportions, and the total volume becomes exactly one dou. The task is to determine the actual volume (in dou) of each type of grain per step.

### Procedure:
The procedure involves setting up a system of equations based on the mixing rules and solving it using elimination techniques. Here's the Python implementation:


"""


from fractions import Fraction

# Step 1: Define the coefficients of the equations based on the problem description.
# Each row represents an equation, and each column represents a variable (white, green, yellow, black).
# The last column represents the total volume (right-hand side of the equation).
equations = [
    [1, 1, 1, 0, 1],  # White takes 1 step of green and yellow, total 1 dou
    [0, 1, 1, 1, 1],  # Green takes 1 step of yellow and black, total 1 dou
    [1, 0, 1, 1, 1],  # Yellow takes 1 step of black and white, total 1 dou
    [1, 1, 0, 1, 1],  # Black takes 1 step of white and green, total 1 dou
]

# Step 2: Perform Gaussian elimination to solve the system of equations.
# Convert the equations into row echelon form.
for i in range(4):  # Loop through each variable (column)
    # Normalize the current row
    factor = equations[i][i]
    for j in range(5):  # Normalize all columns in the current row
        equations[i][j] = Fraction(equations[i][j], factor)
    
    # Eliminate the current variable from all subsequent rows
    for k in range(i + 1, 4):
        factor = equations[k][i]
        for j in range(5):
            equations[k][j] -= factor * equations[i][j]

# Step 3: Back-substitute to find the solution.
solution = [0] * 4
for i in range(3, -1, -1):  # Start from the last row and move upwards
    solution[i] = equations[i][4]  # Start with the right-hand side
    for j in range(i + 1, 4):  # Subtract the known variables
        solution[i] -= equations[i][j] * solution[j]

# Step 4: Extract the solution for each type of grain.
a, b, c, d = solution

# Output the results.
print(f"白禾一步實 {a}斗")
print(f"青禾一步實 {b}斗")
print(f"黃禾一步實 {c}斗")
print(f"黑禾一步實 {d}斗")


"""


### Explanation of the Code:
1. **Equations Setup**: The coefficients of the equations are derived from the problem description. Each row corresponds to one of the mixing rules, and the last column represents the total volume (1 dou).
2. **Gaussian Elimination**: The system of equations is solved using Gaussian elimination, which involves row operations to reduce the matrix to row echelon form and then back-substitution to find the solution.
3. **Fractions**: The `Fraction` class is used to ensure exact arithmetic, as the problem involves ratios and divisions.
4. **Output**: The solution gives the volume (in dou) of each type of grain per step.

### Answer:
The output will provide the values of `a`, `b`, `c`, and `d`, which represent the volume (in dou) of white, green, yellow, and black grain per step, respectively.
"""


"""
Variable 'a' has wrong value. Expected: 11/37, Actual: 1/3
Variable 'b' has wrong value. Expected: 28/111, Actual: 1/3
Variable 'c' has wrong value. Expected: 17/111, Actual: 1/3
Variable 'd' has wrong value. Expected: 10/111, Actual: 1/3"""
