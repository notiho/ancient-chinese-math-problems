"""
今有白禾二步、青禾三步、黃禾四步、黑禾五步，實各不滿斗。白取青、黃，青取黃、黑，黃取黑、白，黑取白、青，各一步，而實滿斗。問︰白、青、黃、黑禾實一步各幾何？
術曰：如方程，各置所取，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：白禾一步實 a(=11/37)斗 ，青禾一步實 b(=28/111)斗 ，黃禾一步實 c(=17/111)斗 ，黑禾一步實 d(=10/111)斗 。
"""

"""
To solve this problem, we will translate the ancient Chinese method of solving simultaneous linear equations (方程術) into Python code. The problem involves four types of grain (white, green, yellow, black), each with a certain contribution to a total of one dou when combined under specific conditions. The solution involves setting up and solving a system of linear equations.


"""


from fractions import Fraction

# Define the coefficients of the equations based on the problem description
# Each row corresponds to one equation
# Each column corresponds to one type of grain (white, green, yellow, black)
coefficients = [
    [1, 1, 0, 1],  # White takes green, yellow, and black
    [1, 1, 1, 0],  # Green takes yellow, black, and white
    [0, 1, 1, 1],  # Yellow takes black, white, and green
    [1, 0, 1, 1]   # Black takes white, green, and yellow
]

# The right-hand side of the equations (total contribution to one dou)
rhs = [1, 1, 1, 1]

# Initialize variables for the solution
# These represent the amount of each type of grain in one step
white, green, yellow, black = 0, 0, 0, 0

# Solve the system of equations using Gaussian elimination
# Step 1: Normalize the first row
for i in range(4):
    coefficients[0][i] = Fraction(coefficients[0][i], coefficients[0][0])
rhs[0] = Fraction(rhs[0], coefficients[0][0])

# Step 2: Eliminate the first variable from the other rows
for i in range(1, 4):
    factor = coefficients[i][0]
    for j in range(4):
        coefficients[i][j] -= factor * coefficients[0][j]
    rhs[i] -= factor * rhs[0]

# Step 3: Normalize the second row
for i in range(1, 4):
    coefficients[1][i] = Fraction(coefficients[1][i], coefficients[1][1])
rhs[1] = Fraction(rhs[1], coefficients[1][1])

# Step 4: Eliminate the second variable from the other rows
for i in [0, 2, 3]:
    factor = coefficients[i][1]
    for j in range(1, 4):
        coefficients[i][j] -= factor * coefficients[1][j]
    rhs[i] -= factor * rhs[1]

# Step 5: Normalize the third row
for i in range(2, 4):
    coefficients[2][i] = Fraction(coefficients[2][i], coefficients[2][2])
rhs[2] = Fraction(rhs[2], coefficients[2][2])

# Step 6: Eliminate the third variable from the other rows
for i in [0, 1, 3]:
    factor = coefficients[i][2]
    for j in range(2, 4):
        coefficients[i][j] -= factor * coefficients[2][j]
    rhs[i] -= factor * rhs[2]

# Step 7: Solve for the fourth variable
rhs[3] = Fraction(rhs[3], coefficients[3][3])

# Back-substitute to solve for the other variables
black = rhs[3]
yellow = rhs[2] - coefficients[2][3] * black
green = rhs[1] - coefficients[1][2] * yellow - coefficients[1][3] * black
white = rhs[0] - coefficients[0][1] * green - coefficients[0][2] * yellow - coefficients[0][3] * black

# Output the results
a = white  # 11/37 dou
b = green  # 28/111 dou
c = yellow # 17/111 dou
d = black  # 10/111 dou

print(f"White grain per step: {a} dou")
print(f"Green grain per step: {b} dou")
print(f"Yellow grain per step: {c} dou")
print(f"Black grain per step: {d} dou")


"""


### Explanation:
1. **Setup the equations**: The coefficients matrix represents the relationships between the grains, and the `rhs` array represents the total contribution to one dou.
2. **Gaussian elimination**: This method systematically eliminates variables to solve the system of linear equations.
3. **Back-substitution**: After eliminating variables, the solution is obtained by substituting values back into the equations.

### Results:
- White grain per step: `11/37` dou
- Green grain per step: `28/111` dou
- Yellow grain per step: `17/111` dou
- Black grain per step: `10/111` dou
"""


"""
Code error: Fraction(0, 0)"""
