"""
今有上禾二秉中禾三秉下禾四秉實皆不滿斗上取中中取下下取上各一秉而實滿斗問上中下禾實一秉各幾何
術曰如方程各置所取以正負術入之正負術曰同名相除異名相益正無入負之負無入正之其異名相除同名相益正無入正之負無入負之
方程術曰置上禾三秉中禾二秉下禾一秉實三十九斗於右方中左禾列如右方以右行上禾遍乘中行而以直除又乘其次亦以直除然以中行中禾不盡者遍乘左行而以直除左方下禾不盡者上為法下為實實即下禾之實求中禾以法乘中行下實而除下禾之實餘如中禾秉數而一即中禾之實求上禾亦以法乘右行下實而除下禾中禾之實餘如上禾秉數而一即上禾之實實皆如法各得一斗
荅曰上禾一秉實 a斗 中禾一秉實 b斗 下禾一秉實 c斗 
"""

"""
This is a classic problem involving a system of linear equations, where the relationships between the quantities of the three types of grain (upper, middle, and lower) are described. The solution involves applying the ancient Chinese method of solving simultaneous equations, which is similar to Gaussian elimination.

Here is the translation of the problem and its solution into Python code:


"""

#----- content starts here -----

"""
Suppose there are 2 bundles of upper grain, 3 bundles of middle grain, and 4 bundles of lower grain.
Each bundle does not fill a dou. 
If the upper grain takes from the middle, the middle takes from the lower, and the lower takes from the upper, each taking one bundle, the total fills exactly one dou.
Question: how much does one bundle of each type of grain weigh?

The procedure says: Use the method of equations. Place the quantities taken from each type of grain and use the positive-negative method to solve.
The positive-negative method says: When the names are the same, subtract. When the names are different, add. 
If positive has no entry, subtract it. If negative has no entry, add it. 
When the names are different, divide. When the names are the same, add. 
If positive has no entry, add it. If negative has no entry, subtract it.

The method of equations says: Place 3 bundles of upper grain, 2 bundles of middle grain, and 1 bundle of lower grain, with the total being 39 dou, on the right side.
On the left side, arrange the grains as on the right side.
Multiply the upper grain by the middle grain and divide by the lower grain.
Then multiply again and divide by the next.
For the middle grain, multiply by the lower grain and divide by the upper grain.
For the lower grain, multiply by the upper grain and divide by the middle grain.
The result is the quantity of each type of grain.

Answer: One bundle of upper grain weighs *a* dou, one bundle of middle grain weighs *b* dou, and one bundle of lower grain weighs *c* dou.
"""

from fractions import Fraction

# Define the system of equations based on the problem:
# Let x = upper grain per bundle, y = middle grain per bundle, z = lower grain per bundle.
# 2x + y - z = 0
# -x + 3y + z = 0
# x - y + 4z = 39

# Coefficients of the equations
A = [
    [2, 1, -1],  # Coefficients of the first equation
    [-1, 3, 1],  # Coefficients of the second equation
    [1, -1, 4],  # Coefficients of the third equation
]

# Right-hand side of the equations
B = [0, 0, 39]

# Solve the system of equations using Gaussian elimination
def gaussian_elimination(A, B):
    n = len(A)
    for i in range(n):
        # Make the diagonal element 1 by dividing the row
        diag = A[i][i]
        for j in range(i, n):
            A[i][j] = Fraction(A[i][j], diag)
        B[i] = Fraction(B[i], diag)

        # Eliminate the current variable from the other rows
        for k in range(n):
            if k != i:
                factor = A[k][i]
                for j in range(i, n):
                    A[k][j] -= factor * A[i][j]
                B[k] -= factor * B[i]

    return B

# Solve for x, y, z
solution = gaussian_elimination(A, B)
a, b, c = solution

# Output the results
a, b, c
#----- content ends here -----


"""


### Explanation of the Code:
1. **System of Equations**: The problem is translated into a system of three linear equations with three variables (`x`, `y`, `z`), representing the amount of grain in one bundle of upper, middle, and lower grain, respectively.
2. **Gaussian Elimination**: The ancient Chinese method of solving equations is implemented as Gaussian elimination, where the equations are manipulated to isolate each variable.
3. **Fractions**: The `Fraction` class is used to ensure exact arithmetic, as the problem involves ratios and divisions.

### Answer:
The solution will output the values of `a`, `b`, and `c`, which represent the amount of grain in one bundle of upper, middle, and lower grain, respectively, in dou.
"""


"""
Variable 'a' has wrong value. Expected: 9/25, Actual: 52/11
Variable 'b' has wrong value. Expected: 7/25, Actual: -13/11
Variable 'c' has wrong value. Expected: 4/25, Actual: 91/11"""
