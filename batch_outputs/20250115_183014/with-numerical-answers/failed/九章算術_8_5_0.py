"""
今有上禾三秉，益實六斗，當下禾十秉。下禾五秉，益實一斗，當上禾二秉。問︰上、下禾實一秉各幾何？
術曰：如方程，置上禾三秉正，下禾一十秉負，益實六斗負。次置上禾二秉負，下禾五秉正，益實一斗負。以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：上禾 a(=1)秉 實 b(=8)斗 ，下禾 c(=1)秉 實 d(=3)斗 。
"""

This problem involves solving a system of linear equations using ancient Chinese mathematical methods, specifically the "fangcheng" (方程) procedure. Below is the translation of the problem and its solution into Python code:

"""
Suppose there are 3 bundles of superior grain (上禾), which when supplemented with 6 dou of grain, are equivalent to 10 bundles of inferior grain (下禾).
Suppose there are 5 bundles of inferior grain, which when supplemented with 1 dou of grain, are equivalent to 2 bundles of superior grain.
Question: how much grain does one bundle of superior grain and one bundle of inferior grain yield?

The procedure says: Treat it as a system of linear equations.
Place 3 bundles of superior grain as positive, 10 bundles of inferior grain as negative, and 6 dou as negative.
Next, place 2 bundles of superior grain as negative, 5 bundles of inferior grain as positive, and 1 dou as negative.
Use the positive-negative procedure to solve it.

The fangcheng procedure says: Place the coefficients of superior grain, middle grain, and inferior grain, along with the constants, on the right side.
Arrange the rows for the middle and left grains as on the right side.
Multiply the first row by the coefficient of the superior grain in the second row, and divide by the diagonal coefficient.
Repeat for the next row, dividing by the diagonal coefficient.
Then, for the middle row, multiply the coefficient of the middle grain by the left row and divide by the diagonal coefficient.
For the inferior grain, the top coefficient becomes the divisor, and the bottom coefficient becomes the dividend.
The result is the yield of one bundle of inferior grain.
To find the yield of the middle grain, multiply the divisor by the middle row's coefficient and divide by the inferior grain's yield.
The remainder divided by the middle grain's coefficient gives the yield of one bundle of middle grain.
To find the yield of the superior grain, multiply the divisor by the right row's coefficient and divide by the inferior and middle grain's yields.
The remainder divided by the superior grain's coefficient gives the yield of one bundle of superior grain.
The yields are all as calculated.

Answer: One bundle of superior grain yields *b*(=8) dou, and one bundle of inferior grain yields *d*(=3) dou.
"""

from fractions import Fraction

# Coefficients for the equations:
# 3 bundles of superior grain - 10 bundles of inferior grain = -6 dou
# -2 bundles of superior grain + 5 bundles of inferior grain = -1 dou

# Equation 1: 3x - 10y = -6
# Equation 2: -2x + 5y = -1

# Step 1: Eliminate one variable (fangcheng procedure)
# Multiply the first equation by 2 and the second equation by 3 to align the coefficients of x
eq1 = [3, -10, -6]  # Coefficients for equation 1
eq2 = [-2, 5, -1]   # Coefficients for equation 2

# Scale equations
eq1_scaled = [2 * term for term in eq1]  # [6, -20, -12]
eq2_scaled = [3 * term for term in eq2]  # [-6, 15, -3]

# Add the scaled equations to eliminate x
combined_eq = [
    eq1_scaled[0] + eq2_scaled[0],  # x coefficient (should be 0)
    eq1_scaled[1] + eq2_scaled[1],  # y coefficient
    eq1_scaled[2] + eq2_scaled[2],  # constant term
]  # [0, -5, -15]

# Simplified equation: -5y = -15
# Solve for y (inferior grain yield)
y = Fraction(-15, -5)  # y = 3 dou

# Step 2: Substitute y back into one of the original equations to solve for x (superior grain yield)
# Using the first equation: 3x - 10y = -6
x = Fraction(-6 + 10 * y, 3)  # x = 8 dou

# Results
a = 1  # One bundle of superior grain
b = x  # Yield of one bundle of superior grain (8 dou)
c = 1  # One bundle of inferior grain
d = y  # Yield of one bundle of inferior grain (3 dou)

# Outputs
a, b, c, d  # (1, 8, 1, 3)
"""
Code error: invalid syntax (<string>, line 2)"""
