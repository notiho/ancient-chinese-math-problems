"""
今有上禾七秉，損實一斗，益之下禾二秉，而實一十斗。下禾八秉，益實一斗與上禾二秉，而實一十斗。問︰上、下禾實一秉各幾何？
術曰：如方程。損之曰益，益之曰損。損實一斗者，其實過一十斗也。益實一斗者，其實不滿一十斗也。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：上禾 a(=1)秉 實 b(=35/26)斗 ，下禾 c(=1)秉 實 d(=41/52)斗 。
"""

"""
This problem involves a system of equations and uses a method similar to Gaussian elimination to solve for the yield of one stalk of upper and lower millet. Below is the translation of the problem and its solution into Python code:


"""


"""
Suppose there are 7 bundles of upper millet, which lose 1 dou of yield, and 2 bundles of lower millet are added, resulting in a total yield of 10 dou.
Suppose there are 8 bundles of lower millet, which gain 1 dou of yield, and 2 bundles of upper millet are added, resulting in a total yield of 10 dou.
Question: What is the yield of one bundle of upper millet and one bundle of lower millet?

The procedure says: Treat it as a system of equations. Loss is treated as gain, and gain is treated as loss.
When the yield loses 1 dou, its actual yield exceeds 10 dou. When the yield gains 1 dou, its actual yield is less than 10 dou.

The method for solving systems of equations says: Place 3 bundles of upper millet, 2 bundles of middle millet, and 1 bundle of lower millet, with a total yield of 39 dou, on the right side.
Arrange the middle and left millet as on the right side. Multiply the upper millet in the right row by the middle row and divide directly. Multiply again by the next row and divide directly.
Then, multiply the middle millet in the middle row by the left row and divide directly. For the lower millet in the left row, the upper value is the divisor, and the lower value is the dividend. The dividend is the yield of the lower millet.
To find the middle millet, multiply the divisor by the middle row's lower yield and divide by the lower millet's yield. The remainder, divided by the number of bundles of middle millet plus one, is the yield of the middle millet.
To find the upper millet, multiply the divisor by the right row's lower yield and divide by the yields of the lower and middle millet. The remainder, divided by the number of bundles of upper millet plus one, is the yield of the upper millet.
The yields are all as calculated, and each is 1 dou.

Answer: The yield of one bundle of upper millet is *a*(=1) bundle, with *b*(=35/26) dou. The yield of one bundle of lower millet is *c*(=1) bundle, with *d*(=41/52) dou.
"""

from fractions import Fraction

# Define the system of equations:
# 7a - 1 + 2b = 10
# 2a + 8b + 1 = 10

# Rewrite the equations:
# 7a + 2b = 11
# 2a + 8b = 9

# Coefficients of the equations
A1, B1, C1 = 7, 2, 11  # 7a + 2b = 11
A2, B2, C2 = 2, 8, 9   # 2a + 8b = 9

# Eliminate one variable (Gaussian elimination):
# Multiply the first equation by 8 and the second equation by 2 to align coefficients of b:
A1, B1, C1 = 7 * 8, 2 * 8, 11 * 8  # 56a + 16b = 88
A2, B2, C2 = 2 * 2, 8 * 2, 9 * 2   # 4a + 16b = 18

# Subtract the second equation from the first to eliminate b:
A = A1 - A2  # 56a - 4a = 52a
C = C1 - C2  # 88 - 18 = 70

# Solve for a:
a = Fraction(C, A)  # a = 70 / 52 = 35 / 26

# Substitute a back into one of the original equations to solve for b:
# Using 7a + 2b = 11:
b = Fraction(C1 - A1 * a, B1)  # b = (11 - 7 * (35/26)) / 2 = 41 / 52

# Results:
print("The yield of one bundle of upper millet (a) is:", a)  # 35/26 dou
print("The yield of one bundle of lower millet (b) is:", b)  # 41/52 dou


"""


### Explanation:
1. The problem is translated into a system of linear equations based on the given conditions.
2. Gaussian elimination is used to solve for one variable (`a` for upper millet yield).
3. The value of `a` is substituted back into one of the original equations to solve for `b` (lower millet yield).
4. The results are expressed as fractions to maintain precision, as required by the problem.
"""


"""
Variable 'a' has wrong value. Expected: 1, Actual: 35/26
Variable 'b' has wrong value. Expected: 35/26, Actual: 41/52
Missing variable in output: 'c'
Missing variable in output: 'd'"""
