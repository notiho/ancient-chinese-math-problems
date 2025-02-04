"""
今有戶高多於廣六尺八寸，兩隅相去適一丈。問︰戶高、廣各幾何？
術曰：令一丈自乘為實。半相多，令自乘，倍之，減實，半其餘。以開方除之，所得，減相多之半，即戶廣。加相多之半，即戶高。
荅曰：廣 a尺 ；高 b尺 。
"""

#----- content starts here -----
"""
Suppose there is a door whose height exceeds its width by 6 chi and 8 cun. The diagonal distance between the two opposite corners is exactly 1 zhang.
Question: what are the height and width of the door?

The procedure says: Let 1 zhang (the diagonal) be squared to obtain the dividend.
Take half of the excess (the difference between height and width), square it, double it, and subtract it from the dividend. Halve the remainder.
Extract the square root of this result, and subtract half of the excess to obtain the width of the door.
Add half of the excess to obtain the height of the door.

Answer: the width is *a* chi, and the height is *b* chi.
"""

from fractions import Fraction
from math import sqrt

# 兩隅相去適一丈 (diagonal distance)
對角線 = 10  # 1 zhang = 10 chi

# 高多於廣六尺八寸 (height exceeds width by 6 chi and 8 cun)
相多 = 6 + Fraction(8, 10)  # 8 cun = 8/10 chi

# 令一丈自乘為實 (square the diagonal)
實 = 對角線 ** 2

# 半相多 (half of the excess)
半相多 = Fraction相多, 2)

# 令自乘，倍之 (square half of the excess and double it)
半相多平方倍 = 2 * (半相多 ** 2)

# 減實 (subtract from the dividend)
餘 = 實 - 半相多平方倍

# 半其餘 (halve the remainder)
半餘 = Fraction(餘, 2)

# 以開方除之 (extract the square root)
平方根 = sqrt(半餘)

# 所得，減相多之半，即戶廣 (subtract half of the excess to get the width)
戶廣 = 平方根 - 半相多

# 加相多之半，即戶高 (add half of the excess to get the height)
戶高 = 平方根 + 半相多

# Final answers
a = 戶廣
b = 戶高#----- content ends here -----

"""
Code error: unmatched ')' (<string>, line 27)"""
