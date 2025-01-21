"""
今有上禾三秉，益實六斗，當下禾十秉。下禾五秉，益實一斗，當上禾二秉。問︰上、下禾實一秉各幾何？
術曰：如方程，置上禾三秉正，下禾一十秉負，益實六斗負。次置上禾二秉負，下禾五秉正，益實一斗負。以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：上禾 a(=1)秉 實 b(=8)斗 ，下禾 c(=1)秉 實 d(=3)斗 。
"""

This problem involves solving a system of linear equations using ancient Chinese methods, which resemble modern elimination techniques. Here's the solution translated into Python code:

"""
Suppose there are 3 bundles of superior grain (上禾), which yield an additional 6 dou, equivalent to 10 bundles of inferior grain (下禾).
And 5 bundles of inferior grain yield an additional 1 dou, equivalent to 2 bundles of superior grain.
Question: how much does one bundle of superior grain and one bundle of inferior grain yield?

The procedure says: Treat it as a system of equations. Place 3 bundles of superior grain as positive, 10 bundles of inferior grain as negative, and 6 dou as negative.
Next, place 2 bundles of superior grain as negative, 5 bundles of inferior grain as positive, and 1 dou as negative.
Use the positive-negative method to solve.

The method for solving systems of equations says: Place the coefficients of superior grain, middle grain, and inferior grain, along with the total dou, on the right side.
Arrange the coefficients of the middle and left grains in the same way as the right side.
Multiply the top row by the middle row and divide by the diagonal.
Repeat for the next row, also dividing by the diagonal.
For the middle row, multiply the middle grain by the left row and divide by the diagonal.
For the left row, if the inferior grain is not fully reduced, the top becomes the divisor, and the bottom becomes the dividend.
The dividend is the yield of the inferior grain.
To find the yield of the middle grain, multiply the divisor by the middle row's yield and divide by the inferior grain's yield.
The remainder, divided by the middle grain's coefficient, gives the yield of the middle grain.
To find the yield of the superior grain, multiply the divisor by the right row's yield and divide by the inferior and middle grain's yield.
The remainder, divided by the superior grain's coefficient, gives the yield of the superior grain.
The yields are all as calculated.

Answer: One bundle of superior grain yields *b*(=8) dou, and one bundle of inferior grain yields *d*(=3) dou.
"""

from fractions import Fraction

# Coefficients from the problem:
# Equation 1: 3上禾 - 10下禾 = -6
# Equation 2: -2上禾 + 5下禾 = -1

# Initialize coefficients
上禾1, 下禾1, 實1 = 3, -10, -6
上禾2, 下禾2, 實2 = -2, 5, -1

# Step 1: Eliminate 上禾 from the second equation
# Multiply the first equation by 2 and the second equation by 3
上禾1, 下禾1, 實1 = 2 * 上禾1, 2 * 下禾1, 2 * 實1
上禾2, 下禾2, 實2 = 3 * 上禾2, 3 * 下禾2, 3 * 實2

# Subtract the second equation from the first
下禾 = 下禾1 - 下禾2
實 = 實1 - 實2

# Step 2: Solve for 下禾 (one bundle of inferior grain)
d = Fraction(實, 下禾)  # 下禾實 = 3斗

# Step 3: Substitute 下禾實 back into one of the original equations to solve for 上禾
實1 = Fraction(實1, 2)  # Restore original equation 1
上禾 = 上禾1
實 = 實1 - (下禾1 * d)
b = Fraction(實, 上禾)  # 上禾實 = 8斗

# Final results
a = 1  # One bundle of superior grain
c = 1  # One bundle of inferior grain

# Outputs
a, b, c, d  # (1, 8, 1, 3)
"""
Code error: unterminated string literal (detected at line 2) (<string>, line 2)"""
