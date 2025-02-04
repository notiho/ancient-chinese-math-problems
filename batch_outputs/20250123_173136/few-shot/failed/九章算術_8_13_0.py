"""
今有白禾二步、青禾三步、黃禾四步、黑禾五步，實各不滿斗。白取青、黃，青取黃、黑，黃取黑、白，黑取白、青，各一步，而實滿斗。問︰白、青、黃、黑禾實一步各幾何？
術曰：如方程，各置所取，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：白禾一步實 a斗 ，青禾一步實 b斗 ，黃禾一步實 c斗 ，黑禾一步實 d斗 。
"""

"""
This problem involves solving a system of linear equations using the ancient Chinese method of elimination, similar to Gaussian elimination. Let's translate the problem and the procedure into Python code step by step.

### Problem Description:
We have four types of grains: white (白禾), green (青禾), yellow (黃禾), and black (黑禾). Their respective areas are 2, 3, 4, and 5 bu, but their yields are less than 1 dou each. The grains exchange portions as follows:
- White takes 1 bu each from green and yellow.
- Green takes 1 bu each from yellow and black.
- Yellow takes 1 bu each from black and white.
- Black takes 1 bu each from white and green.

After these exchanges, the total yield becomes exactly 1 dou. The task is to find the yield per bu for each type of grain.

### Procedure:
The solution involves setting up a system of linear equations and solving it using the method described in the "方程術" (method of equations). This involves elimination and substitution to solve for the unknowns.

### Python Code:


"""


from fractions import Fraction

# Step 1: Define the coefficients of the equations based on the problem description
# Let a, b, c, d represent the yield per bu for white, green, yellow, and black grains respectively.
# The equations are derived from the problem:
# 2a + b + c = 1
# a + 3b + c + d = 1
# a + b + 4c + d = 1
# b + c + 5d = 1

# Coefficients of the equations
coefficients = [
    [2, 1, 1, 0],  # 2a + b + c = 1
    [1, 3, 1, 1],  # a + 3b + c + d = 1
    [1, 1, 4, 1],  # a + b + 4c + d = 1
    [0, 1, 1, 5]   # b + c + 5d = 1
]

# Constants on the right-hand side of the equations
constants = [1, 1, 1, 1]

# Step 2: Perform Gaussian elimination to solve the system of equations

# Convert the coefficients and constants into fractions for exact arithmetic
coefficients = [[Fraction(x) for x in row] for row in coefficients]
constants = [Fraction(x) for x in constants]

# Forward elimination
for i in range(4):
    # Normalize the pivot row
    pivot = coefficients[i][i]
    for j in range(i, 4):
        coefficients[i][j] /= pivot
    constants[i] /= pivot

    # Eliminate the current variable from the rows below
    for k in range(i + 1, 4):
        factor = coefficients[k][i]
        for j in range(i, 4):
            coefficients[k][j] -= factor * coefficients[i][j]
        constants[k] -= factor * constants[i]

# Back substitution
solution = [0] * 4
for i in range(3, -1, -1):
    solution[i] = constants[i]
    for j in range(i + 1, 4):
        solution[i] -= coefficients[i][j] * solution[j]

# Step 3: Extract the results
a, b, c, d = solution

# Output the results
print(f"白禾一步實 {a}斗")
print(f"青禾一步實 {b}斗")
print(f"黃禾一步實 {c}斗")
print(f"黑禾一步實 {d}斗")


"""


### Explanation of the Code:
1. **Equation Setup**: The coefficients of the equations are derived from the problem description, and the constants are set to 1 (representing the total yield after exchanges).
2. **Gaussian Elimination**: The system of equations is solved using forward elimination to create an upper triangular matrix, followed by back substitution to find the values of the unknowns.
3. **Exact Arithmetic**: The `Fraction` class is used to ensure exact arithmetic throughout the calculations, as required by the problem.
4. **Results**: The solution gives the yield per bu for each type of grain.

### Answer:
The yields per bu for each type of grain are:
- 白禾 (white grain): `a` dou
- 青禾 (green grain): `b` dou
- 黃禾 (yellow grain): `c` dou
- 黑禾 (black grain): `d` dou
"""


"""
Variable 'a' has wrong value. Expected: 11/37, Actual: 2/5
Variable 'b' has wrong value. Expected: 28/111, Actual: 3/25
Variable 'c' has wrong value. Expected: 17/111, Actual: 2/25
Variable 'd' has wrong value. Expected: 10/111, Actual: 4/25"""
