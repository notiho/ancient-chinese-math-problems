"""
今有戶高多於廣六尺八寸，兩隅相去適一丈。問︰戶高、廣各幾何？
術曰：令一丈自乘為實。半相多，令自乘，倍之，減實，半其餘。以開方除之，所得，減相多之半，即戶廣。加相多之半，即戶高。
荅曰：廣 a(=14/5)尺 ；高 b(=48/5)尺 。
"""

#----- content starts here -----
"""
Suppose there is a door whose height exceeds its width by 6 chi and 8 cun (6 chi 8 cun = 6 + 8/10 = 68/10 = 34/5 chi).
The diagonal distance between the two opposite corners is exactly 1 zhang (10 chi).
Question: what are the height and width of the door?

The procedure says: Let 1 zhang (10 chi) square itself to obtain the dividend.
Take half of the difference between height and width, let it square itself, double it, and subtract it from the dividend.
Halve the remainder. Extract the square root of this, and divide it by the square root of the divisor.
The result, subtracting half of the difference, gives the width of the door.
Adding half of the difference gives the height of the door.

Answer: The width is *a*(=14/5) chi, and the height is *b*(=48/5) chi.
"""

from fractions import Fraction
import math

# 戶高多於廣六尺八寸
相多 = Fraction(34, 5)  # 6 chi 8 cun = 34/5 chi

# 兩隅相去適一丈
對角線 = 10  # 1 zhang = 10 chi

# 令一丈自乘為實
實 = 對角線 ** 2

# 半相多
半相多 = 相多 / 2

# 令自乘，倍之
倍半相多平方 = 2 * (半相多 ** 2)

# 減實
餘 = 實 - 倍半相多平方

# 半其餘
半餘 = 餘 / 2

# 以開方除之
開方 = math.sqrt(半餘)

# 所得，減相多之半，即戶廣
戶廣 = Fraction(開方) - 半相多

# 加相多之半，即戶高
戶高 = Fraction(開方) + 半相多

a = 戶廣  # 14/5 chi
b = 戶高  # 48/5 chi#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 14/5, Actual: 15762598695796737/5629499534213120
Variable 'b' has wrong value. Expected: 48/5, Actual: 54043195528445953/5629499534213120"""
