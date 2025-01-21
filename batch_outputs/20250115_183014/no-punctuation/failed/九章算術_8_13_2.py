"""
今有白禾二步青禾三步黃禾四步黑禾五步實各不滿斗白取青黃青取黃黑黃取黑白黑取白青各一步而實滿斗問白青黃黑禾實一步各幾何
術曰如方程各置所取以正負術入之
方程術曰置上禾三秉中禾二秉下禾一秉實三十九斗於右方中左禾列如右方以右行上禾遍乘中行而以直除又乘其次亦以直除然以中行中禾不盡者遍乘左行而以直除左方下禾不盡者上為法下為實實即下禾之實求中禾以法乘中行下實而除下禾之實餘如中禾秉數而一即中禾之實求上禾亦以法乘右行下實而除下禾中禾之實餘如上禾秉數而一即上禾之實實皆如法各得一斗荅曰白禾 a步 實 b斗 青禾 c步 實 d斗 黃禾 e步 實 f斗 黑禾 g步 實 h斗 
"""

"""
This problem involves solving a system of linear equations to determine the contribution of each type of grain (white, green, yellow, and black) to a full dou of grain. The ancient Chinese "fangcheng" (方程) method is essentially a matrix-based approach to solving linear equations. Below is the Python implementation of the procedure:


"""


from fractions import Fraction

# Problem setup
# White (白禾), Green (青禾), Yellow (黃禾), Black (黑禾)
# Each type of grain contributes a certain amount to the total of 1 dou when combined.

# Coefficients of the equations based on the problem:
# White takes from Green and Yellow
# Green takes from Yellow and Black
# Yellow takes from Black and White
# Black takes from White and Green
# Each contributes 1 dou in total.

# Coefficients matrix (秉數)
coefficients = [
    [1, -1, -1, 0],  # White equation
    [0, 1, -1, -1],  # Green equation
    [-1, 0, 1, -1],  # Yellow equation
    [-1, -1, 0, 1],  # Black equation
]

# Results vector (實滿斗)
results = [1, 1, 1, 1]

# Step 1: Convert the coefficients matrix and results vector into fractions
coefficients = [[Fraction(x) for x in row] for row in coefficients]
results = [Fraction(x) for x in results]

# Step 2: Solve the system of equations using Gaussian elimination
def gaussian_elimination(coefficients, results):
    n = len(coefficients)
    for i in range(n):
        # Make the diagonal element 1 by dividing the row
        diag = coefficients[i][i]
        for j in range(i, n):
            coefficients[i][j] /= diag
        results[i] /= diag

        # Eliminate the current variable from the other rows
        for k in range(n):
            if k != i:
                factor = coefficients[k][i]
                for j in range(i, n):
                    coefficients[k][j] -= factor * coefficients[i][j]
                results[k] -= factor * results[i]

    return results

# Solve the system
solutions = gaussian_elimination(coefficients, results)

# Extract the solutions
a, c, e, g = solutions  # White, Green, Yellow, Black contributions in dou

# Output the results
b = a  # White's contribution in dou
d = c  # Green's contribution in dou
f = e  # Yellow's contribution in dou
h = g  # Black's contribution in dou

print(f"白禾 {a}步 實 {b}斗")
print(f"青禾 {c}步 實 {d}斗")
print(f"黃禾 {e}步 實 {f}斗")
print(f"黑禾 {g}步 實 {h}斗")


"""


### Explanation of the Code:
1. **Matrix Representation**: The coefficients matrix represents the relationships between the grains as described in the problem. Each row corresponds to an equation for one type of grain.
2. **Gaussian Elimination**: This method is used to solve the system of linear equations. It involves row operations to reduce the matrix to row-echelon form and then solve for the variables.
3. **Fraction Handling**: The `Fraction` class is used to ensure exact arithmetic, as ancient Chinese mathematics often dealt with fractional results.

### Answer:
The values of `a`, `b`, `c`, `d`, `e`, `f`, `g`, and `h` will be calculated by the code, representing the contributions of each type of grain in steps and dou.
"""


"""
Variable 'a' has wrong value. Expected: 1, Actual: -1
Variable 'b' has wrong value. Expected: 11/37, Actual: -1
Variable 'c' has wrong value. Expected: 1, Actual: -1
Variable 'd' has wrong value. Expected: 28/111, Actual: -1
Variable 'e' has wrong value. Expected: 1, Actual: -1
Variable 'f' has wrong value. Expected: 17/111, Actual: -1
Variable 'g' has wrong value. Expected: 1, Actual: -1
Variable 'h' has wrong value. Expected: 10/111, Actual: -1"""
