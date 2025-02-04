"""
今有白禾二步青禾三步黃禾四步黑禾五步實各不滿斗白取青黃青取黃黑黃取黑白黑取白青各一步而實滿斗問白青黃黑禾實一步各幾何
術曰如方程各置所取以正負術入之
方程術曰置上禾三秉中禾二秉下禾一秉實三十九斗於右方中左禾列如右方以右行上禾遍乘中行而以直除又乘其次亦以直除然以中行中禾不盡者遍乘左行而以直除左方下禾不盡者上為法下為實實即下禾之實求中禾以法乘中行下實而除下禾之實餘如中禾秉數而一即中禾之實求上禾亦以法乘右行下實而除下禾中禾之實餘如上禾秉數而一即上禾之實實皆如法各得一斗
荅曰白禾一步實 a斗 青禾一步實 b斗 黃禾一步實 c斗 黑禾一步實 d斗 
"""

"""
This problem involves solving a system of linear equations using the ancient Chinese method of elimination, similar to Gaussian elimination. The problem describes a situation where four types of grain (white, green, yellow, and black) are combined in specific proportions to fill a total of one dou (斗). The goal is to determine how much of each type of grain contributes to one step (步) of the total.

The procedure provided is a step-by-step guide to solving the system of equations using elimination. Below is the Python implementation of the procedure:


"""


from fractions import Fraction

# Define the coefficients of the system of equations
# Each row corresponds to the proportions of grains taken to fill one dou
# White (白禾), Green (青禾), Yellow (黃禾), Black (黑禾)
coefficients = [
    [1, -1, -1, 1],  # White takes Green and Yellow, gives to Black
    [-1, 1, -1, -1], # Green takes Yellow and Black, gives to White
    [-1, -1, 1, -1], # Yellow takes Black and White, gives to Green
    [1, -1, -1, 1]   # Black takes White and Green, gives to Yellow
]

# Define the total (right-hand side of the equations)
total = [1, 1, 1, 1]  # Each step contributes to one dou

# Initialize variables for the solution
white, green, yellow, black = 0, 0, 0, 0

# Step 1: Solve for the grains using elimination
# Normalize the first row
factor = coefficients[0][0]
coefficients[0] = [Fraction(x, factor) for x in coefficients[0]]
total[0] = Fraction(total[0], factor)

# Eliminate the first variable from the other rows
for i in range(1, 4):
    factor = coefficients[i][0]
    coefficients[i] = [coefficients[i][j] - factor * coefficients[0][j] for j in range(4)]
    total[i] -= factor * total[0]

# Normalize the second row
factor = coefficients[1][1]
coefficients[1] = [Fraction(x, factor) for x in coefficients[1]]
total[1] = Fraction(total[1], factor)

# Eliminate the second variable from the other rows
for i in [0, 2, 3]:
    factor = coefficients[i][1]
    coefficients[i] = [coefficients[i][j] - factor * coefficients[1][j] for j in range(4)]
    total[i] -= factor * total[1]

# Normalize the third row
factor = coefficients[2][2]
coefficients[2] = [Fraction(x, factor) for x in coefficients[2]]
total[2] = Fraction(total[2], factor)

# Eliminate the third variable from the other rows
for i in [0, 1, 3]:
    factor = coefficients[i][2]
    coefficients[i] = [coefficients[i][j] - factor * coefficients[2][j] for j in range(4)]
    total[i] -= factor * total[2]

# Normalize the fourth row
factor = coefficients[3][3]
coefficients[3] = [Fraction(x, factor) for x in coefficients[3]]
total[3] = Fraction(total[3], factor)

# Back-substitute to find the solution
black = total[3]
yellow = total[2] - coefficients[2][3] * black
green = total[1] - coefficients[1][2] * yellow - coefficients[1][3] * black
white = total[0] - coefficients[0][1] * green - coefficients[0][2] * yellow - coefficients[0][3] * black

# Output the results
a = white
b = green
c = yellow
d = black

print(f"白禾一步實 {a}斗 青禾一步實 {b}斗 黃禾一步實 {c}斗 黑禾一步實 {d}斗")


"""


This code follows the ancient Chinese elimination method described in the problem. Each step corresponds to the procedure outlined, ensuring that the solution adheres to the structure of the original method. The results are expressed as fractions to maintain precision.
"""


"""
Code error: Fraction(0, 0)"""
