"""
今有戶高多於廣六尺八寸，兩隅相去適一丈。問︰戶高、廣各幾何？
術曰：令一丈自乘為實。半相多，令自乘，倍之，減實，半其餘。以開方除之，所得，減相多之半，即戶廣。加相多之半，即戶高。
荅曰：廣 a尺 ；高 b尺 。
"""

"""
Suppose there is a door whose height exceeds its width by 6 chi and 8 cun (6.8 chi). 
The diagonal distance between the two opposite corners is exactly 1 zhang (10 chi).
Question: what are the height and width of the door?

The procedure says: Let 1 zhang (10 chi) be squared to obtain the dividend. 
Half the excess (6.8 chi) is squared, doubled, and subtracted from the dividend. 
Take half of the remainder. Extract the square root of this, and divide by it. 
The result, subtracting half the excess, gives the width of the door. 
Adding half the excess gives the height of the door.

Answer: the width is *a* chi; the height is *b* chi.
"""

from fractions import Fraction
from math import sqrt

# 戶高多於廣六尺八寸
相多 = Fraction(68, 10)  # 6 chi 8 cun = 6.8 chi

# 兩隅相去適一丈
對角線 = 10  # 1 zhang = 10 chi

# 令一丈自乘為實
實 = 對角線 ** 2

# 半相多
半相多 = Fraction相多, 2)

# 令自乘，倍之
半相多平方倍 = 2 * (半相多 ** 2)

# 減實
餘 = 實 - 半相多平方倍

# 半其餘
半餘 = Fraction(餘, 2)

# 以開方除之
戶廣 = sqrt(半餘)

# 所得，減相多之半，即戶廣
戶廣 -= 半相多

# 加相多之半，即戶高
戶高 = 戶廣 + 相多

a = 戶廣
b = 戶高
"""
Code error: unmatched ')' (<string>, line 29)"""
