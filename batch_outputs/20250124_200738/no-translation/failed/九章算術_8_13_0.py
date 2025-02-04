"""
今有白禾二步、青禾三步、黃禾四步、黑禾五步，實各不滿斗。白取青、黃，青取黃、黑，黃取黑、白，黑取白、青，各一步，而實滿斗。問︰白、青、黃、黑禾實一步各幾何？
術曰：如方程，各置所取，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：白禾一步實 a斗 ，青禾一步實 b斗 ，黃禾一步實 c斗 ，黑禾一步實 d斗 。
"""

"""
To solve this problem, we will implement the described procedure using Python. The problem is essentially a system of linear equations, and we will follow the "方程術" step-by-step as described.


"""

#----- content starts here -----

from fractions import Fraction

# Define the coefficients of the equations based on the problem:
# White (W), Green (G), Yellow (Y), Black (B)
# White takes from Green and Yellow: W + G + Y = 1
# Green takes from Yellow and Black: G + Y + B = 1
# Yellow takes from Black and White: Y + B + W = 1
# Black takes from White and Green: B + W + G = 1

# Coefficients matrix (left-hand side of equations)
coefficients = [
    [1, 1, 1, 0],  # W + G + Y = 1
    [0, 1, 1, 1],  # G + Y + B = 1
    [1, 0, 1, 1],  # Y + B + W = 1
    [1, 1, 0, 1]   # B + W + G = 1
]

# Right-hand side of equations (all equal to 1)
constants = [1, 1, 1, 1]

# Step 1: Elimination process to solve the system of equations
# Convert the coefficients matrix into row echelon form
for i in range(len(coefficients)):
    # Make the diagonal element 1 by dividing the entire row
    diag_element = coefficients[i][i]
    for j in range(len(coefficients[i])):
        coefficients[i][j] = Fraction(coefficients[i][j], diag_element)
    constants[i] = Fraction(constants[i], diag_element)
    
    # Eliminate the current variable from all other rows
    for k in range(len(coefficients)):
        if k != i:
            factor = coefficients[k][i]
            for j in range(len(coefficients[k])):
                coefficients[k][j] -= factor * coefficients[i][j]
            constants[k] -= factor * constants[i]

# Step 2: Extract the solutions
a = constants[0]  # White (W)
b = constants[1]  # Green (G)
c = constants[2]  # Yellow (Y)
d = constants[3]  # Black (B)

# Output the results
a, b, c, d
#----- content ends here -----


"""


### Explanation of the Code:
1. **Coefficients Matrix**: The coefficients matrix represents the system of equations derived from the problem. Each row corresponds to one equation.
2. **Right-Hand Side (Constants)**: The constants are all equal to 1 because each type of grain fills the remaining part of the斗 (bucket).
3. **Gaussian Elimination**: The procedure described in the problem is essentially Gaussian elimination, where we reduce the matrix to row echelon form and then solve for each variable.
4. **Fractions**: The `Fraction` class is used to ensure exact arithmetic, as the problem involves ratios.

### Final Answer:
The values of `a`, `b`, `c`, and `d` represent the amount of grain (in斗) for one step of White, Green, Yellow, and Black grains, respectively.
"""


"""
Variable 'a' has wrong value. Expected: 11/37, Actual: 1/3
Variable 'b' has wrong value. Expected: 28/111, Actual: 1/3
Variable 'c' has wrong value. Expected: 17/111, Actual: 1/3
Variable 'd' has wrong value. Expected: 10/111, Actual: 1/3"""
