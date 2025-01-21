"""
今有白禾二步、青禾三步、黃禾四步、黑禾五步，實各不滿斗。白取青、黃，青取黃、黑，黃取黑、白，黑取白、青，各一步，而實滿斗。問︰白、青、黃、黑禾實一步各幾何？
術曰：如方程，各置所取，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：白禾 a步 實 b斗 ，青禾 c步 實 d斗 ，黃禾 e步 實 f斗 ，黑禾 g步 實 h斗 。
"""

"""
This problem describes a system of simultaneous linear equations, which can be solved using the method of elimination as described in the "方程術" (method of solving equations). Below is the Python implementation of the solution:


"""


from fractions import Fraction

# Define the coefficients of the equations based on the problem
# White (白禾), Green (青禾), Yellow (黃禾), Black (黑禾)
# Each row corresponds to an equation, and each column corresponds to a variable
coefficients = [
    [1, 1, 1, 0],  # White takes from Green and Yellow
    [0, 1, 1, 1],  # Green takes from Yellow and Black
    [1, 0, 1, 1],  # Yellow takes from Black and White
    [1, 1, 0, 1],  # Black takes from White and Green
]

# The total amount of grain in each case is 1斗 (full斗)
results = [1, 1, 1, 1]

# Step 1: Elimination process to solve the system of equations
# Convert the coefficients into fractions for precise calculations
for i in range(len(coefficients)):
    for j in range(len(coefficients[i])):
        coefficients[i][j] = Fraction(coefficients[i][j])
    results[i] = Fraction(results[i])

# Perform Gaussian elimination
for i in range(len(coefficients)):
    # Normalize the current row
    divisor = coefficients[i][i]
    for j in range(len(coefficients[i])):
        coefficients[i][j] /= divisor
    results[i] /= divisor

    # Eliminate the current variable from the other rows
    for k in range(len(coefficients)):
        if k != i:
            factor = coefficients[k][i]
            for j in range(len(coefficients[k])):
                coefficients[k][j] -= factor * coefficients[i][j]
            results[k] -= factor * results[i]

# The results now contain the solution for each variable
白禾實 = results[0]
青禾實 = results[1]
黃禾實 = results[2]
黑禾實 = results[3]

# Step 2: Calculate the number of steps (步) for each type of grain
白禾步 = 2
青禾步 = 3
黃禾步 = 4
黑禾步 = 5

# Output the results
a, b = 白禾步, 白禾實
c, d = 青禾步, 青禾實
e, f = 黃禾步, 黃禾實
g, h = 黑禾步, 黑禾實

print(f"白禾 {a}步 實 {b}斗")
print(f"青禾 {c}步 實 {d}斗")
print(f"黃禾 {e}步 實 {f}斗")
print(f"黑禾 {g}步 實 {h}斗")


"""


### Explanation of the Code:
1. **Coefficients Matrix**: The coefficients of the equations are derived from the problem statement. Each row represents an equation, and each column represents a variable (white, green, yellow, black grains).
2. **Results Vector**: The total amount of grain for each equation is 1斗 (full斗).
3. **Gaussian Elimination**: The system of equations is solved using Gaussian elimination, which involves normalizing rows and eliminating variables step by step.
4. **Output**: The final results are the amounts of grain (in 斗) for each type of grain.

### Answer:
The solution will provide the values of `a`, `b`, `c`, `d`, `e`, `f`, `g`, and `h` as the number of steps and the amount of grain for each type of grain.
"""


"""
Variable 'a' has wrong value. Expected: 1, Actual: 2
Variable 'b' has wrong value. Expected: 11/37, Actual: 1/3
Variable 'c' has wrong value. Expected: 1, Actual: 3
Variable 'd' has wrong value. Expected: 28/111, Actual: 1/3
Variable 'e' has wrong value. Expected: 1, Actual: 4
Variable 'f' has wrong value. Expected: 17/111, Actual: 1/3
Variable 'g' has wrong value. Expected: 1, Actual: 5
Variable 'h' has wrong value. Expected: 10/111, Actual: 1/3"""
