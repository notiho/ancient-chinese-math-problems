"""
今有戶高多於廣六尺八寸，兩隅相去適一丈。問︰戶高、廣各幾何？
術曰：令一丈自乘為實。半相多，令自乘，倍之，減實，半其餘。以開方除之，所得，減相多之半，即戶廣。加相多之半，即戶高。
荅曰：廣 a尺 ；高 b尺 。
"""

#----- content starts here -----
"""
Suppose there is a door where the height exceeds the width by 6 chi and 8 cun (6.8 chi). 
The diagonal distance between the two corners is exactly 1 zhang (10 chi).
Question: what are the height and width of the door?

The procedure says: Square 1 zhang (the diagonal), obtaining the dividend.
Take half of the excess (the difference between height and width), square it, double it, and subtract it from the dividend.
Take half of the remainder.
Extract the square root of this, and divide it.
The result, subtracting half of the excess, gives the width of the door.
Adding half of the excess gives the height of the door.

Answer: the width is *a* chi; the height is *b* chi.
"""

from fractions import Fraction
from math import sqrt

# 兩隅相去適一丈 (diagonal = 1 zhang = 10 chi)
對角線 = 10

# 高多於廣六尺八寸 (height exceeds width by 6 chi and 8 cun = 6.8 chi)
相多 = Fraction(68, 10)  # 6.8 chi as a fraction

# 令一丈自乘為實 (square the diagonal)
實 = 對角線 ** 2

# 半相多 (half of the excess)
半相多 = Fraction相多, 2)

# 令自乘，倍之 (square half of the excess and double it)
減數 = 2 * (半相多 ** 2)

# 減實 (subtract this from the squared diagonal)
餘 = 實 - 減數

# 半其餘 (take half of the remainder)
半餘 = Fraction(餘, 2)

# 以開方除之 (extract the square root of this)
開方 = sqrt(半餘)

# 所得，減相多之半，即戶廣 (subtract half of the excess to get the width)
戶廣 = 開方 - 半相多

# 加相多之半，即戶高 (add half of the excess to get the height)
戶高 = 開方 + 半相多

a = 戶廣
b = 戶高#----- content ends here -----

"""
Code error: unmatched ')' (<string>, line 30)"""
