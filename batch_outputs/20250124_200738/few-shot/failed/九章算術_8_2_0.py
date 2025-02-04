"""
今有上禾二秉，中禾三秉，下禾四秉，實皆不滿斗。上取中，中取下，下取上各一秉而實滿斗。問︰上、中、下禾實一秉各幾何？
術曰：如方程，各置所取，以正負術入之。正負術曰：同名相除，異名相益，正無入負之，負無入正之。其異名相除，同名相益，正無入正之，負無入負之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：上禾一秉實 a斗 ，中禾一秉實 b斗 ，下禾一秉實 c斗 。
"""

"""
This is a classic problem involving a system of linear equations, solved using ancient Chinese methods akin to Gaussian elimination. Below is the Python implementation of the procedure described:


"""

#----- content starts here -----

from fractions import Fraction

# 上禾二秉，中禾三秉，下禾四秉
上禾秉數 = 2
中禾秉數 = 3
下禾秉數 = 4

# 上取中，中取下，下取上各一秉而實滿斗
實滿斗 = 1

# 方程術：設置方程組
# Let 上禾一秉實為 x, 中禾一秉實為 y, 下禾一秉實為 z
# The equations are:
# 2x + y = 1
# x + 3y + z = 1
# y + 4z = 1

# Step 1: Represent the equations in matrix form
# Coefficient matrix
A = [
    [2, 1, 0],  # 2x + y = 1
    [1, 3, 1],  # x + 3y + z = 1
    [0, 1, 4]   # y + 4z = 1
]

# Constant terms
B = [1, 1, 1]

# Step 2: Solve using Gaussian elimination
# Forward elimination
for i in range(len(A)):
    # Normalize the pivot row
    pivot = A[i][i]
    for j in range(len(A[i])):
        A[i][j] = Fraction(A[i][j], pivot)
    B[i] = Fraction(B[i], pivot)
    
    # Eliminate the current variable from subsequent rows
    for k in range(i + 1, len(A)):
        factor = A[k][i]
        for j in range(len(A[k])):
            A[k][j] -= factor * A[i][j]
        B[k] -= factor * B[i]

# Back substitution
X = [0] * len(B)
for i in range(len(A) - 1, -1, -1):
    X[i] = B[i]
    for j in range(i + 1, len(A)):
        X[i] -= A[i][j] * X[j]

# Results
a = X[0]  # 上禾一秉實
b = X[1]  # 中禾一秉實
c = X[2]  # 下禾一秉實

# Output the results
a, b, c
#----- content ends here -----


"""


### Explanation of the Code:
1. **Matrix Representation**: The problem is represented as a system of linear equations in matrix form.
2. **Gaussian Elimination**: The procedure described in the problem is essentially Gaussian elimination. The code performs forward elimination to make the matrix upper triangular and then uses back substitution to solve for the variables.
3. **Fraction Handling**: The `Fraction` class is used to ensure exact arithmetic, as required by the problem.

### Answer:
The results `a`, `b`, and `c` represent the amount of斗 (dou) for one秉 (bing) of上禾 (upper grain),中禾 (middle grain), and下禾 (lower grain), respectively.
"""


"""
Variable 'a' has wrong value. Expected: 9/25, Actual: 4/9
Variable 'b' has wrong value. Expected: 7/25, Actual: 1/9
Variable 'c' has wrong value. Expected: 4/25, Actual: 2/9"""
