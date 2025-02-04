"""
今有戶高多於廣六尺八寸兩隅相去適一丈問戶高廣各幾何
術曰令一丈自乘為實半相多令自乘倍之減實半其餘以開方除之所得減相多之半即戶廣加相多之半即戶高
荅曰廣 a尺 高 b尺 
"""

"""
Suppose there is a door where the height exceeds the width by 6 chi and 8 cun. The diagonal distance between the two opposite corners is exactly 1 zhang.
Question: what are the height and width of the door?

The procedure says: Let 1 zhang (the diagonal) multiply itself to obtain the dividend.
Take half of the difference between the height and the width, let it multiply itself, and double it. Subtract this from the dividend.
Take half of the remainder and extract its square root. Divide by this.
The result, subtracting half of the difference, gives the width of the door.
Adding half of the difference gives the height of the door.

The answer says: the width is *a* chi, and the height is *b* chi.
"""

from fractions import Fraction
from math import sqrt

# 戶高多於廣六尺八寸
相多 = 6 + Fraction(8, 10)  # Convert 6 chi 8 cun to chi

# 兩隅相去適一丈
對角 = 10  # 1 zhang = 10 chi

# 令一丈自乘為實
實 = 對角 ** 2

# 半相多令自乘
半相多 = Fraction相多, 2)
半相多自乘 = 半相多 ** 2

# 倍之減實
餘 = 實 - 2 * 半相多自乘

# 半其餘
半餘 = Fraction(餘, 2)

# 以開方除之
開方 = sqrt(半餘)

# 所得減相多之半，即戶廣
戶廣 = 開方 - 半相多

# 加相多之半，即戶高
戶高 = 開方 + 半相多

a = 戶廣
b = 戶高
"""
Code error: unmatched ')' (<string>, line 28)"""
