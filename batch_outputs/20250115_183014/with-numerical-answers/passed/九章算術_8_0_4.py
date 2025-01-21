"""
今有上禾三秉，中禾二秉，下禾一秉，實三十九斗；上禾二秉，中禾三秉，下禾一秉，實三十四斗；上禾一秉，中禾二秉，下禾三秉，實二十六斗。問︰上、中、下禾實一秉各幾何？
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：上禾 a(=1)秉 ， b(=37/4)斗 ，中禾 c(=1)秉 ， d(=17/4)斗 ，下禾 e(=1)秉 ， f(=11/4)斗 。
"""

"""
This problem involves solving a system of linear equations using ancient Chinese methods, which are similar to Gaussian elimination. The goal is to determine the yield of one bundle of upper, middle, and lower millet.

### Problem Setup:
We are given three equations:
1. \( 3x + 2y + z = 39 \)
2. \( 2x + 3y + z = 34 \)
3. \( x + 2y + 3z = 26 \)

Where:
- \( x \) is the yield of one bundle of upper millet,
- \( y \) is the yield of one bundle of middle millet,
- \( z \) is the yield of one bundle of lower millet.

### Procedure:
The ancient Chinese method involves systematically eliminating variables to solve for the unknowns.


"""


from fractions import Fraction

# Coefficients and results from the equations
matrix = [
    [3, 2, 1, 39],  # 3x + 2y + z = 39
    [2, 3, 1, 34],  # 2x + 3y + z = 34
    [1, 2, 3, 26]   # x + 2y + 3z = 26
]

# Step 1: Eliminate the first variable (x) from the second and third rows
factor1 = Fraction(matrix[1][0], matrix[0][0])  # Factor to eliminate x from row 2
factor2 = Fraction(matrix[2][0], matrix[0][0])  # Factor to eliminate x from row 3

for i in range(4):
    matrix[1][i] -= factor1 * matrix[0][i]
    matrix[2][i] -= factor2 * matrix[0][i]

# Step 2: Eliminate the second variable (y) from the third row
factor3 = Fraction(matrix[2][1], matrix[1][1])  # Factor to eliminate y from row 3

for i in range(1, 4):
    matrix[2][i] -= factor3 * matrix[1][i]

# Step 3: Solve for z (lower millet yield)
z = Fraction(matrix[2][3], matrix[2][2])

# Step 4: Solve for y (middle millet yield)
y = Fraction(matrix[1][3] - matrix[1][2] * z, matrix[1][1])

# Step 5: Solve for x (upper millet yield)
x = Fraction(matrix[0][3] - matrix[0][2] * z - matrix[0][1] * y, matrix[0][0])

# Results
a = 1  # Upper millet bundles
b = x  # Yield per bundle of upper millet
c = 1  # Middle millet bundles
d = y  # Yield per bundle of middle millet
e = 1  # Lower millet bundles
f = z  # Yield per bundle of lower millet

# Output results
a, b, c, d, e, f  # (1, 37/4, 1, 17/4, 1, 11/4)


"""


### Explanation of Results:
- \( a = 1 \), \( b = 37/4 \): One bundle of upper millet yields \( 37/4 \) dou.
- \( c = 1 \), \( d = 17/4 \): One bundle of middle millet yields \( 17/4 \) dou.
- \( e = 1 \), \( f = 11/4 \): One bundle of lower millet yields \( 11/4 \) dou.
"""


"""
"""
