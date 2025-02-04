"""
今有上禾五秉，損實一斗一升，當下禾七秉。上禾七秉，損實二斗五升，當下禾五秉。問︰上、下禾實一秉各幾何？
術曰：如方程，置上禾五秉正，下禾七秉負，損實一斗一升正。次置上禾七秉正，下禾五秉負，損實二斗五升正。以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：上禾一秉 a(=5)升 ，下禾一秉 b(=2)升 。
"""

#----- content starts here -----
"""
Suppose there are 5 bundles of upper millet, which lose 1 dou and 1 sheng of grain, corresponding to 7 bundles of lower millet.
Suppose there are 7 bundles of upper millet, which lose 2 dou and 5 sheng of grain, corresponding to 5 bundles of lower millet.
Question: how much grain does one bundle of upper millet and one bundle of lower millet yield respectively?

The procedure says: As in the method of simultaneous equations, place 5 bundles of upper millet as positive, 7 bundles of lower millet as negative, and 1 dou and 1 sheng as positive. 
Next, place 7 bundles of upper millet as positive, 5 bundles of lower millet as negative, and 2 dou and 5 sheng as positive.
Use the positive-negative method to solve.

The method of simultaneous equations says: Place 3 bundles of upper millet, 2 bundles of middle millet, and 1 bundle of lower millet, with 39 dou on the right side. 
Arrange the middle and left millet similarly to the right side.
Multiply the upper millet row by the middle row and divide directly. Then multiply by the next row and divide directly.
For the middle row, multiply the middle millet row by the left row and divide directly.
For the lower millet, if there is a remainder, take the upper millet as the divisor and the lower millet as the dividend. The result is the grain for the lower millet.
To find the middle millet, multiply the divisor by the middle row's lower millet result and divide by the lower millet's grain. The remainder corresponds to the middle millet's grain.
To find the upper millet, multiply the divisor by the right row's lower millet result and divide by the middle and lower millet's grain. The remainder corresponds to the upper millet's grain.
The grain is calculated as per the method, and each yields 1 dou.

Answer: One bundle of upper millet yields *a*(=5) sheng, and one bundle of lower millet yields *b*(=2) sheng.
"""

from fractions import Fraction

# 上禾五秉，損實一斗一升，當下禾七秉
上禾1 = 5
下禾1 = -7
損實1 = 1 * 10 + 1  # 1斗1升 converted to sheng

# 上禾七秉，損實二斗五升，當下禾五秉
上禾2 = 7
下禾2 = -5
損實2 = 2 * 10 + 5  # 2斗5升 converted to sheng

# Simultaneous equations:
# 上禾1 * x + 下禾1 * y = 損實1
# 上禾2 * x + 下禾2 * y = 損實2

# Solve using elimination:
# Multiply the first equation by 7 and the second equation by 5 to align coefficients of x
eq1 = (7 * 上禾1, 7 * 下禾1, 7 * 損實1)  # (35, -49, 77)
eq2 = (5 * 上禾2, 5 * 下禾2, 5 * 損實2)  # (35, -25, 125)

# Subtract eq1 from eq2 to eliminate x
下禾_coeff = eq2[1] - eq1[1]  # -25 - (-49) = 24
損實_diff = eq2[2] - eq1[2]  # 125 - 77 = 48

# Solve for y (grain per bundle of lower millet)
b = Fraction(損實_diff, 下禾_coeff)  # 48 / 24 = 2 (sheng)

# Substitute y back into the first equation to solve for x (grain per bundle of upper millet)
損實_sub = 損實1 - 下禾1 * b  # 77 - (-7 * 2) = 77 + 14 = 91
a = Fraction(損實_sub, 上禾1)  # 91 / 5 = 5 (sheng)

# Results
a = 5  # Upper millet grain per bundle
b = 2  # Lower millet grain per bundle#----- content ends here -----

"""
"""
