"""
今有白禾二步青禾三步黃禾四步黑禾五步實各不滿斗白取青黃青取黃黑黃取黑白黑取白青各一步而實滿斗問白青黃黑禾實一步各幾何
術曰如方程各置所取以正負術入之
方程術曰置上禾三秉中禾二秉下禾一秉實三十九斗於右方中左禾列如右方以右行上禾遍乘中行而以直除又乘其次亦以直除然以中行中禾不盡者遍乘左行而以直除左方下禾不盡者上為法下為實實即下禾之實求中禾以法乘中行下實而除下禾之實餘如中禾秉數而一即中禾之實求上禾亦以法乘右行下實而除下禾中禾之實餘如上禾秉數而一即上禾之實實皆如法各得一斗
荅曰白禾一步實 a斗 青禾一步實 b斗 黃禾一步實 c斗 黑禾一步實 d斗 
"""

"""
This problem involves solving a system of linear equations using the ancient Chinese method of elimination, as described in the "方程術" (method of solving simultaneous equations). Here's the solution translated into Python code:


"""

#----- content starts here -----

"""
Suppose there are four types of grain: white grain (2 bu), green grain (3 bu), yellow grain (4 bu), and black grain (5 bu).
Each type of grain contributes a certain amount to the total volume of 1 dou when combined in specific proportions:
- White grain takes from green and yellow.
- Green grain takes from yellow and black.
- Yellow grain takes from black and white.
- Black grain takes from white and green.

The question asks: how much volume does each type of grain contribute per bu?

The procedure says: Use the method of solving simultaneous equations.
Place the coefficients of the grains into a matrix, and use elimination to solve for the unknowns.

The answer says: white grain contributes *a* dou, green grain contributes *b* dou, yellow grain contributes *c* dou, and black grain contributes *d* dou.
"""

from fractions import Fraction

# Coefficients of the equations
# Each row represents an equation, and each column represents a grain (white, green, yellow, black).
# The last column represents the total volume (1 dou).
matrix = [
    [1, -1, -1, 0, 0],  # White grain equation
    [0, 1, -1, -1, 0],  # Green grain equation
    [-1, 0, 1, -1, 0],  # Yellow grain equation
    [-1, -1, 0, 1, 0],  # Black grain equation
]

# Total volume of 1 dou
total_volume = 1

# Initialize the solution vector
solution = [0, 0, 0, 0]

# Step 1: Forward elimination
for i in range(4):
    # Normalize the pivot row
    pivot = matrix[i][i]
    for j in range(i, 5):
        matrix[i][j] = Fraction(matrix[i][j], pivot)
    
    # Eliminate the current variable from the rows below
    for k in range(i + 1, 4):
        factor = matrix[k][i]
        for j in range(i, 5):
            matrix[k][j] -= factor * matrix[i][j]

# Step 2: Back substitution
for i in range(3, -1, -1):
    solution[i] = matrix[i][4]
    for j in range(i + 1, 4):
        solution[i] -= matrix[i][j] * solution[j]

# Extract the solutions
a, b, c, d = solution

# Output the results
a, b, c, d
#----- content ends here -----


"""


This code uses the method of Gaussian elimination to solve the system of linear equations described in the problem. Each step of the procedure is implemented explicitly, following the ancient Chinese method. The final result gives the contribution of each type of grain (white, green, yellow, black) to the total volume of 1 dou.
"""


"""
Variable 'a' has wrong value. Expected: 11/37, Actual: 0
Variable 'b' has wrong value. Expected: 28/111, Actual: 0
Variable 'c' has wrong value. Expected: 17/111, Actual: 0
Variable 'd' has wrong value. Expected: 10/111, Actual: 0"""
