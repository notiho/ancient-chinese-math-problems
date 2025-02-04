"""
今有上禾五秉，損實一斗一升，當下禾七秉。上禾七秉，損實二斗五升，當下禾五秉。問︰上、下禾實一秉各幾何？
術曰：如方程，置上禾五秉正，下禾七秉負，損實一斗一升正。次置上禾七秉正，下禾五秉負，損實二斗五升正。以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：上禾一秉 a(=5)升 ，下禾一秉 b(=2)升 。
"""

"""
Suppose there are 5 bundles of upper millet, losing 1 dou and 1 sheng of grain, equivalent to 7 bundles of lower millet.
Suppose there are 7 bundles of upper millet, losing 2 dou and 5 sheng of grain, equivalent to 5 bundles of lower millet.
Question: how much grain does one bundle of upper millet and one bundle of lower millet yield?

The procedure says: As in solving simultaneous equations, place 5 bundles of upper millet as positive, 7 bundles of lower millet as negative, and the loss of 1 dou and 1 sheng as positive.
Next, place 7 bundles of upper millet as positive, 5 bundles of lower millet as negative, and the loss of 2 dou and 5 sheng as positive.
Use the positive-negative method to solve.

The method for solving simultaneous equations says: Place 3 bundles of upper millet, 2 bundles of middle millet, and 1 bundle of lower millet, with a total of 39 dou on the right side.
Arrange the middle and left millet as on the right side.
Multiply the upper millet row by the middle row and divide by the diagonal.
Repeat the multiplication and division for the next row.
Then, multiply the middle row by the lower row and divide by the diagonal.
For the left side, if the lower millet is not fully divisible, take the upper as the divisor and the lower as the dividend.
The result is the yield of the lower millet.
To find the middle millet, multiply the middle row by the lower yield and divide by the lower millet's yield.
The remainder, divided by the middle millet's bundle count plus one, gives the yield of the middle millet.
To find the upper millet, multiply the upper row by the lower yield and divide by the yields of the lower and middle millet.
The remainder, divided by the upper millet's bundle count plus one, gives the yield of the upper millet.
The yields are as per the method, each yielding 1 dou.

Answer: One bundle of upper millet yields *a*(=5) sheng, and one bundle of lower millet yields *b*(=2) sheng.
"""

from fractions import Fraction

# 上禾五秉，損實一斗一升，當下禾七秉
上禾1 = 5
下禾1 = -7
損實1 = 1 * 10 + 1  # 1斗1升 = 11升

# 上禾七秉，損實二斗五升，當下禾五秉
上禾2 = 7
下禾2 = -5
損實2 = 2 * 10 + 5  # 2斗5升 = 25升

# 用正負術解方程
# 計算行列式的主對角線和副對角線
主對角線 = 上禾1 * 下禾2
副對角線 = 上禾2 * 下禾1

# 計算行列式的值
行列式 = 主對角線 - 副對角線

# 計算上禾和下禾的實
a = Fraction((損實1 * 下禾2 - 損實2 * 下禾1), 行列式)  # 上禾一秉的實
b = Fraction((上禾1 * 損實2 - 上禾2 * 損實1), 行列式)  # 下禾一秉的實

a = a.numerator // a.denominator  # 上禾一秉 = 5升
b = b.numerator // b.denominator  # 下禾一秉 = 2升
"""
"""
