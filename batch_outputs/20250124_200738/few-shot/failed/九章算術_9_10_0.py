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

The procedure says: Take 1 zhang (10 chi), square it to obtain the dividend.
Take half of the difference between the height and width, square it, double it, and subtract it from the dividend.
Take half of the remainder, and extract the square root.
Subtract half of the difference from the square root to obtain the width of the door.
Add half of the difference to the square root to obtain the height of the door.

Answer: the width is *a* chi, and the height is *b* chi.
"""

from fractions import Fraction
import math

# 戶高多於廣六尺八寸
相多 = Fraction(6, 1) + Fraction(8, 10)  # 6 chi and 8 cun = 6.8 chi

# 兩隅相去適一丈
對角線 = 10  # 1 zhang = 10 chi

# 令一丈自乘為實
實 = 對角線 ** 2

# 半相多
半相多 = 相多 / 2

# 令自乘，倍之
半相多平方倍 = 2 * (半相多 ** 2)

# 減實
餘 = 實 - 半相多平方倍

# 半其餘
半餘 = 餘 / 2

# 以開方除之
開方 = math.sqrt(半餘)

# 所得，減相多之半，即戶廣
戶廣 = 開方 - 半相多

# 加相多之半，即戶高
戶高 = 開方 + 半相多

a = 戶廣
b = 戶高#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 14/5, Actual: 2.8000000000000003
Variable 'b' has wrong value. Expected: 48/5, Actual: 9.6"""
