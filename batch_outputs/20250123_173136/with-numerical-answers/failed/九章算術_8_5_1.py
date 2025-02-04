"""
今有上禾三秉，益實六斗，當下禾十秉。下禾五秉，益實一斗，當上禾二秉。問︰上、下禾實一秉各幾何？
術曰：如方程，置上禾三秉正，下禾一十秉負，益實六斗負。次置上禾二秉負，下禾五秉正，益實一斗負。以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：上禾一秉實 a(=8)斗 ，下禾一秉實 b(=3)斗 。
"""

"""
Suppose there are 3 bundles of upper millet, which increase the yield by 6 dou, equivalent to 10 bundles of lower millet.
And 5 bundles of lower millet, which increase the yield by 1 dou, equivalent to 2 bundles of upper millet.
Question: how much yield does one bundle of upper millet and one bundle of lower millet produce respectively?

The procedure says: As in the method of solving simultaneous equations, place 3 bundles of upper millet as positive, 10 bundles of lower millet as negative, and 6 dou as negative.
Next, place 2 bundles of upper millet as negative, 5 bundles of lower millet as positive, and 1 dou as negative.
Use the method of positive and negative to solve.

The method of solving simultaneous equations says: Place 3 bundles of upper millet, 2 bundles of middle millet, and 1 bundle of lower millet, with the total yield of 39 dou, on the right side.
Arrange the middle and left millet as on the right side.
Multiply the upper millet row by the middle row and divide directly.
Then multiply by the next row and also divide directly.
Then, multiply the middle row by the middle millet that is not fully accounted for in the left row and divide directly.
For the lower millet that is not fully accounted for on the left side, the upper value becomes the divisor, and the lower value becomes the dividend. The dividend is the yield of the lower millet.
To find the middle millet, multiply the divisor by the middle row's lower yield and divide by the yield of the lower millet. The remainder, according to the number of middle millet bundles, is the yield of the middle millet.
To find the upper millet, also multiply the divisor by the right row's lower yield and divide by the yields of the lower and middle millet. The remainder, according to the number of upper millet bundles, is the yield of the upper millet.
The yields are all as per the divisor, and each is obtained in dou.

Answer: One bundle of upper millet produces *a*(=8) dou, and one bundle of lower millet produces *b*(=3) dou.
"""

from fractions import Fraction

# Equation 1: 3 bundles of upper millet, -10 bundles of lower millet, -6 dou
上禾1 = 3
下禾1 = -10
實1 = -6

# Equation 2: -2 bundles of upper millet, 5 bundles of lower millet, -1 dou
上禾2 = -2
下禾2 = 5
實2 = -1

# Solve using elimination
# Multiply the first equation by 2 and the second equation by 3 to align the coefficients of 上禾
上禾系數1 = 2 * 上禾1
下禾系數1 = 2 * 下禾1
實系數1 = 2 * 实1

上禾系數2 = 3 * 上禾2
下禾系數2 = 3 * 下禾2
實系數2 = 3 * 实2

# Eliminate 上禾
下禾系數 = 下禾系數1 + 下禾系數2
實系數 = 實系數1 + 實系數2

# Solve for 下禾 (lower millet yield per bundle)
b = Fraction(-實系數, 下禾系數)  # 3 dou

# Substitute b back into the first equation to solve for 上禾 (upper millet yield per bundle)
實1_adjusted = 實1 - (下禾1 * b)
a = Fraction(-實1_adjusted, 上禾1)  # 8 dou

# Results
a = 8  # Upper millet yield per bundle
b = 3  # Lower millet yield per bundle
"""
Code error: name '实1' is not defined"""
