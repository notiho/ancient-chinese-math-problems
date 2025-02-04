"""
今有白禾二步、青禾三步、黃禾四步、黑禾五步，實各不滿斗。白取青、黃，青取黃、黑，黃取黑、白，黑取白、青，各一步，而實滿斗。問︰白、青、黃、黑禾實一步各幾何？
術曰：如方程，各置所取，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：白禾一步實 a斗 ，青禾一步實 b斗 ，黃禾一步實 c斗 ，黑禾一步實 d斗 。
"""

"""
This problem involves solving a system of linear equations using the ancient Chinese method of elimination, which is similar to Gaussian elimination. Let's translate the problem and procedure into Python code step by step.

### Problem Description
We have four types of grain: white, green, yellow, and black. Each type occupies a certain number of steps (bu), but their actual contents (shi) are less than one dou. The grains are mixed in such a way that:
- White takes 1 step from green and yellow.
- Green takes 1 step from yellow and black.
- Yellow takes 1 step from black and white.
- Black takes 1 step from white and green.

When combined, the total volume becomes exactly 1 dou. The task is to find the actual volume (shi) of each grain per step.

### Procedure
The procedure involves setting up and solving a system of linear equations using elimination. The steps are:
1. Represent the problem as a system of equations.
2. Use elimination to reduce the system to simpler equations.
3. Solve for each variable step by step.

### Python Code


"""

#----- content starts here -----

from fractions import Fraction

# Step 1: Represent the system of equations
# Let a, b, c, d represent the actual volume (shi) of white, green, yellow, and black grains per step.
# The equations are derived from the problem statement:
# 2a + b + c = 1
# a + 3b + c + d = 1
# a + b + 4c + d = 1
# a + b + c + 5d = 1

# Coefficients of the equations
equations = [
    [2, 1, 1, 0, 1],  # 2a + b + c = 1
    [1, 3, 1, 1, 1],  # a + 3b + c + d = 1
    [1, 1, 4, 1, 1],  # a + b + 4c + d = 1
    [1, 1, 1, 5, 1]   # a + b + c + 5d = 1
]

# Step 2: Elimination process
# Convert the system into upper triangular form
for i in range(4):
    # Normalize the current row
    factor = equations[i][i]
    for j in range(5):
        equations[i][j] = Fraction(equations[i][j], factor)
    
    # Eliminate the current variable from the rows below
    for k in range(i + 1, 4):
        factor = equations[k][i]
        for j in range(5):
            equations[k][j] -= factor * equations[i][j]

# Step 3: Back substitution
# Solve for each variable starting from the last row
results = [0, 0, 0, 0]
for i in range(3, -1, -1):
    results[i] = equations[i][4]
    for j in range(i + 1, 4):
        results[i] -= equations[i][j] * results[j]

# Step 4: Assign results to variables
a, b, c, d = results

# Output the results
print(f"白禾一步實 {a}斗")
print(f"青禾一步實 {b}斗")
print(f"黃禾一步實 {c}斗")
print(f"黑禾一步實 {d}斗")
#----- content ends here -----


"""


### Explanation of the Code
1. **System of Equations**: The problem is translated into a system of linear equations based on the relationships between the grains.
2. **Elimination Process**: The system is solved using the method of elimination, reducing it to an upper triangular form.
3. **Back Substitution**: The values of the variables are determined by substituting back from the last equation to the first.
4. **Fractions**: The `Fraction` class is used to ensure exact arithmetic throughout the calculations.

### Answer
The output will provide the actual volume (shi) of each type of grain per step:
- White grain: `a` dou
- Green grain: `b` dou
- Yellow grain: `c` dou
- Black grain: `d` dou
"""


"""
Variable 'a' has wrong value. Expected: 11/37, Actual: 3/8
Variable 'b' has wrong value. Expected: 28/111, Actual: 3/20
Variable 'c' has wrong value. Expected: 17/111, Actual: 1/10
Variable 'd' has wrong value. Expected: 10/111, Actual: 3/40"""
