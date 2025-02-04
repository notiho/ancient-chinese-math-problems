"""
今有白禾二步、青禾三步、黃禾四步、黑禾五步，實各不滿斗。白取青、黃，青取黃、黑，黃取黑、白，黑取白、青，各一步，而實滿斗。問︰白、青、黃、黑禾實一步各幾何？
術曰：如方程，各置所取，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：白禾一步實 a斗 ，青禾一步實 b斗 ，黃禾一步實 c斗 ，黑禾一步實 d斗 。
"""

"""
This problem involves solving a system of linear equations using ancient Chinese mathematical methods, specifically the "fangcheng" (方程) method, which is equivalent to solving simultaneous linear equations. Below is the Python implementation of the problem:


"""

#----- content starts here -----

from fractions import Fraction

# Problem setup:
# White (白禾), Green (青禾), Yellow (黃禾), Black (黑禾) are represented as variables.
# Each type of grain contributes to the total of 1 dou when combined as described.

# Coefficients for the equations:
# White takes 1 step of Green and Yellow.
# Green takes 1 step of Yellow and Black.
# Yellow takes 1 step of Black and White.
# Black takes 1 step of White and Green.

# Representing the equations in matrix form:
# Each row corresponds to one equation, and the last column is the total (1 dou).
# The matrix represents the coefficients of the variables (White, Green, Yellow, Black).

matrix = [
    [1, -1, -1, 0, 0],  # White: White - Green - Yellow = 0
    [0, 1, -1, -1, 0],  # Green: Green - Yellow - Black = 0
    [-1, 0, 1, -1, 0],  # Yellow: Yellow - Black - White = 0
    [-1, -1, 0, 1, 0],  # Black: Black - White - Green = 0
]

# Augmented column for the total (1 dou for each equation):
total = [0, 0, 0, 0]

# Solving the system of equations using Gaussian elimination:
def gaussian_elimination(matrix, total):
    n = len(matrix)
    for i in range(n):
        # Make the diagonal element 1 by dividing the row by the diagonal element.
        diag = matrix[i][i]
        for j in range(i, n):
            matrix[i][j] = Fraction(matrix[i][j], diag)
        total[i] = Fraction(total[i], diag)

        # Eliminate the current variable from all other rows.
        for k in range(n):
            if k != i:
                factor = matrix[k][i]
                for j in range(i, n):
                    matrix[k][j] -= factor * matrix[i][j]
                total[k] -= factor * total[i]

    return total

# Solve the system:
solution = gaussian_elimination(matrix, total)

# Extract the results:
a, b, c, d = solution

# Output the results:
print(f"白禾一步實 {a}斗")
print(f"青禾一步實 {b}斗")
print(f"黃禾一步實 {c}斗")
print(f"黑禾一步實 {d}斗")
#----- content ends here -----


"""


### Explanation of the Code:
1. **Matrix Representation**: The problem is represented as a system of linear equations, where each equation corresponds to the relationships between the grains.
2. **Gaussian Elimination**: This method is used to solve the system of equations. It involves row operations to reduce the matrix to row-echelon form and then solve for the variables.
3. **Fraction Handling**: The `Fraction` class is used to ensure precise arithmetic with fractions, as required by the problem.
4. **Output**: The solution gives the amount of each type of grain (White, Green, Yellow, Black) in dou.

### Note:
The problem description mentions the "方程術" (fangcheng method), which is essentially the ancient Chinese method for solving linear equations. The implementation above follows this method in a modern programming context.
"""


"""
Variable 'a' has wrong value. Expected: 11/37, Actual: 0
Variable 'b' has wrong value. Expected: 28/111, Actual: 0
Variable 'c' has wrong value. Expected: 17/111, Actual: 0
Variable 'd' has wrong value. Expected: 10/111, Actual: 0"""
