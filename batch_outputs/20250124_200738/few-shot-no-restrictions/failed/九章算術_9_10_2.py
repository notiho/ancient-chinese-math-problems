"""
今有戶高多於廣六尺八寸，兩隅相去適一丈。問︰戶高、廣各幾何？
術曰：令一丈自乘為實。半相多，令自乘，倍之，減實，半其餘。以開方除之，所得，減相多之半，即戶廣。加相多之半，即戶高。
荅曰：廣 a尺 ；高 b尺 。
"""

#----- content starts here -----
"""
Suppose there is a door where the height exceeds the width by 6 chi and 8 cun (6.8 chi). 
The diagonal distance between the two opposite corners is exactly 1 zhang (10 chi).
Question: what are the height and width of the door?

The procedure says: Let 1 zhang (10 chi) square itself to become the "product."
Take half of the excess (6.8 chi), let it square itself, double it, and subtract it from the product. 
Take half of the remainder. Extract the square root of this value and divide it. 
The result, subtracting half of the excess, gives the width of the door. 
Adding half of the excess gives the height of the door.

Answer: the width is *a* chi, and the height is *b* chi.
"""

from fractions import Fraction
from math import sqrt

# 戶高多於廣六尺八寸
相多 = 6 + Fraction(8, 10)  # 6 chi 8 cun = 6.8 chi

# 兩隅相去適一丈
對角線 = 10  # 1 zhang = 10 chi

# 令一丈自乘為實
實 = 對角線 ** 2

# 半相多
半相多 = Fraction相多 / 2

# 令自乘，倍之
倍半相多平方 = 2 * (半相多 ** 2)

# 減實
餘 = 實 - 倍半相多平方

# 半其餘
半餘 = 餘 / 2

# 以開方除之
開方 = sqrt(半餘)

# 所得，減相多之半，即戶廣
戶廣 = 開方 - 半相多

# 加相多之半，即戶高
戶高 = 開方 + 半相多

# 答案
a = 戶廣
b = 戶高

a, b#----- content ends here -----

"""
Code error: name 'Fraction相多' is not defined"""
