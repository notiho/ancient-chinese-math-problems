"""
今有白禾二步、青禾三步、黃禾四步、黑禾五步，實各不滿斗。白取青、黃，青取黃、黑，黃取黑、白，黑取白、青，各一步，而實滿斗。問︰白、青、黃、黑禾實一步各幾何？
術曰：如方程，各置所取，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：白禾一步實 a斗 ，青禾一步實 b斗 ，黃禾一步實 c斗 ，黑禾一步實 d斗 。
"""

"""
To solve this problem using the described method (方程術), we need to translate the ancient Chinese mathematical procedure into Python code. The problem essentially describes a system of linear equations, where the solution involves elimination and substitution. Below is the Python implementation:


"""

#----- content starts here -----

from fractions import Fraction

# Define the coefficients of the equations based on the problem:
# White (白禾), Green (青禾), Yellow (黃禾), Black (黑禾)
# Each row represents an equation, and the last value in each row is the total (right-hand side of the equation).
equations = [
    [1, 1, 1, 0, 1],  # 白禾取青、黃各一步，實滿斗
    [0, 1, 1, 1, 1],  # 青禾取黃、黑各一步，實滿斗
    [1, 0, 1, 1, 1],  # 黃禾取黑、白各一步，實滿斗
    [1, 1, 0, 1, 1]   # 黑禾取白、青各一步，實滿斗
]

# Step 1: Elimination process to solve the system of equations
# Convert the equations into upper triangular form
for i in range(len(equations)):
    # Normalize the current row
    factor = equations[i][i]
    for j in range(len(equations[i])):
        equations[i][j] = Fraction(equations[i][j], factor)
    
    # Eliminate the current variable from the rows below
    for k in range(i + 1, len(equations)):
        factor = equations[k][i]
        for j in range(len(equations[k])):
            equations[k][j] -= factor * equations[i][j]

# Step 2: Back substitution to find the values of the variables
results = [0] * 4  # To store the results for 白禾, 青禾, 黃禾, 黑禾
for i in range(len(equations) - 1, -1, -1):
    results[i] = equations[i][-1]
    for j in range(i + 1, len(equations)):
        results[i] -= equations[i][j] * results[j]

# Assign the results to the respective variables
a = results[0]  # 白禾一步實
b = results[1]  # 青禾一步實
c = results[2]  # 黃禾一步實
d = results[3]  # 黑禾一步實

# Output the results
a, b, c, d
#----- content ends here -----


"""


### Explanation of the Code:
1. **Input Representation**: The equations are represented as a list of lists, where each inner list represents an equation. The last element of each inner list is the total (right-hand side of the equation).

2. **Elimination Process**: The system of equations is converted into an upper triangular form using Gaussian elimination. This involves normalizing the current row and eliminating the current variable from the rows below.

3. **Back Substitution**: Once the equations are in upper triangular form, the values of the variables are determined by back substitution.

4. **Results**: The results are stored in the `results` list and assigned to `a`, `b`, `c`, and `d`, which represent the amounts of 白禾, 青禾, 黃禾, and 黑禾, respectively.

### Final Answer:
The values of `a`, `b`, `c`, and `d` represent the amount of each type of grain (in 斗) for one step.
"""


"""
Variable 'a' has wrong value. Expected: 11/37, Actual: 1/3
Variable 'b' has wrong value. Expected: 28/111, Actual: 1/3
Variable 'c' has wrong value. Expected: 17/111, Actual: 1/3
Variable 'd' has wrong value. Expected: 10/111, Actual: 1/3"""
