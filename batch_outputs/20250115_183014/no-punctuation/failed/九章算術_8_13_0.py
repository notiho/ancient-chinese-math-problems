"""
今有白禾二步青禾三步黃禾四步黑禾五步實各不滿斗白取青黃青取黃黑黃取黑白黑取白青各一步而實滿斗問白青黃黑禾實一步各幾何
術曰如方程各置所取以正負術入之
方程術曰置上禾三秉中禾二秉下禾一秉實三十九斗於右方中左禾列如右方以右行上禾遍乘中行而以直除又乘其次亦以直除然以中行中禾不盡者遍乘左行而以直除左方下禾不盡者上為法下為實實即下禾之實求中禾以法乘中行下實而除下禾之實餘如中禾秉數而一即中禾之實求上禾亦以法乘右行下實而除下禾中禾之實餘如上禾秉數而一即上禾之實實皆如法各得一斗荅曰白禾 a步 實 b斗 青禾 c步 實 d斗 黃禾 e步 實 f斗 黑禾 g步 實 h斗 
"""

"""
This problem involves solving a system of equations using ancient Chinese mathematical methods, specifically the "fangcheng" (方程) method, which is an early form of solving linear equations. Below is the Python implementation of the problem using the described procedure.


"""


from fractions import Fraction

# Problem setup
# White, Green, Yellow, and Black grains are represented as variables
# Each grain contributes to the total of 1 dou (斗) when combined as described in the problem.

# Coefficients for the equations based on the problem description:
# White takes Green and Yellow, Green takes Yellow and Black,
# Yellow takes Black and White, Black takes White and Green.
# Each contributes 1 step to the total of 1 dou.

# Coefficients matrix (left-hand side of the equations)
# Each row corresponds to the contribution of each type of grain.
coefficients = [
    [1, -1, -1, 0],  # White takes Green and Yellow
    [0, 1, -1, -1],  # Green takes Yellow and Black
    [-1, 0, 1, -1],  # Yellow takes Black and White
    [-1, -1, 0, 1],  # Black takes White and Green
]

# Right-hand side of the equations (total contribution to 1 dou)
rhs = [1, 1, 1, 1]

# Step 1: Solve the system of equations using the fangcheng method
# Initialize variables for the solution
white, green, yellow, black = 0, 0, 0, 0

# Fangcheng method: Elimination process
# Normalize the first row
factor = coefficients[0][0]
coefficients[0] = [Fraction(x, factor) for x in coefficients[0]]
rhs[0] = Fraction(rhs[0], factor)

# Eliminate the first variable from the other rows
for i in range(1, 4):
    factor = coefficients[i][0]
    coefficients[i] = [coefficients[i][j] - factor * coefficients[0][j] for j in range(4)]
    rhs[i] = rhs[i] - factor * rhs[0]

# Normalize the second row
factor = coefficients[1][1]
coefficients[1] = [Fraction(x, factor) for x in coefficients[1]]
rhs[1] = Fraction(rhs[1], factor)

# Eliminate the second variable from the other rows
for i in [0, 2, 3]:
    factor = coefficients[i][1]
    coefficients[i] = [coefficients[i][j] - factor * coefficients[1][j] for j in range(4)]
    rhs[i] = rhs[i] - factor * rhs[1]

# Normalize the third row
factor = coefficients[2][2]
coefficients[2] = [Fraction(x, factor) for x in coefficients[2]]
rhs[2] = Fraction(rhs[2], factor)

# Eliminate the third variable from the other rows
for i in [0, 1, 3]:
    factor = coefficients[i][2]
    coefficients[i] = [coefficients[i][j] - factor * coefficients[2][j] for j in range(4)]
    rhs[i] = rhs[i] - factor * rhs[2]

# Normalize the fourth row
factor = coefficients[3][3]
coefficients[3] = [Fraction(x, factor) for x in coefficients[3]]
rhs[3] = Fraction(rhs[3], factor)

# Back-substitution to find the solution
black = rhs[3]
yellow = rhs[2]
green = rhs[1]
white = rhs[0]

# Step 2: Output the results
a, b = white, white
c, d = green, green
e, f = yellow, yellow
g, h = black, black

# Final answer
print(f"白禾 {a}步 實 {b}斗")
print(f"青禾 {c}步 實 {d}斗")
print(f"黃禾 {e}步 實 {f}斗")
print(f"黑禾 {g}步 實 {h}斗")


"""


### Explanation:
1. **Coefficients Matrix**: Each row in the matrix represents an equation based on the problem's description of how each type of grain contributes to the total.
2. **Fangcheng Method**: This is an elimination process similar to Gaussian elimination, where variables are systematically eliminated to solve the system of equations.
3. **Back-Substitution**: After elimination, the solution is obtained by substituting back into the equations.

### Output:
The solution will give the number of steps and dou (斗) for each type of grain:
- 白禾 (White grain): `a` steps, `b` dou
- 青禾 (Green grain): `c` steps, `d` dou
- 黃禾 (Yellow grain): `e` steps, `f` dou
- 黑禾 (Black grain): `g` steps, `h` dou
"""


"""
Variable 'a' has wrong value. Expected: 1, Actual: -4
Variable 'b' has wrong value. Expected: 11/37, Actual: -4
Variable 'c' has wrong value. Expected: 1, Actual: -2
Variable 'd' has wrong value. Expected: 28/111, Actual: -2
Variable 'e' has wrong value. Expected: 1, Actual: -3
Variable 'f' has wrong value. Expected: 17/111, Actual: -3
Variable 'g' has wrong value. Expected: 1, Actual: -1
Variable 'h' has wrong value. Expected: 10/111, Actual: -1"""
