"""
今有白禾二步、青禾三步、黃禾四步、黑禾五步，實各不滿斗。白取青、黃，青取黃、黑，黃取黑、白，黑取白、青，各一步，而實滿斗。問︰白、青、黃、黑禾實一步各幾何？
術曰：如方程，各置所取，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：白禾一步實 a斗 ，青禾一步實 b斗 ，黃禾一步實 c斗 ，黑禾一步實 d斗 。
"""

"""
To solve this problem, we need to translate the ancient Chinese method of solving simultaneous linear equations (方程術) into Python code. Here's the step-by-step implementation:


"""

#----- content starts here -----

from fractions import Fraction

# Define the coefficients of the equations based on the problem:
# White (白), Green (青), Yellow (黃), Black (黑)
# Each row represents the equation for each type of grain.
# Coefficients are based on the problem description:
# White takes from Green and Yellow, Green takes from Yellow and Black, etc.
coefficients = [
    [1, -1, -1, 0],  # White: White - Green - Yellow = 0
    [0, 1, -1, -1],  # Green: Green - Yellow - Black = 0
    [-1, 0, 1, -1],  # Yellow: Yellow - Black - White = 0
    [-1, -1, 0, 1]   # Black: Black - White - Green = 0
]

# The right-hand side of the equations (all are 0 since the total balances out)
rhs = [0, 0, 0, 0]

# Add the constraint that the total of all grains equals 1斗 (one full unit)
coefficients.append([1, 1, 1, 1])  # Sum of all grains = 1
rhs.append(1)

# Solve the system of equations using Gaussian elimination
def gaussian_elimination(coefficients, rhs):
    n = len(coefficients)
    for i in range(n):
        # Make the diagonal element 1 by dividing the row
        diag = coefficients[i][i]
        for j in range(i, n):
            coefficients[i][j] = Fraction(coefficients[i][j], diag)
        rhs[i] = Fraction(rhs[i], diag)

        # Eliminate the current variable from the other rows
        for k in range(n):
            if k != i:
                factor = coefficients[k][i]
                for j in range(i, n):
                    coefficients[k][j] -= factor * coefficients[i][j]
                rhs[k] -= factor * rhs[i]

    return rhs

# Solve the equations
solutions = gaussian_elimination(coefficients, rhs)

# Assign the solutions to the respective grains
a = solutions[0]  # White (白禾)
b = solutions[1]  # Green (青禾)
c = solutions[2]  # Yellow (黃禾)
d = solutions[3]  # Black (黑禾)

# Output the results
a, b, c, d
#----- content ends here -----


"""


### Explanation:
1. **Coefficients Matrix**: The coefficients matrix represents the relationships between the grains as described in the problem. Each row corresponds to one equation.
2. **Right-Hand Side (RHS)**: The RHS of the equations is initially all zeros, except for the constraint that the total of all grains equals 1斗.
3. **Gaussian Elimination**: This method is used to solve the system of linear equations. It systematically eliminates variables to find the solution.
4. **Results**: The solutions `a`, `b`, `c`, and `d` represent the amount of grain (in 斗) for White, Green, Yellow, and Black grains, respectively.

### Final Answer:
- 白禾一步實 `a` 斗
- 青禾一步實 `b` 斗
- 黃禾一步實 `c` 斗
- 黑禾一步實 `d` 斗
"""


"""
Code error: list index out of range"""
